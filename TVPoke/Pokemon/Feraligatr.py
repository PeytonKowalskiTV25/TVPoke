from TVPoke.BaseClasses.PokeTypes import Water
from TVPoke.BaseClasses.Move import Move

class Feraligatr(Water):
    def __init__(self):
        moves = [
            Move("Waterfall", "WATER", 80, "Physical"),
            Move("Crunch", "DARK", 80, "Physical"),
            Move("Ice Fang", "ICE", 65, "Physical"),
            Move("Dragon Dance", "DRAGON", 0, "Status")
        ]
        stats = {
            "healthPoints": 85,
            "attack": 105,
            "defense": 100,
            "specialAttack": 79,
            "specialDefense": 83,
            "speed": 78
        }
        super().__init__("Feraligatr", stats["healthPoints"], moves, "./TVPoke/Pokemon/imgs/Feraligatr.png", stats)