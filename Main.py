import time, os, platform, sys, Clear, Level1, WordCore, UniData

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
        Level1.UniWrite()
        os.system("rm Save_file.py")
        Level1.Save_Check()
    elif action == "SETTINGS":
        settings()
    elif action == "EXIT":
        Clear.clear()
        exit()
    else:
        intro()

def settings():
    color = str(input("Enable color (Current value [" + str(UniData.color) + "]): " ))
    if color == "YES":
        with open('UniData.py', 'r') as file:
            data = file.readlines()
        data[27] = "color = 1\n"
        with open("UniData.py", 'w') as file:
            file.writelines(data)
        WordCore.word_core("Color Enabled", 0.1)
        intro()
    elif color == "NO":
        with open('UniData.py', 'r') as file:
            data = file.readlines()
        data[27] = "color = 0\n"
        with open("UniData.py", 'w') as file:
            file.writelines(data)
        WordCore.word_core("Color Disabled", 0.1)
        intro()
    else:
        settings()

intro()
