from TVPoke.BaseClasses.PokeTypes import Normal
from TVPoke.BaseClasses.Move import Move

class Snorlax(Normal):
    def __init__(self):
        moves = [
            Move("Body Slam", "NORMAL", 85, "Physical"),
            Move("Crunch", "DARK", 80, "Physical"),
            Move("Earthquake", "GROUND", 100, "Physical"),
            Move("Rest", "PSYCHIC", 0, "Status")
        ]
        stats = {
            "healthPoints": 160,
            "attack": 110,
            "defense": 65,
            "specialAttack": 65,
            "specialDefense": 110,
            "speed": 30
        }
        super().__init__("Snorlax", stats["healthPoints"], moves, "./TVPoke/Pokemon/imgs/Snorlax.png", stats)