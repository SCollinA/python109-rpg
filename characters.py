from random import random

class Character:
    def __init__(self):
        self.name = ''
        self.health = 6
        self.power = 2
        self.armor = 0
        self.evade = 0
        self.coins = 5
    def alive(self):
        return self.health > 0
    def attack(self, enemy):
        attack_power = self.power
        enemy.defend(attack_power)
        if not enemy.alive():
            print("The %s is dead." % enemy.name)
    def defend(self, enemy, attack_power):
        self.health -= attack_power
        print("The %s does %d damage to the %s." % (enemy.name, attack_power, self.name))
    def print_status(self):
        print("The %s has %d health and %d power." % (self.name, self.health, self.power))

class Enemy(Character):
    def is_friend(self):
        return False

class Friend(Character):
    def is_friend(self):
        return True

class Hero(Friend):
    def __init__(self, name):
        super.__init__()
        self.name = name
        self.health = 10
        self.power = 5
        self.coins = 20
        self.knapsack = []
    # make the hero generate double damage points during an attack with a probabilty of 20%
    def attack(self, enemy):
        if random() > 0.8:
            attack_power = self.power * 2
        else:
            attack_power = self.power
        enemy.defend(self, attack_power)
        if not enemy.alive():
            print("The %s is dead." % enemy.name)

    def defend(self, enemy, attack_power):
        attack_power -= self.armor
        evade_probability = 1 - (1 / (1 + self.evade))
        if random() > evade_probability:
            attack_power = 0
        self.health -= attack_power
        print("The %s does %d damage to the %s." % (enemy.name, attack_power, self.name))
    
    def buy(self, item):
        self.coins -= item.cost
        self.knapsack.append(item)

    # def sell(self, item):
    #     self.coins += item.cost
    #     self.knapsack.remove(item)


class HumanShield(Friend):
    def __init__(self, name):
        super.__init__()
        self.name = name
        self.health = 20
        self.power = 1

# make a new character called Medic that can sometimes recuperate 2 health points 
# after being attacked with a probability of 20%
class Medic(Friend):
    def __init__(self, name):
        super.__init__()
        self.name = name
    def defend(self, enemy, attack_power):
        self.health -= attack_power
        if random() > .8:
            self.heal(self)
        print("The %s does %d damage to the %s." % (enemy.name, attack_power, self.name))
    def heal(self, target):
        target.health += 2

class Goblin(Enemy):
    def attack(self, enemy):
        if self.steal():
            enemy.coins -= 5
            self.coins += 5
        enemy.defend(self, self.power)
        if not enemy.alive():
            print("The %s is dead." % enemy.name)
    def steal(self):
        return random() > .5

class Wizard(Enemy):
    def __init__(self, name):
        super.__init__()
        self.name = name
        self.coins = 8
    def attack(self, enemy):
        # 10% of time Wizard attack is devastating
        if self.cast_spell():
            enemy.health -= self.power * 3
    def cast_spell(self):
        return random() > .9

# make a Zombie character that doesn't die even if his health is below zero
class Zombie(Enemy):
    def __init__(self, name):
        super.__init__()
        self.name = name
        self.health = 4
        self.power = 1
        self.coins = 10000
    def alive(self):
        if self.health < 4:
            self.eat_brains()
        return True
    def eat_brains(self):
        print("brains...")
        self.health = 4

# make a character called Shadow who has only 1 starting health 
# but will only take damage about once out of every ten times he is attacked.
class Shadow(Enemy):
    def __init__(self, name):
        super.__init__()
        self.name = name
        self.health = 1
        self.coins = 2
    def defend(self, enemy, attack_power):
        if random() > .1:
            attack_power = 0
        self.health -= attack_power
        print("The %s does %d damage to the %s." % (enemy.name, attack_power, self.name))
