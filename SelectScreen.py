from PyUI.Screen import Screen
from PyUI.PageElements import *
from TVPoke.helper import getAllPokemonNames

class SelectScreen(Screen):
    def __init__(self, window):
        super().__init__(window, (4,50,3))
        self.state = {
            "selectedPoke": [],
            "pageNum": 0,
            "pokemon": getAllPokemonNames(),
            "pokemonShowing": [],
            "hasNextPage": False,
            "hasPrevPage": False
        }
        self.updatePokemonShowing()


    def elementsToDisplay(self):
        self.elements = [ 
            Label((25, 95), 50, 10, "Choose your pokemon!", 24)
        ]
        itemsPerRow = 3
        rowsOfItems = 3


        #uses left part of screen for pokemon to select, right to show pokemon selected

        xCoord = 0
        indexOnPage = -1
        print(self.state["pokemonShowing"])
        for x in range(itemsPerRow):
            yCoord = 0
            xCoord += 50/(itemsPerRow + 1)
            for y in range(rowsOfItems):
                indexOnPage += 1
                yCoord += 80/(itemsPerRow + 1)
                if indexOnPage < len(self.state["pokemonShowing"]):
                    self.elements.append(PokeImage((xCoord, yCoord), self.state["pokemonShowing"][indexOnPage], 50/itemsPerRow, 80/rowsOfItems))
                    indexOnPage += 1
                else:
                    break

        if self.state["hasPrevPage"]:
            self.elements.append(BackButton())
        if self.state["hasNextPage"]:
            self.elements.append(ForwardButton())

        #uses right part of screen to show pokemon selected
        yCoord = 0
        for p in self.state["selectedPoke"]:
            yCoord += 100/4
            self.elements.append(SelectedPokeImage((75, yCoord), p, 20, 100/4))


    def updatePokemonShowing(self):
        startIndex = self.state["pageNum"] * 9
        self.state["hasPrevPage"] = startIndex > 0
        pokeShowing = []
        self.state["hasNextPage"] = True
        for i in range(startIndex, startIndex + 9):
            if i < len(self.state["pokemon"]):
                pokeShowing.append(self.state["pokemon"][i])
            else:
                self.state["hasNextPage"] = False
                break
        self.state["pokemonShowing"] = pokeShowing
                



class PokeImage(Image):
    def __init__(self, pos, name, width, height):
        self.name = name
        super().__init__(pos, width, height, './TVPoke/Pokemon/imgs/' + name + '.png')

    def onClick(self, screen):
        screen.state["selectedPoke"].append(self.name)

class SelectedPokeImage(Image):
    def __init__(self, pos, name, width, height):
        self.name = name
        super().__init__(pos, width, height, './TVPoke/Pokemon/imgs/' + name + '.png')

    def onClick(self, screen):
        screen.state["selectedPoke"].remove(self)

class BackButton(Image):
    def __init__(self):
        super().__init__((45, 85), 10, 10, './imgs/BackButton.png')

    def onClick(self, screen):
        screen.state["pageNum"] -= 1
        screen.updatePokemonShowing()

class ForwardButton(Image):
    def __init__(self):
        super().__init__((45, 85), 10, 10, './imgs/ForwardButton.png')

    def onClick(self, screen):
        screen.state["pageNum"] += 1
        screen.updatePokemonShowing()

    
        
