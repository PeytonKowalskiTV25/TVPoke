from PyUI.Screen import Screen
from TVPoke.BaseClasses.Trainer import Trainer
from PyUI.PageElements import *

class BattleScreen(Screen):
    def __init__(self, window):
        super().__init__(window, (25, 255, 40))
        self.trainers = []
        self.activeTrainer = []

    def addTrainers(self, trainer1Poke, trainer2Poke):
        self.trainers = [
            Trainer(trainer1Poke),
            Trainer(trainer2Poke)
        ]
        self.activeTrainer = self.trainers[0]
        
    def elementsToDisplay(self):
        self.elements = []

        for trainer in self.trainers:
            if trainer == self.activeTrainer:
                trainer.position = 1
            else:
                trainer.position = 2

        for trainer in self.trainers:
            self.elements.extend(trainer.getElements())

        if self.activeTrainer == self.trainers[0]:
            self.activeTrainer = self.trainers[1]
        else:
            self.activeTrainer = self.trainers[0]
        
        activePokemon = self.activeTrainer.pokemon[0]
        startX = 80
        startY = 30

        for index, move in enumerate(activePokemon.moves):
            buttonX = startX
            for index, move in enumerate(activePokemon.moves):
                buttonY = startY
                self.elements.append(MoveButton((buttonX, buttonY), move.name))

class MoveButton(Button):
    def __init__(self, centerXY, moveName):
        super().__init__(centerXY, 20, 10, moveName)
        self.moveName = moveName
    
    def onClick(self, screen):
        for trainer in screen.trainers:
            if trainer != screen.activeTrainer:
                screen.activePokemon.takeDamage()



