from TVPoke.BaseClasses.PokeTypes import Fairy
from TVPoke.BaseClasses.Move import Move

class Wigglytuff(Fairy):
    def __init__(self):
        moves = [
            Move("Play Rough", "FAIRY", 90, "Physical"),
            Move("Hyper Voice", "NORMAL", 90, "Special"),
            Move("Dazzling Gleam", "FAIRY", 80, "Special"),
            Move("Double-Edge", "NORMAL", 120, "Physical")
        ]
        stats = {
            "healthPoints": 140,
            "attack": 70,
            "defense": 45,
            "specialAttack": 85,
            "specialDefense": 50,
            "speed": 45
        }
        
        statBuffs = {
            "healthPoints": 1,
            "attack": 1,
            "defense": 1,
            "specialAttack": 1,
            "specialDefense": 1,
            "speed": 1
            }
        
        super().__init__("Wigglytuff", stats["healthPoints"], moves, "./TVPoke/Pokemon/imgs/Wigglytuff.png", stats, statBuffs)