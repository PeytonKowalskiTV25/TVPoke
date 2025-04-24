from TVPoke.BaseClasses.PokeTypes import Ground
from TVPoke.BaseClasses.Move import Move

class Diglett(Ground):
    def __init__(self):
        moves = [
            Move("Mud-Slap", "GROUND", 20, "Special"),
            Move("Dig", "GROUND", 80, "Physical"),
            Move("Scratch", "NORMAL", 40, "Physical"),
            Move("Earthquake", "GROUND", 100, "Physical")
        ]
        stats = {
            "healthPoints": 10,
            "attack": 55,
            "defense": 25,
            "specialAttack": 35,
            "specialDefense": 45,
            "speed": 95
        }
        
        statBuffs = {
            "healthPoints": 1,
            "attack": 1,
            "defense": 1,
            "specialAttack": 1,
            "specialDefense": 1,
            "speed": 1
            }
        
        super().__init__("Diglett", stats["healthPoints"], moves, "./TVPoke/Pokemon/imgs/Diglett.png", stats, statBuffs)