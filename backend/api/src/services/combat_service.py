from src.rules_engine import RulesEngine
from src.combat_engine import CombatEngine
from src.status_engine import StatusEngine


class CombatService:

    def __init__(self):
        self.rules = RulesEngine()
        self.combat = CombatEngine()
        self.status = StatusEngine()

    async def handle(self, room, msg, user, roll_dice):

        combat = room.state["combat"]

        # -------------------------
        # COMBAT START
        # -------------------------
        if msg["type"] == "combat_start":
            self.combat.start_combat(room)

            return {"type": "combat_started"}

        # -------------------------
        # INITIATIVE
        # -------------------------
        if msg["type"] == "initiative":
            result = await roll_dice("1d20")

            combat["initiative"].append({
                "user_id": user["id"],
                "name": user["name"],
                "roll": result["result"]
            })

            return {"type": "initiative_added", "result": result}

        # -------------------------
        # ATTACK
        # -------------------------
        if msg["type"] == "attack":
            attacker = combat["entities"][user["id"]]
            target = combat["entities"][msg["target"]]

            hit = self.rules.roll_hit(msg["attack_roll"], target.ac)

            damage = 0

            if hit:
                damage = msg["damage"]
                self.rules.apply_damage(target, damage)

            return {
                "type": "attack_result",
                "hit": hit,
                "damage": damage
            }

        # -------------------------
        # NEXT TURN
        # -------------------------
        if msg["type"] == "next_turn":
            self.combat.next_turn(room)

            return {"type": "turn_changed"}

        return None