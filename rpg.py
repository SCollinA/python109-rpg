"""
In this simple RPG game, the hero fights the goblin. He has the options to:
1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee
"""
class Hero:
    def __init__(self, health, power):
        self.health = health
        self.power = power

class Goblin:
    def __init__(self, health, power):
        self.health = health
        self.power = power

def main():
    hero = Hero(10, 5)
    # hero_health = 10
    # hero_power = 5
    goblin = Goblin(6, 2)
    # goblin_health = 6
    # goblin_power = 2
    while goblin.health > 0 and hero.health > 0:
    # while goblin_health > 0 and hero_health > 0:
        print("You have %d health and %d power." % (hero.health, hero.power))
        # print("You have %d health and %d power." % (hero_health, hero_power))
        print("The goblin has %d health and %d power." % (goblin.health, goblin.power))
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
            goblin.health -= hero.power
            # goblin_health -= hero_power
            print("You do %d damage to the goblin." % hero.power)
            # print("You do %d damage to the goblin." % hero_power)
            if goblin.health <= 0:
            # if goblin_health <= 0:
                print("The goblin is dead.")
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
            hero.health -= goblin.power
            # hero_health -= goblin_power
            print("The goblin does %d damage to you." % goblin.power)
            # print("The goblin does %d damage to you." % goblin_power)
            if hero.health <= 0:
            # if hero_health <= 0:
                print("You are dead.")
main()