# Store items
class StoreItem:
    pass

class SuperTonic(StoreItem):
    def __init__(self):
        self.name = "SuperTonic"
        self.cost = 5
    def apply(self, target):
        target.health += 10
        print("%s's health increased to %d." % (target.name, target.health))

class Sword(StoreItem):
    def __init__(self):
        self.name = "Sword"
        self.cost = 5
    def apply(self, target):
        target.power += 2
        print("%s's power increased to %d." % (target.name, target.power))

class Armor(StoreItem):
    def __init__(self):
        self.name = "Armor"
        self.cost = 5
    def apply(self, target):
        target.armor += 2
        print("%s's power increased to %d." % (target.name, target.armor))


class Evade(StoreItem):
    def __init__(self):
        self.name = "Evade"
        self.cost = 5
    def apply(self, target):
        target.evade += 2
        print("%s's evade increased to %d." % (target.name, target.evade))

class Swap(StoreItem):
    def apply(self, target):
        pass

# class Hyper(StoreItem):
#     def __init__(self):
#         self.turns = 1
#         self.cost = 5

class Store:
    def __init__(self):
        self.items = [SuperTonic, Sword, Armor, Evade, Swap]
    def go_shopping(self, hero):
        while True:
            print("=====================")
            print("Welcome to the store!")
            print("=====================")
            print("You have %d coins." % hero.coins)
            print("What do you want to do?")
            for i in range(len(self.items)):
                item = self.items[i]
                print("%d. buy %s (%d)" % (i + 1, item.name, item.cost))
                print("%d. leave" % len(self.items))
            user_input = int(input("> "))
            if user_input == len(self.items):
                break
            else:
                ItemToBuy = self.items[user_input - 1]
                item = ItemToBuy()
            hero.buy(item)