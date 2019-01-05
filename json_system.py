import json

def load_1():
    with open("Save.txt", 'r') as f:
        variables = json.load(f)
    with open("UniData.txt", 'w') as f2:
        json.dumps(variables, f2, indent=3)

def load_3():
    with open("Globals.txt", 'r') as f:
        data = json.load(f)
    with open("UniData.txt", 'w') as f2:
        json.dump(data, f2, indent=3)

def save_1():
    with open("UniData.txt", 'r') as f:
        variables = json.load(f)
    with open("Save.txt", 'w') as f2:
        json.dump(variables, f2, indent=3)

def Read_val():
    with open("UniData.txt", 'r') as f:
        variables = json.load(f)

def Write_val():
    with open("UniData", 'w') as f2:
        json.dump(variables, f2, indent=3)

