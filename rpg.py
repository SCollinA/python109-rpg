"""
In this simple RPG game, the hero fights the goblin. He has the options to:
1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee
"""
from time import sleep
from random import random
from characters import *

# parties
class Party:
    def __init__(self):
        self.party = []

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