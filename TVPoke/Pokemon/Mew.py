from TVPoke.BaseClasses.PokeTypes import Psychic
from TVPoke.BaseClasses.Move import Move

class Mew(Psychic):
    def __init__(self):
        moves = [
            Move("Psychic", "PSYCHIC", 90, "Special"),
            Move("Aura Sphere", "FIGHTING", 80, "Special"),
            Move("Shadow Ball", "GHOST", 80, "Special"),
            Move("Thunderbolt", "ELECTRIC", 90, "Special")
        ]
        stats = {
            "healthPoints": 100,
            "attack": 100,
            "defense": 100,
            "specialAttack": 100,
            "specialDefense": 100,
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
        
        super().__init__("Mew", stats["healthPoints"], moves, "./TVPoke/Pokemon/imgs/Mew.png", stats, statBuffs)