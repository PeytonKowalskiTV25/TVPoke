from TVPoke.BaseClasses.PokeTypes import Psychic
from TVPoke.BaseClasses.Move import Move

class MrMime(Psychic):
    def __init__(self):
        moves = [
            Move("Psychic", "PSYCHIC", 90, "Special"),
            Move("Dazzling Gleam", "FAIRY", 80, "Special"),
            Move("Barrier", "PSYCHIC", 0, "Status"),
            Move("Shadow Ball", "GHOST", 80, "Special")
        ]
        stats = {
            "healthPoints": 40,
            "attack": 45,
            "defense": 65,
            "specialAttack": 100,
            "specialDefense": 120,
            "speed": 90
        }
        super().__init__("Mr. Mime", stats["healthPoints"], moves, "./TVPoke/Pokemon/imgs/MrMime.png", stats)