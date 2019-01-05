import os, platform

OS = platform.system()


def clear():
    if OS == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def delete():
    if OS == "Windows":
        os.system("del Save_file.py")
    else:
        os.system("rm Save_file.py")
