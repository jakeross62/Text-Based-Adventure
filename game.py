from operator import inv
from map import *
from player import *
from items import *
from enemies import *
from gameparser import *
from random import *
from story import *
from room_map import *
from shop import *


# global enemy_in_room
execute_use_called = False
enemy_in_room = False


# Prints useful commands for the player to play the game
def help():
    print()
    print("Help Section:")
    print("Type 'take' 'item' to take an item.")
    print("Type 'drop' 'item' to drop an item.")
    print("Type 'use' 'item' to use an item.")
    print("Type 'health' to view your health.")
    print("Type 'stats' to view your stats.")
    current_room["info"] = 0


def stats():
    print()
    print("Current Player Stats:")
    print("Level:", player_stats["level"])
    print("Max Health:", player_stats["maxhealth"])
    print("Current Health:", player_stats["health"])
    print("Damage Multiplier:", player_stats["multiplier"])
    print("Max weight:", player_stats["weight"])
    print("Experience:", player_stats["experience"])
    print("Shronkles:", player_stats["shronkles"])
    current_room["info"] = 0


# This function puts the list of items in a string seperated by ","
def list_of_items(items):
    listofitems = ""
    for item in items:
        if listofitems == "":
            listofitems = item["name"]
        else:
            listofitems = listofitems + ", " + item["name"]
    return listofitems


# This function prints the items in the room
def print_room_items(room):
    if list_of_items(room["items"]) != "":
        print("There is", list_of_items(room["items"]), "here.")
        print()


# This funciton prints the items in your inventory
def print_inventory_items(items):
    if list_of_items(items) != "":
        print("You have", list_of_items(items).lower() + ".")
        print("")


def list_of_enemies(enemies):
    listofenemies = ""
    for enemy in enemies:
        if listofenemies == "":
            listofenemies = enemy["id"]
        else:
            listofenemies = listofenemies + "," + enemy["id"]
        return listofenemies


def print_room_enemies(room):
    if list_of_enemies(room["enemies"]) != None:
        print("There is a", list_of_enemies(room["enemies"]), "here! You cannot go to another room!")
        print()
        print_enemy_health()
        enemy_in_room == True
    else:
        print("This room is clear!")


# This function prints the name and discription of a room, as well as the items and if enemies are present.
def print_room(room):
    if room["story"] != "" and room["story"]["used"] == 1:
        print(room["story"]["text"])
        room["story"]["used"] = 0
    print()
    print(room["name"].upper())
    print()
    print(room["description"])
    print()
    print_room_items(room)
    print_health()
    print()
    print_room_enemies(room)


def print_enemy_health():
    if len(current_room["enemies"]) != 0:
        for enemies in current_room["enemies"]:
            health = enemies["health"]
            health_dashes = 100
            max_health = enemies["maxhealth"]

        # Maths
        if health < 0:
            health = 0

        convert_to_dashes = float(max_health / health_dashes)
        current_dashes = int(health / convert_to_dashes)
        remaining_health = health_dashes - current_dashes

        # Actually printing the health bar
        health_display = '=' * current_dashes
        remaining_display = ' ' * remaining_health
        percent = str(int((health / max_health) * 100)) + '%'
        print()
        print("ENEMY HEALTH:")
        print("                                               " + "Health:")
        print("||" + health_display + remaining_display + "||")
        print("                                                " + percent)


def print_health():
    health = player_stats["health"]
    health_dashes = 100
    max_health = player_stats["maxhealth"]
    if health < 0:
        health = 0
        player_stats["health"] = 0

    # Maths
    convert_to_dashes = int(max_health / health_dashes)
    current_dashes = int(health / convert_to_dashes)
    remaining_health = health_dashes - current_dashes

    # Actually printing the health bar
    health_display = '=' * current_dashes
    remaining_display = ' ' * remaining_health
    percent = str(int((health / max_health) * 100)) + '%'
    print()
    print("PLAYER HEALTH:")
    print("                                               " + "Health:")
    print("||" + health_display + remaining_display + "||")
    print("                                                " + percent)

    if player_stats["health"] <= 0:
        print("Game ORGER, You have died!")
        print("Press ENTER to end program")
        input("> ")
        print("The game will now terminate! . . . . ")
        exit()


