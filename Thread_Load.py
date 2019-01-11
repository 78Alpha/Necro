from openal import *
import time
import time, os, platform, sys, Clear, Level1, WordCore, UI, threading
from json_system import *
from ColorSplash import *
from Settings import *


def f1():
    # open our wave file
    source = oalOpen("Necro6.wav")

    # and start playback
    source.play()
    #while source.get_state() == AL_PLAYING:
    # check if the file is still playing


ft = threading.Thread(f1())


def intro(): #The intro to the game
    print(Reset, end='\n')
    Clear.clear()
    with open("Globals.txt", 'r') as file:
        variables = json.load(file)
    if variables["color"] != 0:
        UI.necro_color()
        print(Green_Blackxx, end='')
    else:
        UI.necro()
    print("\n")
    WordCore.word_corex("DEVELOPER |", "78 Alpha\n")
    print("\n")
    time.sleep(0.5)
    WordCore.word_corex("CONTINUE |", "Continue from previous save")
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
    if action == "CONTINUE":
        oalQuit()
        #ft.join()
        #ft.close()
        Level1.Save_Check()
    elif action == "NEW":
        oalQuit()
        #ft.join()
        #ft.close()
        load_3()
        Level1.Save_Check()
    elif action == "SETTINGS":
        settings()
        intro()
    elif action == "EXIT":
        Clear.clear()
        exit()
    else:
        intro()

Intro_Thread = threading.Thread(intro())

if __name__ == '__main__':
    ft.start()
    Intro_Thread.start()
    ft.join()
