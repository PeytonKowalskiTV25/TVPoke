from TVPoke.BaseClasses.PokeTypes import Fire
from TVPoke.BaseClasses.Move import Move

class Rapidash(Fire):
    def __init__(self):
        moves = [
            Move("Flare Blitz", "FIRE", 120, "Physical"),
            Move("Stomp", "NORMAL", 65, "Physical"),
            Move("Fire Spin", "FIRE", 35, "Special"),
            Move("Agility", "PSYCHIC", 0, "Status")
        ]
        stats = {
            "healthPoints": 65,
            "attack": 100,
            "defense": 70,
            "specialAttack": 80,
            "specialDefense": 80,
            "speed": 105
        }
        super().__init__("Rapidash", stats["healthPoints"], moves, "./TVPoke/Pokemon/imgs/Rapidash.png", stats)