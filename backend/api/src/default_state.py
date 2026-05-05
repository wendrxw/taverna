def initial_state():
    return {
        "players": {},
        "monsters": {},
        "combat": {
            "active": False,
            "round": 0,
            "turn_index": 0,
            "initiative": [],
            "current_turn_user_id": None
        }
    }