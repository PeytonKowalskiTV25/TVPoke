from TVPoke.BaseClasses.PokeTypes import Grass
from TVPoke.BaseClasses.Move import Move

class Exeggutor(Grass):
    def __init__(self):
        moves = [
            Move("Seed Bomb", "GRASS", 80, "Physical"),
            Move("Psychic", "PSYCHIC", 90, "Special"),
            Move("Stomp", "NORMAL", 65, "Physical"),
            Move("Sludge Bomb", "POISON", 90, "Special")
        ]
        stats = {
            "healthPoints": 95,
            "attack": 95,
            "defense": 85,
            "specialAttack": 125,
            "specialDefense": 75,
            "speed": 55
        }
        
        statBuffs = {
            "healthPoints": 1,
            "attack": 1,
            "defense": 1,
            "specialAttack": 1,
            "specialDefense": 1,
            "speed": 1
            }
        
        super().__init__("Exeggutor", stats["healthPoints"], moves, "./TVPoke/Pokemon/imgs/Exeggutor.png", stats, statBuffs)