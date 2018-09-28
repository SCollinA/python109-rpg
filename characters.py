from random import random, randint

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
        enemy.defend(self, attack_power)
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
    def choose_target(self, hero_party):
        alive_friends = []
        for friend in hero_party.party:
            if friend.alive():
                alive_friends.append(friend)
        return alive_friends[randint(0, len(alive_friends) - 1)]

class Friend(Character):
    # only friends have knapsack that they share
    knapsack = []
    def is_friend(self):
        return True
    def choose_target(self, hero_party, enemy_party):
        targets = hero_party.party + enemy_party.party
        for target in targets:
            if not target.alive():
                targets.remove(target)
        while True:
            print("Choose a target.")
            for i in range(len(targets)):
                print("%d. %s" % (i + 1, targets[i].name))
            user_input = input("> ")
            try:
                choice = int(user_input)
                return targets[choice - 1]
            except:
                pass
            
    def choose_action(self):
        while True:
            print("What do you want to do?")
            print("1. attack")
            print("2. use item")
            print("3. do nothing")
            print("4. flee")
            print("> ", end="")
            user_input = input()
            valid_input = ['1', '2', '3', '4']
            if user_input in valid_input:
                return user_input
            else:
                print("Invalid input %r" % user_input)
    def choose_item(self):
        while True:
            print("Which item would you like to use?")
            for i in range(len(Friend.knapsack)):
                print("%d. %s" % (i + 1, Friend.knapsack[i]))
            user_input = input("> ")
            try:
                choice = int(user_input)
            except:
                pass
            if choice > 0 and choice < len(Friend.knapsack):
                return Friend.knapsack[choice - 1]
    def use_item(self, item, target):
        item.apply(target)


class Hero(Friend):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.health = 10
        self.power = 5
        self.coins = 20
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
    def __init__(self):
        super().__init__()
        self.name = "Brock"
        self.health = 20
        self.power = 1

# make a new character called Medic that can sometimes recuperate 2 health points 
# after being attacked with a probability of 20%
class Medic(Friend):
    def __init__(self):
        super().__init__()
        self.name = "Medic"
    def defend(self, enemy, attack_power):
        self.health -= attack_power
        if random() > .8:
            self.heal(self)
        print("The %s does %d damage to the %s." % (enemy.name, attack_power, self.name))
    def heal(self, target):
        target.health += 2

class Goblin(Enemy):
    def __init__(self):
        super().__init__()
        self.name = "Goblin"
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
    def __init__(self):
        super().__init__()
        self.name = "Wizard"
        self.coins = 8
    def attack(self, enemy):
        # 10% of time Wizard attack is devastating
        if self.cast_spell():
            enemy.health -= self.power * 3
    def cast_spell(self):
        return random() > .9

# make a Zombie character that doesn't die even if his health is below zero
class Zombie(Enemy):
    def __init__(self):
        super().__init__()
        self.name = "Zombie"
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
    def __init__(self):
        super().__init__()
        self.name = "Shadow"
        self.health = 1
        self.coins = 2
    def defend(self, enemy, attack_power):
        if random() > .1:
            attack_power = 0
        self.health -= attack_power
        print("The %s does %d damage to the %s." % (enemy.name, attack_power, self.name))
