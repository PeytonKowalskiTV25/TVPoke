from TVPoke.BaseClasses.PokeTypes import Water
from TVPoke.BaseClasses.Move import Move

class Psyduck(Water):
    def __init__(self):
        moves = [
            Move("Water Gun", "WATER", 40, "Special"),
            Move("Confusion", "PSYCHIC", 50, "Special"),
            Move("Scratch", "NORMAL", 40, "Physical"),
            Move("Zen Headbutt", "PSYCHIC", 80, "Physical")
        ]
        stats = {
            "healthPoints": 50,
            "attack": 52,
            "defense": 48,
            "specialAttack": 65,
            "specialDefense": 50,
            "speed": 55
        }
        super().__init__("Psyduck", stats["healthPoints"], moves, "./TVPoke/Pokemon/imgs/Psyduck.png", stats)