from TVPoke.BaseClasses.PokeParentClass import Pokemon

class Water(Pokemon):
    def __init__(self, name, hp, moves, imgPath, stats):
        super().__init__(name, hp, "WATER", "ELECTRIC", moves, imgPath, stats)

class Ground(Pokemon):
    def __init__(self, name, hp, moves, imgPath, stats):
        super().__init__(name, hp, "GROUND", "GRASS", moves, imgPath, stats)

class Grass(Pokemon):
    def __init__(self, name, hp, moves, imgPath, stats):
        super().__init__(name, hp, "GRASS", "FIRE", moves, imgPath, stats)

class Fire(Pokemon):
    def __init__(self, name, hp, moves, imgPath, stats):
        super().__init__(name, hp, "FIRE", "WATER", moves, imgPath, stats)

class Electric(Pokemon):
    def __init__(self, name, hp, moves, imgPath, stats):
        super().__init__(name, hp, "ELECTRIC", "GROUND", moves, imgPath, stats)

class Normal(Pokemon):
    def __init__(self, name, hp, moves, imgPath, stats):
        super().__init__(name, hp, "NORMAL", "FIGHTING", moves, imgPath, stats)

class Fighting(Pokemon):
    def __init__(self, name, hp, moves, imgPath, stats):
        super().__init__(name, hp, "FIGHTING", "PSYCHIC", moves, imgPath, stats)

class Fairy(Pokemon):
    def __init__(self, name, hp, moves, imgPath, stats):
        super().__init__(name, hp, "FAIRY", "POISON", moves, imgPath, stats)

class Poison(Pokemon):
    def __init__(self, name, hp, moves, imgPath, stats):
        super().__init__(name, hp, "POISON", "GROUND", moves, imgPath, stats)

class Psychic(Pokemon):
    def __init__(self, name, hp, moves, imgPath, stats):
        super().__init__(name, hp, "PSYCHIC", "GHOST", moves, imgPath, stats)

class Dragon(Pokemon):
    def __init__(self, name, hp, moves, imgPath, stats):
        super().__init__(name, hp, "DRAGON", "DRAGON", moves, imgPath, stats)

class Ice(Pokemon):
    def __init__(self, name, hp, moves, imgPath, stats):
        super().__init__(name, hp, "ICE", "ROCK", moves, imgPath, stats)

class Rock(Pokemon):
    def __init__(self, name, hp, moves, imgPath, stats):
        super().__init__(name, hp, "ROCK", "STEEL", moves, imgPath, stats)
        
class Steel(Pokemon):
    def __init__(self, name, hp, moves, imgPath, stats):
        super().__init__(name, hp, "STEEL", "FIRE", moves, imgPath, stats)

class Flying(Pokemon):
    def __init__(self, name, hp, moves, imgPath, stats):
        super().__init__(name, hp, "FLYING", "ELECTRIC", moves, imgPath, stats)

class Ghost(Pokemon):
    def __init__(self, name, hp, moves, imgPath, stats):
        super().__init__(name, hp, "GHOST", "DARK", moves, imgPath, stats)

class Bug(Pokemon):
    def __init__(self, name, hp, moves, imgPath, stats):
        super().__init__(name, hp, "BUG", "FLYING", moves, imgPath, stats)

class Dark(Pokemon):
    def __init__(self, name, hp, moves, imgPath, stats):
        super().__init__(name, hp, "DARK", "GHOST", moves, imgPath, stats)

