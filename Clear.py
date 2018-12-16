import os, platform

OS = platform.system()


def clear():
    if OS == "Windows":
        os.system("cls")
    else:
        os.system("clear")