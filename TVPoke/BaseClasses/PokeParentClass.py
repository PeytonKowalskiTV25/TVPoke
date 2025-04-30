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
            if random.random() < 0.5:
                print(f"{self.name} hurt itself in confusion!")
                attack = self.stats["attack"] * self.statBuffs["attack"]
                defense = max(self.stats["defense"] * stage_to_multiplier(self.statBuffs["defense"]), 1)  # Ensure defense is at least 1
                damage = ((0.5 * 40 * (attack / defense)) + 1)
                self.hp -= damage
                print(f"{self.name} took {damage:.1f} damage!")
            else:
                print(f"{self.name} snapped out of confusion and attacked successfully!")
                self.confusion["turnsLeft"] -= 1  # Decrement only if no self-damage

            if self.confusion["turnsLeft"] <= 0:
                self.confusion["isConfused"] = False
                print(f"{self.name} is no longer confused!")

    def inflictBurn(self):
        if not self.burn["isBurned"]:  # Prevent duplicate burns
            self.burn["isBurned"] = True
            self.burn["turnsLeft"] = random.randint(3, 5)
            self.statBuffs["attack"] *= 0.5  # Apply attack reduction once
            print(f"{self.name} is burned!")

    def resolveBurn(self):
        if self.burn["isBurned"]:
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

        if move.damageCategory == "Physical":
            attack = attacker.stats["attack"] * stage_to_multiplier(attacker.statBuffs["attack"])
            defense = self.stats["defense"] * stage_to_multiplier(self.statBuffs["defense"])
            print(self.stats["attack"])
            print(stage_to_multiplier(attacker.statBuffs["attack"]))
            totalDamage = round(((0.5 * move.power * (attack / defense)) + 1) * multi)
            print(f"0.5 * {move.power} * ({attack} / {defense})) + 1) * {multi})")
        else:
            attack = attacker.stats["specialAttack"] * stage_to_multiplier(attacker.statBuffs["specialAttack"])
            defense = self.stats["specialDefense"] * stage_to_multiplier(self.statBuffs["specialDefense"])
            totalDamage = round(((0.5 * move.power * (attack / defense)) + 1) * multi)
            print(f"0.5 * {move.power} * ({attack} / {defense})) + 1) * {multi})")

        self.hp -= totalDamage
        print(f"{self.name} took {totalDamage} damage")
        print(f"attack:{attack}; defense:{defense}")

def stage_to_multiplier(stage):
    if stage >= 0:
        return (2 + stage) / 2  # Positive stages: 1.5x for +1, 2.0x for +2, etc.
    else:
        return 2 / (2 - stage)  # Negative stages: 0.67x for -1, 0.5x for -2, etc.
