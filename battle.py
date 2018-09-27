def do_battle(hero_party, enemy_party):
    
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