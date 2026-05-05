from collections import defaultdict
from src.models import Event
from src.default_state import initial_state


class Room:
    def __init__(self, room_id: str):
        self.room_id = room_id
        self.users = {}        # user_id -> user
        self.events = []       # event log
        self.state = initial_state()

    def initial_state():
        return {
            "players": {},
            "combat": {
                "active": False,
                "round": 0,
                "turn_index": 0,
                "initiative": [],
                "current_turn_user_id": None
            }
        }

    def create_entity(name: str, hp: int, ac: int):
        return {
            "name": name,
            "hp": hp,
            "max_hp": hp,
            "ac": ac,
            "status": []
        }
    
    def apply_damage(self, target_id: str, damage: int):
        entity = self.room.state["combat"]["entities"].get(target_id)

        if not entity:
            return

        entity["hp"] -= damage

        if entity["hp"] <= 0:
            entity["hp"] = 0
            entity["status"].append("dead")

            self.room.add_event(Event(
                type="entity_down",
                user=None,
                data={"target": target_id}
            ))

    # -------------------------
    # EVENT STORE
    # -------------------------
    def add_event(self, event: Event):
        self.events.append(event)
        self.apply(event)

    # -------------------------
    # STATE REDUCER
    # -------------------------
    def apply(self, event: Event):
        if event.type == "user_joined":
            self.state.setdefault("last_events", []).append(event.data)

        elif event.type == "roll":
            self.state.setdefault("last_rolls", []).append(event.data)

        elif event.type == "initiative":
            self.state["initiative"].append(event.data)

        elif event.type == "combat_start":
            self.state["combat"] = True

    async def attack(self, attacker_id: str, target_id: str, attack_roll: int, damage: int):
        target = self.room.state["combat"]["entities"][target_id]
        hit = attack_roll >= target["ac"]

        if hit:
            self.apply_damage(target_id, damage)

        self.room.add_event(Event(
            type="attack",
            user=attacker_id,
            data={
                "target": target_id,
                "hit": hit,
                "damage": damage if hit else 0
            }
        ))

    def rebuild_state(self):
        self.state = initial_state()

        for event in self.events:
            self.apply(event)