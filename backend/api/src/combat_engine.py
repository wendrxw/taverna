class CombatEngine:

    def can_start_combat(self, room):
        return len(room.state["combat"]["initiative"]) > 0

    def start_combat(self, room):
        combat = room.state["combat"]

        if len(combat["initiative"]) == 0:
            return False

        combat["active"] = True
        combat["round"] = 1
        combat["turn_index"] = 0

        combat["initiative"].sort(key=lambda x: x["roll"], reverse=True)

        combat["current_turn_user_id"] = combat["initiative"][0]["user_id"]

        return True
    
    def apply_status_effects(self, room):
        for entry in room.state["combat"]["initiative"]:
            player = room.state["players"].get(entry["user_id"])

            if not player:
                continue

            if "poisoned" in player.get("status", []):
                player["hp"] -= 2

            if player["hp"] <= 0:
                player["hp"] = 0
                if "dead" not in player["status"]:
                    player["status"].append("dead")

    def check_death(self, room):
        combat = room.state["combat"]

        combat["initiative"] = [
            e for e in combat["initiative"]
            if room.state["players"][e["user_id"]]["hp"] > 0
        ]

    def next_turn(self, room):
        self.apply_status_effects(room)
        self.advance_turn(room)
        self.check_death(room)
        self.trigger_reactions(room)

    def advance_turn(self, room):
        combat = room.state["combat"]

        if not combat["initiative"]:
            return

        combat["turn_index"] += 1

        if combat["turn_index"] >= len(combat["initiative"]):
            combat["turn_index"] = 0
            combat["round"] += 1

        current = combat["initiative"][combat["turn_index"]]
        combat["current_turn_user_id"] = current["user_id"]

    def trigger_reactions(self, room):
        # futuro: opportunity attacks, legendary actions etc
        pass