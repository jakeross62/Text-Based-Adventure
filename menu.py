from gameparser import *
from game import *
from player import *

def menu_main():
    print(""" 
          _____ __ __  ____   ___   ____   __  _                 
         / ___/|  |  ||    \ /   \ |    \ |  |/ ]   __             
        (   \_ |  |  ||  D  )     ||  _  ||  ' /   |  |            
         \__  ||  _  ||    /|  O  ||  |  ||    \   |__|            
         /  \ ||  |  ||    \|     ||  |  ||     |   __             
         \    ||  |  ||  .  \     ||  |  ||  .  |  |  |            
          \___||__|__||__|\_|\___/ |__|__||__|\_|  |__|            
                                                                 
                     ______  __ __    ___                        
                    |      ||  |  |  /  _]                       
                    |      ||  |  | /  [_                        
                    |_|  |_||  _  ||    _]                       
                      |  |  |  |  ||   [_                        
                      |  |  |  |  ||     |                       
                      |__|  |__|__||_____|                       
                                                                 
  ____  __    __   ____  __  _    ___  ____   ____  ____    ____ 
 /    ||  |__|  | /    ||  |/ ]  /  _]|    \ |    ||    \  /    |
|  o  ||  |  |  ||  o  ||  ' /  /  [_ |  _  | |  | |  _  ||   __|
|     ||  |  |  ||     ||    \ |    _]|  |  | |  | |  |  ||  |  |
|  _  ||  `  '  ||  _  ||     ||   [_ |  |  | |  | |  |  ||  |_ |
|  |  | \      / |  |  ||  .  ||     ||  |  | |  | |  |  ||     |
|__|__|  \_/\_/  |__|__||__|\_||_____||__|__||____||__|__||___,_|
                                                              
                                                              """)
    print("\n\nWelcome to Shronk: The Awakening!!\n")
    menu_print()

def menu_print():
    print("-------- Menu --------\n")
    print("Enter START To Start Your Unknown Journey")
    print("Enter EXIT To Leave The Game")
    start = input("> ")
    start = normalise_input(start)
    if not start:
        print("Please enter something.")
        menu_print()
    elif start[0] == "start":
        mode()
    elif start[0] == "exit":
        print("Shutting down.........")
        exit()
    else:
        print("Please enter a valid value!")
        menu_print()

def mode():
    print("\nPlease choose a mode that you would like to start in:\n")
    print("- Easy\n- Normal")
    print("\nEnter EASY for easy difficulty\nEnter NORMAL for Regular difficulty")
    modes = input("> ")
    modes = normalise_input(modes)
    if not modes:
        print("Please enter something.")
        mode()
    elif modes[0] == "easy":
        player_stats["health"] *= 2
        player_stats["maxhealth"] *= 2
        player_stats["multiplier"] *= 1.5
        main()
    elif modes[0] == "normal":
        main()
    else:
        print("Please enter a valid value!")
        mode()
menu_main()