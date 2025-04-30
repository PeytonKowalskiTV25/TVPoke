from TVPoke.BaseClasses.PokeTypes import Ghost
from TVPoke.BaseClasses.Move import Move

class Gengar(Ghost):
    def __init__(self):
        moves = [
            Move("Shadow Ball", "GHOST", 80, "Special"),
            Move("Focus Blast", "FIGHTING", 120, "Special"),
            Move("Will-O-Wisp", "FIRE", 0, "Status"),
            Move("Hidden Power Ice", "ICE", 70, "Special")
        ]
        stats = {
            "healthPoints": 60,
            "attack": 65,
            "defense": 60,
            "specialAttack": 130,
            "specialDefense": 75,
            "speed": 110
        }
        
        statBuffs = {
            "healthPoints": 1,
            "attack": 1,
            "defense": 1,
            "specialAttack": 1,
            "specialDefense": 1,
            "speed": 1
        }
        
        super().__init__("Gengar", stats["healthPoints"], moves, "./TVPoke/Pokemon/imgs/Gengar.png", stats, statBuffs)