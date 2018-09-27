"""
In this simple RPG game, the hero fights the goblin. He has the options to:
1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee
"""
from time import sleep
from random import random, choice
from characters import *
from party import *
from battle import *
from store import *

battle_engine = Battle()
shopping_engine = Store()
print("Welcome to another land. What is your name?")
user_name = input("> ")
user_hero = Hero(user_name)
medic = Medic("medic")
brock = HumanShield("brock")
hero_party = Party([user_hero, medic, brock])
enemies = [Goblin, Wizard, Zombie, Shadow]

while Battle.battles_remaining > 0:
    enemy_party = []
    while len(enemy_party) < 3:
        enemy_party.append(choice(enemies)())
    if not battle_engine.do_battle(hero_party, enemy_party):
        print("Game Over...")
        break

print("You Win!")