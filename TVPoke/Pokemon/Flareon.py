from TVPoke.BaseClasses.PokeTypes import Fire
from TVPoke.BaseClasses.Move import Move

class Flareon(Fire):
    def __init__(self):
        moves = [
            Move("Flare Blitz", "FIRE", 120, "Physical"),
            Move("Fire Fang", "FIRE", 65, "Physical"),
            Move("Quick Attack", "NORMAL", 40, "Physical"),
            Move("Will-O-Wisp", "FIRE", 0, "Status")
        ]
        stats = {
            "healthPoints": 65,
            "attack": 130,
            "defense": 60,
            "specialAttack": 95,
            "specialDefense": 110,
            "speed": 65
        }
        
        statBuffs = {
            "healthPoints": 1,
            "attack": 1,
            "defense": 1,
            "specialAttack": 1,
            "specialDefense": 1,
            "speed": 1
            }
        
        super().__init__("Flareon", stats["healthPoints"], moves, "./TVPoke/Pokemon/imgs/Flareon.png", stats, statBuffs)