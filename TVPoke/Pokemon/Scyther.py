from TVPoke.BaseClasses.PokeTypes import Bug
from TVPoke.BaseClasses.Move import Move

class Scyther(Bug):
    def __init__(self):
        moves = [
            Move("X-Scissor", "BUG", 80, "Physical"),
            Move("Wing Attack", "FLYING", 60, "Physical"),
            Move("Slash", "NORMAL", 70, "Physical"),
            Move("Quick Attack", "NORMAL", 40, "Physical")
        ]
        stats = {
            "healthPoints": 70,
            "attack": 110,
            "defense": 80,
            "specialAttack": 55,
            "specialDefense": 80,
            "speed": 105
        }
        
        statBuffs = {
            "healthPoints": 1,
            "attack": 1,
            "defense": 1,
            "specialAttack": 1,
            "specialDefense": 1,
            "speed": 1
            }
        
        super().__init__("Scyther", stats["healthPoints"], moves, "./TVPoke/Pokemon/imgs/Scyther.png", stats, statBuffs)