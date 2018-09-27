# Store items
class StoreItem:
    pass

class SuperTonic(StoreItem):
    def __init__(self):
        self.health_restore = 10
        self.cost = 5

class Armor(StoreItem):
    def __init__(self):
        self.armor_strength = 2
        self.cost = 5

class Evade(StoreItem):
    def __init__(self):
        self.evade_points = 2
        self.cost = 5

class Hyper(StoreItem):
    def __init__(self):
        self.turns = 1
        self.cost = 5

class Strong(StoreItem):
    def __init__(self):
        self.attack_boost = 2
        self.cost = 5

class Store:
    def __init__(self):
        self.items = [SuperTonic(), Armor(), Evade(), Hyper(), Strong()]
