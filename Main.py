import time, os, platform, sys, Clear, Level1, WordCore
from json_system import *

def intro(): #The intro to the game
    Clear.clear()
    WordCore.word_core("@@;          #@@  @@@@@@@@@@@@@@@@   .@@@@@@@@@@@@@@  @@@@@@@@@@@@@@+    '@@@@@@@@@@@@`\n", 0.0001)
    WordCore.word_core("@@@@         #@@  @@@@@@@@@@@@@@@@  ,@@@@@@@@@@@@@@@  @@@@@@@@@@@@@@@@  @@@@@@@@@@@@@@@`\n", 0.0001)
    WordCore.word_core("@@@@@        #@@  @@@:::::::::::::  @@@@::::::::::::  @@@:::::::::+@@@  @@@+::::::::@@@@\n", 0.0001)
    WordCore.word_core("@@@@@@       #@@  @@@               @@@               @@@          `@@  @@.          @@@\n", 0.0001)
    WordCore.word_core("@@.@@@@.     #@@  @@@@@@@@@@@@@@    @@@               @@@          `@@  @@.          @@@\n", 0.0001)
    WordCore.word_core("@@. ;@@@+    #@@  @@@@@@@@@@@@@@    @@@               @@@          ;@@  @@.          @@@\n", 0.0001)
    WordCore.word_core("@@.  `@@@@   #@@  @@@@@@@@@@@@@@    @@@               @@@@@@@@@@@@@@@@  @@.          @@@\n", 0.0001)
    WordCore.word_core("@@.    @@@@  #@@  @@@               @@@               @@@@@@@@@@@@@@@   @@.          @@@\n", 0.0001)
    WordCore.word_core("@@.     @@@@`#@@  @@@               @@@               @@@   @@@@        @@.          @@@\n", 0.0001)
    WordCore.word_core("@@.      ;@@@@@@  @@@               @@@               @@@    '@@@+      @@.          @@@\n", 0.0001)
    WordCore.word_core("@@.       `@@@@@  @@@:::::::::::::  @@@@::::::::::::  @@@     `@@@@     @@@+::::::::@@@@\n", 0.0001)
    WordCore.word_core("@@.         @@@@  @@@@@@@@@@@@@@@@  ,@@@@@@@@@@@@@@@  @@@       @@@@:   @@@@@@@@@@@@@@@`\n", 0.0001)
    WordCore.word_core("@@.          @@@  @@@@@@@@@@@@@@@@   .@@@@@@@@@@@@@@  @@@        +@@@@   +@@@@@@@@@@@@.\n", 0.0001)
    print("\n")
    WordCore.word_corex("DEVELOPER |", "78 Alpha\n")
    time.sleep(0.5)
    WordCore.word_corex("START |", "Start the game")
    print("\n")
    time.sleep(0.5)
    WordCore.word_corex("NEW |", "Create a new game")
    print("\n")
    time.sleep(0.5)
    WordCore.word_corex("SETTINGS |", "Change game settings")
    print("\n")
    time.sleep(0.5)
    WordCore.word_corex("EXIT |", "Exit the application")
    print("\n")
    time.sleep(0.5)
    action = input(str("What would you like to do: "))
    if action == "START":
        Level1.Save_Check()
    elif action == "NEW":
        load_3()
        Level1.Save_Check()
    elif action == "SETTINGS":
        settings()
    elif action == "EXIT":
        Clear.clear()
        exit()
    else:
        intro()

def settings():
    with open("Globals.txt", 'r') as f:
        variables = json.load(f)
    print("This feature is in [alpha], and may cause [Program Termination]")
    color_ = str(input("Enable color (Current value [" + str(variables["color"]) + "]): "))
    if color_ == "YES":
        variables["color"] = 1
        with open("Globals.txt", 'w') as f2:
            json.dump(variables, f2, indent=3)
        intro()
    elif color_ == "NO":
        variables["color"] = 0
        with open("Globals.txt", 'w') as f2:
            json.dump(variables, f2, indent=3)
        intro()
    else:
        settings()

intro()