# This function prints the menu of exits
def print_exit(direction, leads_to):
    print("GO " + direction.upper() + " to " + leads_to + ".")


# This function displays the menu to the player
def print_menu(exits, room_items, inv_items):
    print()
    print("You can:")
    for direction in exits:
        print_exit(direction, exit_leads_to(exits, direction))
    for item in room_items:
        print("TAKE", item["id"].upper(), "to take", item["name"] + ".")
    for item2 in inv_items:
        print("DROP", item2["id"].upper(), "to drop", item2["name"])
    for item2 in inv_items:
        print("USE", item2["id"].upper(), "to use", item2["name"])
    if current_room == room_1_u:
        print("Type SHOP to access the store")

    print("What do you want to do?")


def fight_room_enemies(enemies):  ## This is UNFINISHED and needs work before moving forward.

    for enemies in current_room["enemies"]:
        if execute_use_called == True:
            print(enemies["name"], "used", str(enemies["weapon_id"].lower()) + "!")  ## Doesn't redo after item used.
            player_stats["health"] = player_stats["health"] - enemies["weapon_damage"]
            print("Your health has been reduced by", str(enemies["weapon_damage"]) + ".")
            print_health()

            if enemies["health"] <= 0:
                print()
                print(enemies["name"], "has been killed! You have won this round...")
                money(enemies)
                experience(enemies)
                chance_drop = randint(1, 3)
                if chance_drop == 1 and enemies["id"] == "goblin":
                    inventory.append(item_tiny_healthpotion)
                    print("The enemy dropped a tiny health potion")
                if chance_drop == 1 and enemies["id"] == "large rat":
                    inventory.append(item_tiny_healthpotion)
                    print("The enemy dropped a tiny health potion")
                if chance_drop == 1 and enemies["id"] != "goblin" and enemies["id"] != "large rat":
                    inventory.append(item_medium_healthpotion)
                    print("The enemy dropped a medium health potion")
                print("You may now leave this area and move on!")
                current_room["enemies"].clear()  # Deletes the enemy from the room
                enemy_in_room == False
                if execute_use_called == True:
                    print("Warning: Weapons will not do anything as the enemy has been killed!")


def fight_enemy_boss(enemies):
    for enemies in current_room["enemies"]:
        if execute_use_called == True:
            print(enemies["name"], "used", str(enemies["weapon_id"].lower()) + "!")  ## Doesn't redo after item used.
            player_stats["health"] = player_stats["health"] - enemies["weapon_damage"]
            print("Your health has been reduced by", str(enemies["weapon_damage"]) + ".")
            print_health()

        if enemies["health"] <= 0:
            print()
            print(enemies["name"], "has been killed! You have defeated the final boss!")
            money(enemies)
            experience(enemies)
            print("That's it for the demo version, we hope you enjoyed our game!")
            current_room["enemies"].clear()  # Deletes the enemy from the room
            enemy_in_room == False
            print("Press ENTER to end program")
            input("> ")
            print("The game will now terminate! . . . . ")
            exit()


def fight_enemy_miniboss(enemies):
    for enemies in current_room["enemies"]:
        if execute_use_called == True:
            print(enemies["name"], "used", str(enemies["weapon_id"].lower()) + "!")  ## Doesn't redo after item used.
            player_stats["health"] = player_stats["health"] - enemies["weapon_damage"]
            print("Your health has been reduced by", str(enemies["weapon_damage"]) + ".")
            print_health()

        if enemies["health"] <= 0:
            print()
            print(enemies["name"], "has been killed! You have defeated scorilla!")
            money(enemies)
            experience(enemies)
            print("It dropped a mysterious key!")
            inventory.append(item_shronk_key)
            current_room["enemies"].clear()  # Deletes the enemy from the room
            enemy_in_room == False


