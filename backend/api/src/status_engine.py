class StatusEngine:

    def apply_turn_effects(self, entity):

        statuses = entity.get("statuses", {})

        for name, effect in list(statuses.items()):

            if name == "poisoned":
                entity["hp"] -= effect.get("damage", 2)

            effect["duration"] -= 1

            if effect["duration"] <= 0:
                del statuses[name]

        if entity["hp"] <= 0:
            entity["hp"] = 0
            statuses["dead"] = {"duration": None}