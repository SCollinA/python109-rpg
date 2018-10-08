# Store items
class StoreItem:
    pass

class SuperTonic(StoreItem):
    name = "SuperTonic"
    cost = 5
    def apply(self, target):
        target.health += 10
        print("%s's health increased by 10." % (target.name))

class Sword(StoreItem):
    name = "Sword"
    cost = 5
    def apply(self, target):
        target.power += 2
        print("%s's power increased by 2." % (target.name))

class Armor(StoreItem):
    name = "Armor"
    cost = 5
    def apply(self, target):
        target.armor += 2
        print("%s's armor increased by 2." % (target.name))


class Evade(StoreItem):
    name = "Evade"
    cost = 5
    def apply(self, target):
        target.evade += 2
        print("%s's evade increased by 2." % (target.name))

class Swap(StoreItem):
    name = "Swap"
    cost = 5
    def apply(self, target):
        pass

# class Hyper(StoreItem):
#     def __init__(self):
#         self.turns = 1
#         self.cost = 5

class Store:
    def __init__(self):
        self.items = [SuperTonic, Sword, Armor, Evade]
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
            print("%d. leave" % (len(self.items) + 1))
            user_input = int(input("> "))
            if user_input == len(self.items) + 1:
                break
            else:
                ItemToBuy = self.items[user_input - 1]
                item = ItemToBuy()
            hero.buy(item)
            print("%s bought a %s" % (hero.name, item.name))