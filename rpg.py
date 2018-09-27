"""
In this simple RPG game, the hero fights the goblin. He has the options to:
1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee
"""
from time import sleep
from random import random

class Character:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power
    def alive(self):
        return self.health > 0
    def attack(self, enemy):
        enemy.health -= self.power
        print("The %s does %d damage to the %s." % (self.name, self.power, enemy.name))
        if not enemy.alive():
            print("The %s is dead." % enemy.name)
    def print_status(self):
        print("The %s has %d health and %d power." % (self.name, self.health, self.power))

class Hero(Character):
    def __init__(self, name):
        self.name = name
        self.health = 10
        self.power = 5
    # make the hero generate double damage points during an attack with a probabilty of 20%
    def attack(self, enemy):
        if random() > 0.8:
            enemy.health -= self.power * 2
        else:
            enemy.health -= self.power
        print("The %s does %d damage to the %s." % (self.name, self.power, enemy.name))

class Goblin(Character):
    def __init__(self, name):
        self.name = name
        self.health = 6
        self.power = 2

class Wizard(Character):
    def __init__(self, name):
        self.name = name
        self.health = 6
        self.power = 2
    def attack(self, enemy):
        # 10% of time Wizard attack is devastating
        if random() > .9:
            enemy.health -= self.power * 3
        else:
            enemy.health -= self.power

# make a Zombie character that doesn't die even if his health is below zero
class Zombie(Character):
    def __init__(self, name):
        self.name = name
        self.health = 4
        self.power = 1
    def alive(self):
        if self.health < 4:
            self.eat_brains()
        return True
    def eat_brains(self):
        print("brains...")
        self.health = 4

# make a new character called Medic that can sometimes recuperate 2 health points 
# after being attacked with a probability of 20%
class Medic(Character):
    def __init__(self, name):
        self.name = name
        self.health = 10
        self.power = 5
    def alive(self):
        if random() > .8:
            self.recuperate()
        return self.health > 0
    def recuperate(self):
        self.health += 2

# make a character called Shadow who has only 1 starting health 
# but will only take damage about once out of every ten times he is attacked.
class Shadow(Character):
    def __init__(self, name):
        self.name = name
        self.health = 1
        self.power = 2
    def alive(self):
        if random() > .1:
            self.health = 1
        return self.health > 0

class HumanShield(Character):
    def __init__(self, name):
        self.name = name
        self.health = 20
        self.power = 1


def main():
    hero = Hero("Hero")
    goblin = Goblin("Goblin")
    while goblin.alive() and hero.alive():
        hero.print_status()
        goblin.print_status()
        print()
        print("What do you want to do?")
        print("1. fight %s" % goblin.name)
        print("2. do nothing")
        print("3. flee")
        print("> ", end="")
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
        if goblin.alive():
            # Goblin attacks hero
            goblin.attack(hero)
    if hero.alive():
        zombie = Zombie("Zombie")
        while zombie.alive() and hero.alive():
            hero.print_status()
            zombie.print_status()
            print()
            print("What do you want to do?")
            print("1. fight %s" % zombie.name)
            print("2. do nothing")
            print("3. flee")
            print("> ", end="")
            user_input = input()
            if user_input == "1":
                # Hero attacks goblin
                hero.attack(zombie)
            elif user_input == "2":
                pass
            elif user_input == "3":
                print("Goodbye.")
                break
            else:
                print("Invalid input %r" % user_input)
            if zombie.alive():
                # Goblin attacks hero
                zombie.attack(hero)
main()