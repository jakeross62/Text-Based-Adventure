# when selling if you want to cancel you might have to add a extra function for checking is exit is said or something
#add rounding to sell
from game import *
from gameparser import *
from player import *

shop_items = {
    "potions": ["tiny", "medium", "bean"],
    "Weapons": ["club", "knife", "sword", "map"],
    "keys": ["wkey", "skey", "dkey", "bosskey"]
}

shop_items_id = {
    "tiny": item_tiny_healthpotion,
    "medium": item_medium_healthpotion,
    "bean": item_magic_bean,
    "club": item_club,
    "knife": item_knife,
    "sword": weapon_rusty_sword,
    "wkey": wooden_key,
    "skey": silver_key,
    "dkey": diamond_key,
    "bosskey": item_boss_key,
    "map": item_map,
}

# Shows items in the shop
def print_shop_buy():
    # iterates all the category in the shop
    global buy_id
    buy_id = []
    for i in shop_items:
        # prints the shop category
        print("--------------------"+i.upper()+"--------------------")
        # iterates all the items in the category
        for items in shop_items[i]:
            a = shop_items_id[items]
            buy_id.append(a['id'])
            temp = a['name']
            print("ID ", a['id'])
            print("Name: " + temp[0].upper() + temp[1: len(temp)], "\nPrice:", a["price"], "Shronkles\n")
    buy()

def print_shop_sell():
    print("\nWhat would you like to sell from your inventory?\n")
    print("---------- Items you can sell ----------")
    for i in inventory:
        # prints the Inventory items with price
        if "price" in i.keys():
            print("ID: ", i["id"])
            print("Name:", i["name"])
            print("Price:", round(i['price'] * 0.8, 2), "Shronkles\n")
    sell()

def shop_option():
    print("So what brings you here today to BUY, SELL or LEAVE with em sweet shronkles")
    option = input("> ")
    option = normalise_input(option)

    if not option:
        print("YOU FOOL WE DON'T DO THAT HERE!!")

    elif option == ['buy']:
        print_shop_buy()

    elif option == ['sell']:
        print_shop_sell()
    elif len(option) == 0:
        print("Please enter something.")
        shop_option()
    elif option == ['leave']:
        print("Aright then don't come in unless you want to buy something. -Bonky mumbles to himselve")
    else:
        print("Invalid input please try again")
        shop_option()

def buy():
    print("Please Select a item.    -- Or enter BACK to go to previous option --")
    print("You currently have", player_stats["shronkles"], "Shronkles")
    user_input = input("> ")
    while not user_input:
        print("---- Empty Value ----\n\nPlease enter a value. \n-- Or enter BACK to go to previous option --")
        user_input = input("> ")
    user_input = normalise_input(user_input)

    # checks if user input is in the items that the store sells
    if not user_input:
        print("YOU FOOL WE DON'T HAVE THAT HERE!!")
        buy()
    elif user_input[0] in buy_id:
        value_item = shop_items_id[user_input[0]]
        if player_stats["shronkles"] >= value_item['price']:
            player_stats["shronkles"] -= value_item['price']
            inventory.append(value_item)
            print("Here you go good sir have your wonderful", value_item['name'], "\n\n---- You've obtained", value_item['name'], "----\n")
            print("You currently have", player_stats["shronkles"], "Shronkles")
        else:
            print("You what?! Don't have enough money?! GET OUT DON'T WASTE MY GOBBLE TIME!\n\n----Gets Kicked Out----\n")
    elif user_input[0] == "back":
        print(" ")
        shop_main()
        user_input = ("")
    elif user_input[0] not in buy_id:
        print("Item doesn't exist please enter a valid value!")
        buy()
    pass

def sell():
    print("Please Select a item.    -- Or enter BACK to go to previous option --")
    print("You currently have", player_stats["shronkles"], "Shronkles")
    user_input = input("> ")
    while not user_input:
        print("---- Empty Value ----\n\nPlease enter a value. \n-- Or enter BACK to go to previous option --")
        user_input = input("> ")
    user_input = normalise_input(user_input)
    counter = 0
    if not user_input:
        print("YOU FOOL WE DON'T HAVE THAT HERE!!")
        sell()

    elif user_input[0] == "back":
        print(" ")
        shop_main()
        user_input = ("")

    else:
        for i in inventory:
            if user_input[0] == i['id']:
                counter += 1
            if i == items_id[user_input[0]]:
                item = i
            else:
                pass

        if counter > 0:
            player_stats["shronkles"] += round(item['price'] * 0.8, 2)
            inventory.remove(item)
            print("\nHehehehe another item bought from a fool!\n\n---- Price sold for:", round(item['price'] * 0.8, 2), "Shronkles ----\n")
            print("You currently have", player_stats["shronkles"], "Shronkles")
        elif counter == 0:
            print("Item doesn't exist please enter a valid value!")
            sell()
    pass

# main shop body
def shop_main():
    print("\n-----------------------------------------Shop-----------------------------------------\n")
    print("Welcome to the store of Bonkle\nWe sell the best quality items at floor one with competitve prices! *wink wink*\n")
    shop_option()

    pass