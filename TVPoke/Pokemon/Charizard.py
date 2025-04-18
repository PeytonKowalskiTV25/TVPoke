from TVPoke.BaseClasses.PokeTypes import Fire
from TVPoke.BaseClasses.Move import Move

class Charizard(Fire):
    def __init__(self):
        moves = [
            Move("Tackle", "NORMAL", 40, "Physical"),
            Move("Flamethrower", "FIRE", 90, "Special"),
            Move("Body Slam", "NORMAL", 80, "Physical"),
            Move("Wing Attack", "FLYING", 60, "Physical")
        ]
        stats = {
            "healthPoints": 78,
            "attack": 84,
            "defense": 78,
            "specialAttack": 109,
            "specialDefense": 85,
            "speed": 100
        }
        super().__init__("Charizard", stats["healthPoints"], moves, "./TVPoke/Pokemon/imgs/Charizard.png", stats)