# This function find the room the player would like to go next
def exit_leads_to(exits, direction):
    return rooms[exits[direction]]["name"]


# This function checks to see if the exit is valid
def is_valid_exit(exits, chosen_exit):
    return chosen_exit in exits


# This function moves the player to the next room
def execute_go(direction):
    global current_room
    check = 0
    if is_valid_exit(current_room["exits"], direction) == True:
        if len(current_room["enemies"]) == 0 and current_room["id"] == "1s" and direction == "east":
            for item in inventory:
                if item["id"] == "shronkkey":
                    print()
                    print("Welcome to the final boss battle of floor 1, I'm suprised you made it this far!")
                    print("===============================================================================")
                    current_room = rooms[current_room["exits"][direction]]
                    current_room["info"] = 1
                    check = check + 1
                    return
            if check == 0:
                print("You need a key to enter this room!")
                current_room["info"] = 0
        elif len(current_room["enemies"]) == 0 and current_room["id"] == "1b" and direction == "south":
            for item in inventory:
                if item["id"] == "bosskey":
                    current_room = rooms[current_room["exits"][direction]]
                    current_room["info"] = 1
                    check = check + 1
                    return
            if check == 0:
                print("You need a key to enter this room!")
                current_room["info"] = 0
        elif len(current_room["enemies"]) == 0 and current_room["id"] == "1q" and direction == "east":
            for item in inventory:
                if item["id"] == "bosskey":
                    current_room = rooms[current_room["exits"][direction]]
                    current_room["info"] = 1
                    check = check + 1
                    return
            if check == 0:
                print("You need a key to enter this room!")
                current_room["info"] = 0
        elif len(current_room["enemies"]) == 0 and current_room["id"] == "1j" and current_room["solved"] == False:
            print()
            print("You hear a voice coming from the door to your west.....")
            print('"If you answer this riddle correctly, you will gain access to this room"')
            print('"Ive got oceans without water,"')
            print('"Ive got deserts without sand,"')
            print('"Ive fields without soil,"')
            print('"Ive mountains without land."')
            answer = input('"What am I?" ')
            if normalise_input(answer)[0] == "map":
                print("That is correct! You now have access to this room!")
                current_room["solved"] = True
                current_room = rooms[current_room["exits"][direction]]
                current_room["info"] = 1
            else:
                print("That is incorrect! You dont have access to this room!")
        elif len(current_room["enemies"]) == 0 and current_room["id"] != "1s":
            spawnenemy()
            for enemy in enemies:
                enemies[enemy]["health"] = enemies[enemy]["maxhealth"]
            current_room = rooms[current_room["exits"][direction]]
            current_room["info"] = 1
        elif len(current_room["enemies"]) == 0 and current_room["id"] == "1s" and direction == "west":
            spawnenemy()
            for enemy in enemies:
                enemies[enemy]["health"] = enemies[enemy]["maxhealth"]
            current_room = rooms[current_room["exits"][direction]]
            current_room["info"] = 1
        else:
            print("You must kill opponent first!")
            current_room["info"] = 0
    else:
        print("You cannot go there.")
        current_room["info"] = 0


# This function takes the specified item in the room
def execute_take(item_id):
    check = 0
    count = 0
    totalmass = 0

    for inv in inventory:
        totalmass = totalmass + float(inv["mass"])
    if totalmass < player_stats["weight"]:
        for item in current_room["items"]:
            if item["id"] == item_id:
                print()
                print("You have taken", item["name"] + ".")
                inventory.append(current_room["items"][count])
                del current_room["items"][count]
                check = check + 1
            count = count + 1
        if check != 1:
            print("You cannot take that.")
    else:
        print("You are carrying too many items!")

    if totalmass == 3.0:
        print("You are carrying too many items!")
    current_room["info"] = 0


# This function drops the specified item into the room
def execute_drop(item_id):
    check = 0
    count = 0
    for item in inventory:
        if item["id"] == item_id:
            print()
            print("You have dropped", item["name"] + ".")
            current_room["items"].append(inventory[count])
            del inventory[count]
            check = check + 1
        count = count + 1
    if check != 1:
        print("You cannot drop that.")
    current_room["info"] = 0


