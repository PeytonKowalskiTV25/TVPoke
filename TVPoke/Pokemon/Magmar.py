from TVPoke.BaseClasses.PokeTypes import Fire
from TVPoke.BaseClasses.Move import Move

class Magmar(Fire):
    def __init__(self):
        moves = [
            Move("Flamethrower", "FIRE", 90, "Special"),
            Move("Fire Punch", "FIRE", 75, "Physical"),
            Move("Thunder Punch", "ELECTRIC", 75, "Physical"),
            Move("Confuse Ray", "GHOST", 0, "Status")
        ]
        stats = {
            "healthPoints": 65,
            "attack": 95,
            "defense": 57,
            "specialAttack": 100,
            "specialDefense": 85,
            "speed": 93
        }
        super().__init__("Magmar", stats["healthPoints"], moves, "./TVPoke/Pokemon/imgs/Magmar.png", stats)