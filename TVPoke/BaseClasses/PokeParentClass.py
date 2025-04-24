import random

class Pokemon:
    def __init__(self, name, hp, type, critType, moves, imgPath, stats, statBuffs):
        self.name = name
        self.hp = hp
        self.type = type
        self.critType = critType
        self.moves = moves
        self.img = imgPath
        self.stats = stats
        self.statBuffs = statBuffs

        self.confusion = {
            "isConfused": False,
            "turnsLeft": 0
        }
        self.burn = {
            "isBurned": False,
            "turnsLeft": 0
        }

    def inflictConfusion(self):
        self.confusion["isConfused"] = True
        self.confusion["turnsLeft"] = random.randint(1, 4)  # Confusion lasts 1-4 turns

    def resolveConfusion(self):
        if self.confusion["isConfused"]:
            # 50% chance to hurt itself
            if random.random() < 0.5:
                print(f"{self.name} hurt itself in confusion!")
                # Calculate self-damage as if using a 40-power physical move
                attack = self.stats["attack"] * self.statBuffs["attack"]
                defense = self.stats["defense"] * self.statBuffs["defense"]
                damage = ((0.5 * 40 * (attack / defense)) + 1)
                self.hp -= damage
                print(f"{self.name} took {damage:.1f} damage!")
            else:
                print(f"{self.name} snapped out of confusion and attacked successfully!")

            # Decrease confusion duration
            self.confusion["turnsLeft"] -= 1
            if self.confusion["turnsLeft"] <= 0:
                self.confusion["isConfused"] = False
                print(f"{self.name} is no longer confused!")

    def inflictBurn(self):
        self.burn["isBurned"] = True
        self.burn["turnsLeft"] = random.randint(3, 5)  # Burn lasts 3-5 turns
        print(f"{self.name} is burned!")

    def resolveBurn(self):
        if self.burn["isBurned"]:
            # Reduce attack stat by 50% (multiplier = 0.5)
            self.statBuffs["attack"] *= 0.5

            # Take burn damage (1/16th of max HP)
            burnDamage = self.stats["healthPoints"] // 16
            self.hp -= burnDamage
            print(f"{self.name} took {burnDamage} damage from its burn!")

            # Decrease burn duration
            self.burn["turnsLeft"] -= 1
            if self.burn["turnsLeft"] <= 0:
                self.burn["isBurned"] = False
                print(f"{self.name}'s burn has healed!")

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
    