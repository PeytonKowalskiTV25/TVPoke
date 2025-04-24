from TVPoke.BaseClasses.PokeTypes import Dragon
from TVPoke.BaseClasses.Move import Move

class Dragonite(Dragon):
    def __init__(self):
        moves = [
            Move("Dragon Claw", "DRAGON", 80, "Physical"),
            Move("Hurricane", "FLYING", 110, "Special"),
            Move("Thunder Punch", "ELECTRIC", 75, "Physical"),
            Move("Fire Punch", "FIRE", 75, "Physical")
        ]
        stats = {
            "healthPoints": 91,
            "attack": 134,
            "defense": 95,
            "specialAttack": 100,
            "specialDefense": 100,
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
        
        super().__init__("Dragonite", stats["healthPoints"], moves, "./TVPoke/Pokemon/imgs/Dragonite.png", stats)