import uuid
from fastapi import WebSocket
from collections import defaultdict
from .user import User


class ConnectionManager:
    def __init__(self):
        self.rooms = {}

    def add(self, room_id, user):
        self.rooms.setdefault(room_id, {})[user["id"]] = user

    def remove(self, room_id, user_id):
        if room_id in self.rooms:
            self.rooms[room_id].pop(user_id, None)

    async def broadcast(self, room_id, message):
        for user in self.rooms.get(room_id, {}).values():
            await user["ws"].send_json(message)