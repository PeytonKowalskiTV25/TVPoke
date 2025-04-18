from TVPoke.BaseClasses.PokeTypes import Water
from TVPoke.BaseClasses.Move import Move

class Golduck(Water):
    def __init__(self):
        moves = [
            Move("Hydro Pump", "WATER", 110, "Special"),
            Move("Zen Headbutt", "PSYCHIC", 80, "Physical"),
            Move("Ice Beam", "ICE", 90, "Special"),
            Move("Surf", "WATER", 90, "Special")
        ]
        stats = {
            "healthPoints": 80,
            "attack": 82,
            "defense": 78,
            "specialAttack": 95,
            "specialDefense": 80,
            "speed": 85
        }
        super().__init__("Golduck", stats["healthPoints"], moves, "./TVPoke/Pokemon/imgs/Golduck.png", stats)

