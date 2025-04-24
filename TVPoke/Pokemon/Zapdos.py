from TVPoke.BaseClasses.PokeTypes import Electric
from TVPoke.BaseClasses.Move import Move

class Zapdos(Electric):
    def __init__(self):
        moves = [
            Move("Thunderbolt", "ELECTRIC", 90, "Special"),
            Move("Air Cutter", "FLYING", 60, "Special"),
            Move("Heat Wave", "FIRE", 100, "Special"),
            Move("Ominous Wind", "GHOST", 60, "Special")
        ]
        stats = {
            "healthPoints": 90,
            "attack": 90,
            "defense": 85,
            "specialAttack": 125,
            "specialDefense": 90,
            "speed": 100
        }
        
        statBuffs = {
            "healthPoints": 1,
            "attack": 1,
            "defense": 1,
            "specialAttack": 1,
            "specialDefense": 1,
            "speed": 1
            }
        
        super().__init__("Zapdos", stats["healthPoints"], moves, "./TVPoke/Pokemon/imgs/Zapdos.png", stats, statBuffs)

