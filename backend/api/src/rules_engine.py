import random

class RulesEngine:

    def roll_d20(self):
        return random.randint(1, 20)

    def roll_damage(self, expr="1d6"):
        import re

        match = re.match(r"(\d+)d(\d+)", expr)
        n, sides = int(match.group(1)), int(match.group(2))

        return sum(random.randint(1, sides) for _ in range(n))

    def attack(self, attacker, target):
        roll = self.roll_d20()

        hit = roll >= target["ac"]

        damage = self.roll_damage("1d6") if hit else 0

        return {
            "roll": roll,
            "hit": hit,
            "damage": damage
        }