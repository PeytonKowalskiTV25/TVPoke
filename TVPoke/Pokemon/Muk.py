from TVPoke.BaseClasses.PokeTypes import Poison
from TVPoke.BaseClasses.Move import Move

class Muk(Poison):
    def __init__(self):
        moves = [
            Move("Sludge Bomb", "POISON", 90, "Special"),
            Move("Gunk Shot", "POISON", 120, "Physical"),
            Move("Shadow Sneak", "GHOST", 40, "Physical"),
            Move("Acid Armor", "POISON", 0, "Status")
        ]
        stats = {
            "healthPoints": 105,
            "attack": 105,
            "defense": 75,
            "specialAttack": 65,
            "specialDefense": 100,
            "speed": 50
        }
        super().__init__("Muk", stats["healthPoints"], moves, "./TVPoke/Pokemon/imgs/Muk.png", stats)