class Pokemon:
    def __init__(self, name, hp, type, critType, moves, imgPath):
        self.name = name
        self.hp = hp
        self.type = type
        self.critType = critType
        self.moves = moves
        self.img = imgPath

        self.stats = {
        "healthPoints" : None,
        "attack" : None,
        "defense" : None,
        "specialAttack" : None,
        "specialDefense" : None,
        "speed" : None
        }

    def takeDamage(self, move, attacker):
        totalDamage = 0
        multi = 1
        if move.type == self.critType:
            multi = 2
        
        if move.damageCategory == "physical":
            attack = attacker.stats["attack"] * attacker.statBuffs["attack"]
            defense = self.stats["defense"] * self.statBuffs["defense"]
        else:
            attack = attacker.stats["specialAttack"] * attacker.statBuffs["specialAttack"]
            defense = self.stats["specialDefense"] * self.statBuffs["specialDefense"]

        totalDamage = ((0.5 * move.power * ((attack)/(defense))) + 1) * multi

        self.hp -= totalDamage