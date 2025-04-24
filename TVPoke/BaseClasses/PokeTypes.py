from TVPoke.BaseClasses.PokeParentClass import Pokemon

class Water(Pokemon):
    def __init__(self, name, hp, moves, imgPath, stats, statBuffs):
        super().__init__(name, hp, "WATER", "ELECTRIC", moves, imgPath, stats, statBuffs)

class Ground(Pokemon):
    def __init__(self, name, hp, moves, imgPath, stats, statBuffs):
        super().__init__(name, hp, "GROUND", "GRASS", moves, imgPath, stats, statBuffs)

class Grass(Pokemon):
    def __init__(self, name, hp, moves, imgPath, stats, statBuffs):
        super().__init__(name, hp, "GRASS", "FIRE", moves, imgPath, stats, statBuffs)

class Fire(Pokemon):
    def __init__(self, name, hp, moves, imgPath, stats, statBuffs):
        super().__init__(name, hp, "FIRE", "WATER", moves, imgPath, stats, statBuffs)

class Electric(Pokemon):
    def __init__(self, name, hp, moves, imgPath, stats, statBuffs):
        super().__init__(name, hp, "ELECTRIC", "GROUND", moves, imgPath, stats, statBuffs)

class Normal(Pokemon):
    def __init__(self, name, hp, moves, imgPath, stats, statBuffs):
        super().__init__(name, hp, "NORMAL", "FIGHTING", moves, imgPath, stats, statBuffs)

class Fighting(Pokemon):
    def __init__(self, name, hp, moves, imgPath, stats, statBuffs):
        super().__init__(name, hp, "FIGHTING", "PSYCHIC", moves, imgPath, stats, statBuffs)

class Fairy(Pokemon):
    def __init__(self, name, hp, moves, imgPath, stats, statBuffs):
        super().__init__(name, hp, "FAIRY", "POISON", moves, imgPath, stats, statBuffs)

class Poison(Pokemon):
    def __init__(self, name, hp, moves, imgPath, stats, statBuffs):
        super().__init__(name, hp, "POISON", "GROUND", moves, imgPath, stats, statBuffs)

class Psychic(Pokemon):
    def __init__(self, name, hp, moves, imgPath, stats, statBuffs):
        super().__init__(name, hp, "PSYCHIC", "GHOST", moves, imgPath, stats, statBuffs)

class Dragon(Pokemon):
    def __init__(self, name, hp, moves, imgPath, stats, statBuffs):
        super().__init__(name, hp, "DRAGON", "DRAGON", moves, imgPath, stats, statBuffs)

class Ice(Pokemon):
    def __init__(self, name, hp, moves, imgPath, stats, statBuffs):
        super().__init__(name, hp, "ICE", "ROCK", moves, imgPath, stats, statBuffs)

class Rock(Pokemon):
    def __init__(self, name, hp, moves, imgPath, stats, statBuffs):
        super().__init__(name, hp, "ROCK", "STEEL", moves, imgPath, stats, statBuffs)

class Steel(Pokemon):
    def __init__(self, name, hp, moves, imgPath, stats, statBuffs):
        super().__init__(name, hp, "STEEL", "FIRE", moves, imgPath, stats, statBuffs)

class Flying(Pokemon):
    def __init__(self, name, hp, moves, imgPath, stats, statBuffs):
        super().__init__(name, hp, "FLYING", "ELECTRIC", moves, imgPath, stats, statBuffs)

class Ghost(Pokemon):
    def __init__(self, name, hp, moves, imgPath, stats, statBuffs):
        super().__init__(name, hp, "GHOST", "DARK", moves, imgPath, stats, statBuffs)

class Bug(Pokemon):
    def __init__(self, name, hp, moves, imgPath, stats, statBuffs):
        super().__init__(name, hp, "BUG", "FLYING", moves, imgPath, stats, statBuffs)

class Dark(Pokemon):
    def __init__(self, name, hp, moves, imgPath, stats, statBuffs):
        super().__init__(name, hp, "DARK", "GHOST", moves, imgPath, stats, statBuffs)