# This function uses a specified item and then deletes it from the inventory
def execute_use(item_id):
    global execute_use_called
    execute_use_called = True
    check = 0
    count = -1

    for item in inventory:
        count = count + 1
        if item["id"] == item_id and item["weapon"] == "Yes":
            if len(current_room["enemies"]) != 0:
                if current_room["enemies"][0]["id"] == "SHRONK":
                    for enemies in current_room["enemies"]:
                        print()
                        print("The enemies health has been reduced by", str(item["damage"] * round(player_stats["multiplier"])) + ".")
                        enemies["health"] = enemies["health"] - item["damage"] * round(player_stats["multiplier"])
                        print()
                        fight_enemy_boss(current_room["enemies"][0])
                        print_enemy_health()
                elif current_room["enemies"][0]["id"] == "scorilla":
                    for enemies in current_room["enemies"]:
                        print()
                        print("The enemies health has been reduced by", str(item["damage"] * round(player_stats["multiplier"])) + ".")
                        enemies["health"] = enemies["health"] - item["damage"] * round(player_stats["multiplier"])
                        print()
                        fight_enemy_miniboss(current_room["enemies"][0])
                        print_enemy_health()
                else:
                    for enemies in current_room["enemies"]:
                        print()
                        print("The enemies health has been reduced by", str(item["damage"] * round(player_stats["multiplier"])) + ".")
                        enemies["health"] = enemies["health"] - item["damage"] * round(player_stats["multiplier"])
                        print()
                        fight_room_enemies(enemies)
                        print_enemy_health()
            else:
                print()
                print("There is no enemy to use that on.")
            check = check + 1

        elif item["id"] == item_id and item["weapon"] == "No":
            if item["id"] == "map":
                print()
                print("You take a glance at your map:")
                room_map()
                check = check + 1
            elif item["id"] == "wkey":
                if current_room["id"] == room_1_k["id"]:
                    print()
                    print("The key has worked!")
                    print("You have found the legendary cleaver and 50 shronkles!")
                    inventory.append(weapon_legendary)
                    player_stats["shronkles"] = player_stats["shronkles"] + 50
                    inventory.remove(wooden_key)
                else:
                    break
            elif item["id"] == "skey":
                if current_room == room_1_k:
                    print()
                    print("The key did not work!")
                    inventory.remove(silver_key)
                else:
                    break
            elif item["id"] == "dkey":
                if current_room == room_1_k:
                    print()
                    print("The key did not work")
                    inventory.remove(diamond_key)
                else:
                    break
            else:
                print("You have used", item["name"] + ".")
                del inventory[count]
                check = check + 1

                # Checks if the item being used is a potion, and increments player_health if it hasn't reached maxhealth
                if item_id == item_tiny_healthpotion["id"] or item_id == item_medium_healthpotion["id"] or item_id == \
                        item_big_healthpotion["id"]:
                    if item_tiny_healthpotion["health_increase"] + player_stats["health"] > player_stats["maxhealth"] or \
                            item_medium_healthpotion["health_increase"] + player_stats["health"] > player_stats[
                        "maxhealth"] or item_big_healthpotion["health_increase"] + player_stats["health"] > \
                            player_stats["maxhealth"]:
                        print("Bad move! Your health bar was full, but you still lost the item!")
                        player_stats["health"] == player_stats["maxhealth"]
                        print_health()
                    else:
                        print("Your health has been increased by", str(item["health_increase"]) + ".")
                        player_stats["health"] = player_stats["health"] + item["health_increase"]
                        print_health()

    if check != 1:
        print()
        print("You cannot use that.")
    current_room["info"] = 0


