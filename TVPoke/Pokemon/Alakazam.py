from TVPoke.BaseClasses.PokeTypes import Psychic
from TVPoke.BaseClasses.Move import Move

class Alakazam(Psychic):
    def __init__(self):
        moves = [
            Move("Fire Punch", "FIRE", 75, "Physical"),
            Move("Ice Punch", "ICE", 75, "Physical"),
            Move("Psycho Cut", "PSYCHIC", 70, "Physical"),
            Move("Future Sight", "PSYCHIC", 120, "Special")
        ]
        stats = {
            "healthPoints": 55,
            "attack": 50,
            "defense": 45,
            "specialAttack": 135,
            "specialDefense": 95,
            "speed": 120
        }
        super().__init__("Alakazam", stats["healthPoints"], moves, "./TVPoke/Pokemon/imgs/Alakazam.png", stats)