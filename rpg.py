"""
In this simple RPG game, the hero fights the goblin. He has the options to:
1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee
"""
class Character:
    def alive(self):
        if self.health > 0:
            return True
    def attack(self, enemy):
        enemy.health -= self.power
        # goblin.health -= hero.power
        # goblin_health -= hero_power
        print("The %s does %d damage to the %s." % (self.name, self.power, enemy.name))
        # print("You do %d damage to the goblin." % hero.power)
        # print("You do %d damage to the goblin." % hero_power)
        if enemy.health <= 0:
        # if goblin.health <= 0:
        # if goblin_health <= 0:
            print("The %s is dead." % enemy.name)
            # print("The goblin is dead.")
    def print_status(self):
        print("The %s have %d health and %d power." % (self.name self.health, self.power))
        # print("You have %d health and %d power." % (hero.health, hero.power))

class Hero(Character):
    def __init__(self, name):
        self.name = name
        self.health = 10
        self.power = 5

class Goblin(Character):
    def __init__(self, name):
        self.name = name
        self.health = 6
        self.power = 2

def main():
    hero = Hero("Hero")
    # hero_health = 10
    # hero_power = 5
    goblin = Goblin("Goblin")
    # goblin_health = 6
    # goblin_power = 2
    while goblin.alive() and hero.alive():
    # while goblin.health > 0 and hero.health > 0:
    # while goblin_health > 0 and hero_health > 0:
        hero.print_status()
        # print("You have %d health and %d power." % (hero.health, hero.power))
        # print("You have %d health and %d power." % (hero_health, hero_power))
        goblin.print_status()
        # print("The goblin has %d health and %d power." % (goblin.health, goblin.power))
        # print("The goblin has %d health and %d power." % (goblin_health, goblin_power))
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ",)
        user_input = input()
        if user_input == "1":
            # Hero attacks goblin
            hero.attack(goblin)
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input %r" % user_input)
        if goblin.health > 0:
        # if goblin_health > 0:
            # Goblin attacks hero
            goblin.attack(hero)
main()