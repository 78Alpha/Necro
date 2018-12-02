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
    word_core("@@;          #@@  @@@@@@@@@@@@@@@@   .@@@@@@@@@@@@@@  @@@@@@@@@@@@@@+    '@@@@@@@@@@@@`\n", 0.0001)
    word_core("@@@@         #@@  @@@@@@@@@@@@@@@@  ,@@@@@@@@@@@@@@@  @@@@@@@@@@@@@@@@  @@@@@@@@@@@@@@@`\n", 0.0001)
    word_core("@@@@@        #@@  @@@:::::::::::::  @@@@::::::::::::  @@@:::::::::+@@@  @@@+::::::::@@@@\n", 0.0001)
    word_core("@@@@@@       #@@  @@@               @@@               @@@          `@@  @@.          @@@\n", 0.0001)
    word_core("@@.@@@@.     #@@  @@@@@@@@@@@@@@    @@@               @@@          `@@  @@.          @@@\n", 0.0001)
    word_core("@@. ;@@@+    #@@  @@@@@@@@@@@@@@    @@@               @@@          ;@@  @@.          @@@\n", 0.0001)
    word_core("@@.  `@@@@   #@@  @@@@@@@@@@@@@@    @@@               @@@@@@@@@@@@@@@@  @@.          @@@\n", 0.0001)
    word_core("@@.    @@@@  #@@  @@@               @@@               @@@@@@@@@@@@@@@   @@.          @@@\n", 0.0001)
    word_core("@@.     @@@@`#@@  @@@               @@@               @@@   @@@@        @@.          @@@\n", 0.0001)
    word_core("@@.      ;@@@@@@  @@@               @@@               @@@    '@@@+      @@.          @@@\n", 0.0001)
    word_core("@@.       `@@@@@  @@@:::::::::::::  @@@@::::::::::::  @@@     `@@@@     @@@+::::::::@@@@\n", 0.0001)
    word_core("@@.         @@@@  @@@@@@@@@@@@@@@@  ,@@@@@@@@@@@@@@@  @@@       @@@@:   @@@@@@@@@@@@@@@`\n", 0.0001)
    word_core("@@.          @@@  @@@@@@@@@@@@@@@@   .@@@@@@@@@@@@@@  @@@        +@@@@   +@@@@@@@@@@@@.\n", 0.0001)
    print("\n")
    word_corex("DEVELOPER |", "78 Alpha\n")
    time.sleep(0.5)
    word_corex("START |", "Start the game")
    print("\n")
    time.sleep(0.5)
    word_corex("EXIT |", "Exit the application")
    print("\n")
    time.sleep(0.5)
    action = input(str("What would you like to do: "))
    if action == "START":
        diff_set()
    elif action == "EXIT":
        clear()
        exit()
    else:
        intro()

def diff_set():
    import Level1

def clear():
    global OS
    if OS == "Windows":
        os.system("cls")
    else:
        os.system("clear")

intro()
