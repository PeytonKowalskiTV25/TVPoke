from TVPoke.BaseClasses.PokeTypes import Water
from TVPoke.BaseClasses.Move import Move

class Vaporeon(Water):
    def __init__(self):
        moves = [
            Move("Surf", "WATER", 90, "Special"),
            Move("Ice Beam", "ICE", 90, "Special"),
            Move("Shadow Ball", "GHOST", 80, "Special"),
            Move("Hydro Pump", "WATER", 110, "Special")
        ]
        stats = {
            "healthPoints": 130,
            "attack": 65,
            "defense": 60,
            "specialAttack": 110,
            "specialDefense": 95,
            "speed": 65
        }
        super().__init__("Vaporeon", stats["healthPoints"], moves, "./TVPoke/Pokemon/imgs/Vaporeon.png", stats)