import time, os, platform, sys, Clear, Level1, WordCore, UI, threading
from json_system import *
from ColorSplash import *
from Settings import *
#from Intro_Sounds import *

def intro(): #The intro to the game
    print(Reset, end='')
    Clear.clear()
    with open("Globals.txt", 'r') as file:
        variables = json.load(file)
    if variables["color"] != 0:
        UI.necro_color()
        print(Green_Blackxx, end='')
    else:
        UI.necro()
    print("\n")
    Music_Thread.start()
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
        #Music_Thread.join()
        #Music_Thraed.close()
        Level1.Save_Check()
    elif action == "NEW":
        #Music_Thread.join()
        #Music_Thraed.close()
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

#def Necro_Intro():
#    while True:
#        mixer.init()
#        #pygame.display.set_mode((0, 0))
#        mixer.music.load("Necro.mp3")
#        mixer.music.play(0)

#        clock = time.Clock()
#        clock.tick(10)
#        while mixer.music.get_busy():
#            #pygame.event.poll()
#            clock.tick(10)



#Music_Thread = threading.Thread(Necro_Intro())

Intro_Thread = threading.Thread(intro())


#intro()
#Music_Thread.start()
