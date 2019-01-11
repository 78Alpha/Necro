import json_system, json
#from Main import *
def settings():
    with open("Globals.txt", 'r') as f:
        variables = json.load(f)
    print("This feature is in [alpha], and may cause [Program Termination]")
    color_ = str(input("Enable color (Current value [" + str(variables["color"]) + "]): "))
    if color_ == "YES":
        variables["color"] = 1
        with open("Globals.txt", 'w') as f2:
            json.dump(variables, f2, indent=3)
        #intro()
    elif color_ == "NO":
        variables["color"] = 0
        with open("Globals.txt", 'w') as f2:
            json.dump(variables, f2, indent=3)
    else:
        settings()