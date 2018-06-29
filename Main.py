from __future__ import print_function
import time, os, platform, sys

OS = platform.system()

def word_core(sen, sec): # Human-like typing
    for letter in sen:
        print(letter, end='')
        sys.stdout.flush()  # Needed for Unix based systems
        time.sleep(sec)

def word_corex(stub, sen): # Stationary title with a natural typing statement
    print(stub + " ", end='')
    sys.stdout.flush()  # Needed for Unix based systems
    time.sleep(0.5)
    for letter in sen:
        print(letter, end='')
        sys.stdout.flush()  # Needed for Unix based systems
        time.sleep(.05)

def intro(): #The intro to the game
    clear()
    word_core("@@;          #@@  @@@@@@@@@@@@@@@@   .@@@@@@@@@@@@@@  @@@@@@@@@@@@@@+    '@@@@@@@@@@@@`\n", 0.001)
    word_core("@@@@         #@@  @@@@@@@@@@@@@@@@  ,@@@@@@@@@@@@@@@  @@@@@@@@@@@@@@@@  @@@@@@@@@@@@@@@`\n", 0.001)
    word_core("@@@@@        #@@  @@@:::::::::::::  @@@@::::::::::::  @@@:::::::::+@@@  @@@+::::::::@@@@\n", 0.001)
    word_core("@@@@@@       #@@  @@@               @@@               @@@          `@@  @@.          @@@\n", 0.001)
    word_core("@@.@@@@.     #@@  @@@@@@@@@@@@@@    @@@               @@@          `@@  @@.          @@@\n", 0.001)
    word_core("@@. ;@@@+    #@@  @@@@@@@@@@@@@@    @@@               @@@          ;@@  @@.          @@@\n", 0.001)
    word_core("@@.  `@@@@   #@@  @@@@@@@@@@@@@@    @@@               @@@@@@@@@@@@@@@@  @@.          @@@\n", 0.001)
    word_core("@@.    @@@@  #@@  @@@               @@@               @@@@@@@@@@@@@@@   @@.          @@@\n", 0.001)
    word_core("@@.     @@@@`#@@  @@@               @@@               @@@   @@@@        @@.          @@@\n", 0.001)
    word_core("@@.      ;@@@@@@  @@@               @@@               @@@    '@@@+      @@.          @@@\n", 0.001)
    word_core("@@.       `@@@@@  @@@:::::::::::::  @@@@::::::::::::  @@@     `@@@@     @@@+::::::::@@@@\n", 0.001)
    word_core("@@.         @@@@  @@@@@@@@@@@@@@@@  ,@@@@@@@@@@@@@@@  @@@       @@@@:   @@@@@@@@@@@@@@@`\n", 0.001)
    word_core("@@.          @@@  @@@@@@@@@@@@@@@@   .@@@@@@@@@@@@@@  @@@        +@@@@   +@@@@@@@@@@@@.\n", 0.001)
    print("\n")
    word_corex("DEVELOPER |", "78 Alpha\n")
    #time.sleep(5)
    #clear()
    #word_core("Welcome to the apocalypse...\n", 0.01)
    print("\n")
    time.sleep(1)
    word_corex("INIT |", "Creates an initial save")
    print("\n")
    time.sleep(0.5)
    word_corex("START |", "Start the game")
    print("\n")
    time.sleep(0.5)
    word_corex("EXIT |", "Exit the application")
    print("\n")
    time.sleep(0.5)
    action = raw_input("What would you like to do: ")
    if action == "INIT":
        Save_Make()
    elif action == "START":
        diff_set()
    elif action == "EXIT":
        clear()
        exit()
    else:
        intro()


def Save_Make(): # Create a save if none exists, this is necessary to run the game, or delete a previous save
    clear()
    global OS
    if OS == "Windows":
        os.system("del Save_file.py")
    else:
        os.system("rm Save_file.py")
    with open("Globals.py", "r") as file:
        read = file.readlines()
        content = [x.strip() for x in read]
    with open("Save_file.py", "a") as written:
        for i in range(0, len(content)):
            written.write(content[i] + "\n")
    word_corex("CREATING |", "Save data has been successfully created!")
    intro()

def diff_set():
    import Level1
    #start_turn()


def clear():
    global OS
    if OS == "Windows":
        os.system("cls")
    else:
        os.system("clear")


intro()
