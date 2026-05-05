class CombatSystem:
    def __init__(self, room):
        self.room = room

    # -------------------------
    # INITIATIVE
    # -------------------------
    def add_initiative(self, user_id, name, roll):
        self.room.state["combat"]["initiative"].append({
            "user_id": user_id,
            "name": name,
            "roll": roll
        })

    def start_combat(self):
        combat = self.room.state["combat"]

        combat["active"] = True
        combat["round"] = 1
        combat["turn_index"] = 0

        # ordena iniciativa (desc)
        combat["initiative"].sort(key=lambda x: x["roll"], reverse=True)

        combat["current_turn_user_id"] = combat["initiative"][0]["user_id"]

    # -------------------------
    # TURN SYSTEM
    # -------------------------
    def next_turn(self):
        combat = self.room.state["combat"]

        if not combat["active"]:
            return

        combat["turn_index"] += 1

        if combat["turn_index"] >= len(combat["initiative"]):
            combat["turn_index"] = 0
            combat["round"] += 1

        combat["current_turn_user_id"] = combat["initiative"][combat["turn_index"]]["user_id"]

    def get_current_turn(self):
        combat = self.room.state["combat"]
        return combat["current_turn_user_id"]
