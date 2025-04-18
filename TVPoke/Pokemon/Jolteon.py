from TVPoke.BaseClasses.PokeTypes import Electric
from TVPoke.BaseClasses.Move import Move

class Jolteon(Electric):
    def __init__(self):
        moves = [
            Move("Thunderbolt", "ELECTRIC", 90, "Special"),
            Move("Shadow Ball", "GHOST", 80, "Special"),
            Move("Volt Switch", "ELECTRIC", 70, "Special"),
            Move("Thunder Wave", "ELECTRIC", 0, "Status")
        ]
        stats = {
            "healthPoints": 65,
            "attack": 65,
            "defense": 60,
            "specialAttack": 110,
            "specialDefense": 95,
            "speed": 130
        }
        super().__init__("Jolteon", stats["healthPoints"], moves, "./TVPoke/Pokemon/imgs/Jolteon.png", stats)