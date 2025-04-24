from TVPoke.BaseClasses.PokeTypes import Water
from TVPoke.BaseClasses.Move import Move

class Magikarp(Water):
    def __init__(self):
        moves = [
            Move("Splash", "NORMAL", 0, "Status"),
            Move("Tackle", "NORMAL", 40, "Physical"),
            Move("Flail", "NORMAL", 50, "Physical"),
            Move("Bounce", "FLYING", 85, "Physical")
        ]
        stats = {
            "healthPoints": 20,
            "attack": 10,
            "defense": 55,
            "specialAttack": 15,
            "specialDefense": 20,
            "speed": 80
        }
        
        statBuffs = {
            "healthPoints": 1,
            "attack": 1,
            "defense": 1,
            "specialAttack": 1,
            "specialDefense": 1,
            "speed": 1
            }
        
        super().__init__("Magikarp", stats["healthPoints"], moves, "./TVPoke/Pokemon/imgs/Magikarp.png", stats, statBuffs)