from TVPoke.BaseClasses.PokeTypes import Normal
from TVPoke.BaseClasses.Move import Move

class Kangaskhan(Normal):
    def __init__(self):
        moves = [
            Move("Fake Out", "NORMAL", 40),
            Move("Body Slam", "NORMAL", 85),
            Move("Crunch", "DARK", 80),
            Move("Power up Punch", "FIGHTING", 40)
        ]
        super().__init__("Kangaskhan", 140, moves, "./TVPoke/Pokemon/imgs/Kangaskhan.png")