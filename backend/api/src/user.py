class User:
    def __init__(self, user_id: str, name: str, websocket):
        self.user_id = user_id
        self.name = name
        self.websocket = websocket