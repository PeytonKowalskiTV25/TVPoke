from PyUI.Screen import Screen
from TVPoke.BaseClasses.Trainer import Trainer
from PyUI.PageElements import *
from TVPoke.BaseClasses.EffectMoves import effectMoveList

class BattleScreen(Screen):
    def __init__(self, window):
        super().__init__(window, (25, 255, 40))
        self.state = {
            "goTo" : ""
        }
        self.trainers = []
        self.loser = ""
        self.winner = ""
        
    def addTrainers(self, trainer1Poke, trainer2Poke):
        self.trainers = [
            Trainer(trainer1Poke),
            Trainer(trainer2Poke)
        ]

        self.activeTrainer = self.trainers[0]
        self.trainers[0].name = "player 1"
        self.trainers[1].name = "player 2"

        for trainer in self.trainers:
            if trainer == self.activeTrainer:
                trainer.position = 1
            else:
                trainer.position = 2

    def checkLoser(self):
        for trainer in self.trainers:
            if len(trainer.pokemon) == 0:
                self.loser = trainer.name
                for guy in self.trainers:
                    if guy != trainer:
                        self.winner = guy.name
                        self.state["goTo"] = "WIN"
                break

    def elementsToDisplay(self):
        self.elements = [
            Arena(),
            Shape((82, 17), 60, 30, [(0, 0), (100, 0), (100, 100), (0, 100)], (100, 100, 100))
        ]

        self.checkLoser()

        for trainer in self.trainers:
            self.elements.extend(trainer.getElements())

        if self.loser != "":
            pass
        else:
            for i, move in enumerate(self.activeTrainer.pokemon[0].moves):
                x = 75 + (i % 2) * 15  
                y = 10 + (i // 2) * 15 
                self.elements.append(MoveButton((x,y), move))

class Arena(Image):
    def __init__(self):
        super().__init__((50, 50), 100, 100, "./imgs/battleground.jpg")

class MoveButton(Button):
    def __init__(self, centerXY, move):
        super().__init__(centerXY, 20, 10, move.name)
        self.move = move

    def onClick(self, screen):
        activePokemon = screen.activeTrainer.pokemon[0]
        targetTrainer = screen.trainers[1 if screen.activeTrainer == screen.trainers[0] else 0]
        targetPokemon = targetTrainer.pokemon[0]

        print(f"{activePokemon.name} used {self.move.name}")

        if self.move.damageCategory == "effect":
            for effectMove in effectMoveList:
                if self.move.name == effectMove["name"]:
                    affectedStat = effectMove["affectedStat"]
                    statModifier = effectMove["statModifier"]

                    # Handle effects
                    if "burn" in statModifier:
                        if not targetPokemon.burn["isBurned"]:
                            targetPokemon.inflictBurn()
                    elif "confusion" in affectedStat:
                        targetPokemon = screen.trainers[1 if screen.activeTrainer == screen.trainers[0] else 0].pokemon[0]
                        targetPokemon.inflictConfusion()
                        print(f"{targetPokemon.name} became confused!")
                    elif statModifier == "restore to full":  # Restore HP to full
                        activePokemon.hp = activePokemon.stats["healthPoints"]
                    elif isinstance(affectedStat, list):  # If multiple stats are affected
                        for stat in affectedStat:
                            activePokemon.statBuffs[stat] += float(statModifier)
                    else:  # Handle other stat modifiers
                        activePokemon.statBuffs[affectedStat] += float(statModifier)
        elif self.move.name == "Power up Punch":
            targetPokemon.takeDamage(self.move, activePokemon)
            activePokemon.statBuffs["attack"] += 1  # Increment attack stage
            print(f"{activePokemon.name}'s attack stage: {activePokemon.statBuffs['attack']}")
        else:
            targetPokemon.takeDamage(self.move, activePokemon)

        # Switch trainers or perform other game logic here
        if screen.activeTrainer == screen.trainers[0]:
            screen.activeTrainer = screen.trainers[1]
        else:
            screen.activeTrainer = screen.trainers[0]

        for trainer in screen.trainers:
            if trainer == screen.activeTrainer:
                trainer.position = 1
            else:
                trainer.position = 2
