class Entity:
    def __init__(self, id, name, hp, ac):
        self.id = id
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.ac = ac
        self.status = []