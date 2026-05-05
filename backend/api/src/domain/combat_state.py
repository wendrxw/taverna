class CombatState:
    def __init__(self):
        self.active = False
        self.round = 0
        self.turn_index = 0
        self.initiative = []
        self.entities = {}
        self.current_turn_user_id = None