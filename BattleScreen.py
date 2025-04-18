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
        
        self.activePokemon = self.activeTrainer.pokemon[0]
        
        buttonWidth = 20
        buttonHeight = 10
        margin = 5
        startX = 60
        startY = 10
    
        for index, move in enumerate(self.activePokemon.moves):
            row = index // 2
            col = index % 2
            buttonX = startX + col * (buttonWidth + margin)
            buttonY = startY + row * (buttonHeight + margin)
            self.elements.append(MoveButton((buttonX, buttonY), move))

class MoveButton(Button):
    def __init__(self, centerXY, move):
        super().__init__(centerXY, 20, 10, move.name)
        self.moveName = move.name
        self.move = move
    
    def onClick(self, screen):
        print(f"{screen.activePokemon.name} used {self.moveName}")



