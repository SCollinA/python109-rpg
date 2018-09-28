
class Battle:

    battles_remaining = 3

    def do_battle(self, hero_party, enemy_party):
        while hero_party.alive() and enemy_party.alive():
            hero_party.print_status()
            enemy_party.print_status()
            print()
            for friend in hero_party.party:
                if friend.alive():
                    print("%s's turn." % friend.name)
                    action = friend.choose_action()
                    if action == "1":
                        # attack
                        target = friend.choose_target(hero_party, enemy_party)
                        friend.attack(target)
                    elif action == "2":
                        # choose item
                        item = friend.choose_item()
                        # use item
                        target = friend.choose_target(hero_party, enemy_party)
                        friend.use_item(item, target)
                    elif action == "3":
                        pass
                    elif action == "4":
                        print("fleeing...")
                        return True
                hero_party.print_status()
                enemy_party.print_status()
            # if the enemy party is still standing
            if enemy_party.alive():
                # each enemy gets a turn
                for enemy in enemy_party.party:
                    # if this enemy is alive
                    if enemy.alive():
                        # attack a random friend from hero_party
                        target = enemy.choose_target(hero_party)
                        enemy.attack(target)
            if not hero_party.alive():
                return False
        Battle.battles_remaining -= 1
        return True