def experience(enemy):
    experienceearned = randint(enemy["minexperience"], enemy["maxexperience"])
    print("You have gained", experienceearned, "experience.")
    player_stats["experience"] = player_stats["experience"] + experienceearned
    if player_stats["experience"] >= 10 and player_stats["level"] == 1:
        player_stats["level"] = 2
        player_stats["maxhealth"] = player_stats["maxhealth"] + 25
        player_stats["weight"] = player_stats["weight"] + 1.5
        player_stats["health"] = player_stats["maxhealth"]
        player_stats["multiplier"] += 0.2
        print("Well done! You have leveled up to level", player_stats["level"])
        print("Your max health is now", player_stats["maxhealth"], "and max weight is now", player_stats["weight"])
        print("Your health has been restored!")
        print("You are now a little bit less of a noob :)")
    if player_stats["experience"] >= 50 and player_stats["level"] == 2:
        player_stats["level"] = 3
        player_stats["maxhealth"] = player_stats["maxhealth"] + 25
        player_stats["weight"] = player_stats["weight"] + 1.5
        player_stats["health"] = player_stats["maxhealth"]
        player_stats["multiplier"] += 0.2
        print("Well done! You have leveled up to level", player_stats["level"])
        print("Your max health is now", player_stats["maxhealth"], "and max weight is now", player_stats["weight"])
        print("Your health has been restored!")
    if player_stats["experience"] >= 150 and player_stats["level"] == 3:
        player_stats["level"] = 4
        player_stats["maxhealth"] = player_stats["maxhealth"] + 25
        player_stats["weight"] = player_stats["weight"] + 1.5
        player_stats["health"] = player_stats["maxhealth"]
        player_stats["multiplier"] += 0.2
        print("Well done! You have leveled up to level", player_stats["level"])
        print("Your max health is now", player_stats["maxhealth"], "and max weight is now", player_stats["weight"])
        print("Your health has been restored!")
    if player_stats["experience"] >= 300 and player_stats["level"] == 4:
        player_stats["level"] = 5
        player_stats["maxhealth"] = player_stats["maxhealth"] + 25
        player_stats["weight"] = player_stats["weight"] + 1.5
        player_stats["health"] = player_stats["maxhealth"]
        player_stats["multiplier"] += 0.2
        print("Well done! You have leveled up to level", player_stats["level"])
        print("Your max health is now", player_stats["maxhealth"], "and max weight is now", player_stats["weight"])
        print("Your health has been restored!")


def spawnenemy():
    noofenemies = 0
    noofrooms = 0
    for room in rooms:
        noofrooms = noofrooms + 1

    while noofenemies < 10:
        noofenemies = 0
        for room in rooms:
            noofenemies = noofenemies + len(rooms[room]["enemies"])
            if noofenemies == 10:
                return
            elif randint(0, noofrooms) == 22:
                if len(rooms[room]["enemies"]) == 0:
                    noofpossibleenemies = len(rooms[room]["possibleenemies"])
                    randomenemy = randint(0, noofpossibleenemies - 1)
                    rooms[room]["enemies"].append(rooms[room]["possibleenemies"][randomenemy])


def money(enemy):
    moneyearned = randint(enemy["minshronkles"], enemy["maxshronkles"])
    print("You have gained", moneyearned, "shronkles.")
    player_stats["shronkles"] = player_stats["shronkles"] + moneyearned


# This function checks to see what the player wants to do
def execute_command(command):
    if 0 == len(command):
        print("Please enter a command.")
        current_room["info"] = 0
        return

    if command[0] == "go":
        if len(command) > 1:
            execute_go(command[1])
        else:
            print("Go where?")
            current_room["info"] = 0

    elif command[0] == "take":
        if len(command) > 1:
            execute_take(command[1])
        else:
            print("Take what?")
            current_room["info"] = 0

    elif command[0] == "drop":
        if len(command) > 1:
            execute_drop(command[1])
        else:
            print("Drop what?")
            current_room["info"] = 0

    elif command[0] == "use":
        if len(command) > 1:
            execute_use(command[1])
        else:
            print("Use what?")
            current_room["info"] = 0

    elif command[0] == "shop" and current_room == room_1_u:
        shop_main()

    elif command[0] == "help":
        help()

    elif command[0] == "stats":
        stats()

    elif command[0] == "health":
        print_health()
        current_room["info"] = 0

    else:
        print("This makes no sense.")
        current_room["info"] = 0


