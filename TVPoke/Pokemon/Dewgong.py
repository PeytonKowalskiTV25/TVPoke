from TVPoke.BaseClasses.PokeTypes import Water
from TVPoke.BaseClasses.Move import Move

class Dewgong(Water):
    def __init__(self):
        moves = [
            Move("Ice Shard", "ICE", 40, "Physical"),
            Move("Aurora Beam", "ICE", 65, "Special"),
            Move("Surf", "WATER", 90, "Special"),
            Move("Rest", "PSYCHIC", 0, "Status")
        ]
        stats = {
            "healthPoints": 90,
            "attack": 70,
            "defense": 80,
            "specialAttack": 70,
            "specialDefense": 95,
            "speed": 70
        }
        super().__init__("Dewgong", stats["healthPoints"], moves, "./TVPoke/Pokemon/imgs/Dewgong.png", stats)