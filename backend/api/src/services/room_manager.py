from collections import defaultdict
from src.room import Room


class RoomManager:
    def __init__(self):
        self.rooms: dict[str, Room] = {}

    def get(self, room_id: str) -> Room:
        if room_id not in self.rooms:
            self.rooms[room_id] = Room(room_id)
        return self.rooms[room_id]