# This function displays the menu to the player and see what they want to do
def menu(exits, room_items, inv_items):
    # Display menu
    print_menu(exits, room_items, inv_items)

    # Read player's input
    user_input = input("> ")

    # Normalise the input
    normalised_user_input = normalise_input(user_input)

    return normalised_user_input


# This function moves the player
def move(exits, direction):
    # Next room to go to
    for enemies in current_room["enemies"]:
        if enemies["health"] <= 0:
            return rooms[exits[direction]]
        else:
            print("You must kill opponent first!")


def room_info():
    print_room(current_room)
    print_inventory_items(inventory)
    print("What do you want to do?")
    print("Enter 'help' for a list of commands.")


# This is the entry point of the program
def main():
    # Main game loop
    while True:
        # Display game status (room description, inventory etc.)
        # Show the menu with possible actions and ask the player
        if current_room["info"] == 1:
            room_info()

        command = menu(current_room["exits"], current_room["items"], inventory)

        # Execute the player's command
        execute_command(command)


# def menu_main():
#     print("""
#           _____ __ __  ____   ___   ____   __  _
#          / ___/|  |  ||    \ /   \ |    \ |  |/ ]   __
#         (   \_ |  |  ||  D  )     ||  _  ||  ' /   |  |
#          \__  ||  _  ||    /|  O  ||  |  ||    \   |__|
#          /  \ ||  |  ||    \|     ||  |  ||     |   __
#          \    ||  |  ||  .  \     ||  |  ||  .  |  |  |
#           \___||__|__||__|\_|\___/ |__|__||__|\_|  |__|
#
#                      ______  __ __    ___
#                     |      ||  |  |  /  _]
#                     |      ||  |  | /  [_
#                     |_|  |_||  _  ||    _]
#                       |  |  |  |  ||   [_
#                       |  |  |  |  ||     |
#                       |__|  |__|__||_____|
#
#   ____  __    __   ____  __  _    ___  ____   ____  ____    ____
#  /    ||  |__|  | /    ||  |/ ]  /  _]|    \ |    ||    \  /    |
# |  o  ||  |  |  ||  o  ||  ' /  /  [_ |  _  | |  | |  _  ||   __|
# |     ||  |  |  ||     ||    \ |    _]|  |  | |  | |  |  ||  |  |
# |  _  ||  `  '  ||  _  ||     ||   [_ |  |  | |  | |  |  ||  |_ |
# |  |  | \      / |  |  ||  .  ||     ||  |  | |  | |  |  ||     |
# |__|__|  \_/\_/  |__|__||__|\_||_____||__|__||____||__|__||___,_|
#
#                                                               """)
#     print("\n\nWelcome to Shronk: The Awakening!!\n")
#     menu_print()
#
#
# def menu_print():
#     print("-------- Menu --------\n")
#     print("Enter START To Start Your Unknown Journey")
#     print("Enter EXIT To Leave The Game")
#     start = input("> ")
#     start = normalise_input(start)
#     if not start:
#         print("Please enter something.")
#         menu_print()
#     elif start[0] == "start":
#         mode()
#     elif start[0] == "exit":
#         print("Shutting down.........")
#         exit()
#     else:
#         print("Please enter a valid value!")
#         menu_print()
#
#
# def mode():
#     print("\nPlease choose a mode that you would like to start in:\n")
#     print("- Easy\n- Normal")
#     print("\nEnter EASY for easy difficulty\nEnter NORMAL for Regular difficulty")
#     modes = input("> ")
#     modes = normalise_input(modes)
#     if not modes:
#         print("Please enter something.")
#         mode()
#     elif modes[0] == "easy":
#         player_stats["maxhealth"] *= 2
#         player_stats["multiplier"] *= 1.5
#         main()
#     elif modes[0] == "normal":
#         main()
#     else:
#         print("Please enter a valid value!")
#         mode()
#
#
# menu_main()
