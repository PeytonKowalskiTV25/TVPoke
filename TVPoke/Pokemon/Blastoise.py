from TVPoke.BaseClasses.PokeTypes import Water
from TVPoke.BaseClasses.Move import Move

class Blastoise(Water):
    def __init__(self):
        moves = [
            Move("Body Slam", "NORMAL", 40, "Physical"),
            Move("Water Cannon", "WATER", 30, "Special"),
            Move("Power Wash", "WATER", 50, "Special"),
            Move("Quake", "ROCK", 20, "Physical")
        ]
        stats = {
            "healthPoints": 79,
            "attack": 83,
            "defense": 100,
            "specialAttack": 85,
            "specialDefense": 105,
            "speed": 78
        }
        super().__init__("Blastoise", stats["healthPoints"], moves, "./TVPoke/Pokemon/imgs/Blastoise.png", stats)