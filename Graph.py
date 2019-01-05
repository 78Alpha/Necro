import time, WordCore, Clear, ColorSplash
from json_system import *

def inf_graph(): # Visuals for population infection
    with open("UniData.txt", 'r') as f:
        variables = json.load(f)
    infect = int((float(variables["infected"])/variables["limit"])*100)
    inf = "["
    for i in range(infect):  # Visual for infection
        inf += "|"
    for i in range(100-int(infect)):  # Visual for non-variables["infected"]
        inf += "."
    inf2 = str(inf) + "] " + str(infect) + "% Infected"
    print("Population Infected")
    print(inf2)
    print("\n")
    WordCore.word_corex("Infected |", str(variables["infected"]) + " People Infected")
    print("\n")
    time.sleep(1)

def color_inf_graph(): # Visuals for population infection
    with open("UniData.txt", 'r') as f:
        variables = json.load(f)
    infect = int((float(variables["infected"])/variables["limit"])*100)
    inf = "["
    for i in range(infect):  # Visual for infection
        inf += ColorSplash.Green_Squarexx + "|" + ColorSplash.Reset
    for i in range(100-int(infect)):  # Visual for non-variables["infected"]
        inf += ColorSplash.Red_Squarexxxx + "." + ColorSplash.Reset
    inf2 = str(inf) + "] " + str(infect) + "% Infected"
    print("Population Infected")
    print(inf2)
    print("\n")
    WordCore.word_corex("Infected |", str(variables["infected"]) + " People Infected")
    print("\n")
    time.sleep(1)

def color_inf_graph_mini():
    with open("UniData.txt", 'r') as f:
        variables = json.load(f)
    infect = int((float(variables["infected"])/variables["limit"]) * 10)
    inf = "["
    inf_t = 0
    for i in range(infect):  # Visual for infection
        inf += ColorSplash.Green_Squarexx + "|" + ColorSplash.Reset
        inf_t += 10
    for t in range(10-int(infect)):  # Visual for non-variables["infected"]
        inf += ColorSplash.Red_Squarexxxx + "." + ColorSplash.Reset
    inf2 = str(inf) + "] " + str(inf_t) + "% Infected"
    print(inf2)

def inf_graph_mini():
    with open("UniData.txt", 'r') as f:
        variables = json.load(f)
    infect = int((float(variables["infected"])/variables["limit"]) * 10)
    inf = "["
    inf_t = 0
    for i in range(infect):  # Visual for infection
        inf += "|"
        inf_t += 10
    for t in range(10-int(infect)):  # Visual for non-variables["infected"]
        inf += "."
    inf2 = str(inf) + "] " + str(inf_t) + "% Infected"
    print(inf2)

def cure_progress(): #notifies if the cure is a threat or not
    with open("UniData.txt", 'r') as f:
        variables = json.load(f)
    variables["cure_percent"] = (float(variables["cure"])/1000) * 100
    cur_graph()
    if variables["cure_percent"] < int(10):
        print("The cure is not yet a threat\n")
    elif variables["cure_percent"] < int(25):
        print("The cure is becoming an annoyance\n")
    elif variables["cure_percent"] < int(50):
        print("A threat ensues\n")
    elif variables["cure_percent"] < int(75):
        print("The cure is a threat\n")
    elif variables["cure_percent"] < int(90):
        print("The cure has become a severe threat\n")
    elif variables["cure_percent"] < int(99):
        print("You are screwed\n")
    else:
        print("You will see this message if an uncorrectable error has occurred")
    time.sleep(1)

def color_cure_progress(): #notifies if the cure is a threat or not
    with open("UniData.txt", 'r') as f:
        variables = json.load(f)
    variables["cure_percent"] = (float(variables["cure"])/1000) * 100
    color_cur_graph()
    print(ColorSplash.Green_Blackxx)
    if variables["cure_percent"] < int(10):
        print("The cure is not yet a threat\n")
    elif variables["cure_percent"] < int(25):
        print("The cure is becoming an annoyance\n")
    elif variables["cure_percent"] < int(50):
        print("A threat ensues\n")
    elif variables["cure_percent"] < int(75):
        print("The cure is a threat\n")
    elif variables["cure_percent"] < int(90):
        print("The cure has become a severe threat\n")
    elif variables["cure_percent"] < int(99):
        print("You are screwed\n")
    else:
        print("You will see this message if an uncorrectable error has occurred")
    print(ColorSplash.Reset)
    time.sleep(1)

def cur_graph(): #Displays the percent of cure completion
    with open("UniData.txt", 'r') as f:
        variables = json.load(f)
    cur = "["
    curer = int(variables["cure_percent"])
    for i in range(curer):  # percent to completion
        cur += "|"
    for i in range(100-int(curer)):  # Distance from completion
        cur += "."
    cur2 = str(cur) + "] " + str(curer) + "% Complete"
    print("Cure Completion")
    print(cur2)
    print("\n")
    time.sleep(1)

def color_cur_graph(): #Displays the percent of cure completion
    with open("UniData.txt", 'r') as f:
        variables = json.load(f)
    cur = "["
    curer = int(variables["cure_percent"])
    for i in range(curer):  # percent to completion
        cur += ColorSplash.Green_Squarexx + "|" + ColorSplash.Reset
    for i in range(100-int(curer)):  # Distance from completion
        cur += ColorSplash.Red_Squarexxxx + "." + ColorSplash.Reset
    cur2 = str(cur) + "] " + str(curer) + "% Complete"
    print("Cure Completion")
    print(cur2)
    print("\n")
    time.sleep(1)

def cur_graph_mini():
    with open("UniData.txt", 'r') as f:
        variables = json.load(f)
    cur = "["
    cur_t = 0
    variables["cure_percent"] = (float(variables["cure"]) / 1000) * 100
    curer = int(variables["cure_percent"] / 10)
    for i in range(curer):  # percent to completion
        cur += "|"
        cur_t += 10
    for i in range(10 - int(curer)):  # Distance from completion
        cur += "."
    cur2 = str(cur) + "] " + str(cur_t) + "% Cure"
    print(cur2)

def color_cur_graph_mini():
    with open("UniData.txt", 'r') as f:
        variables = json.load(f)
    cur = "["
    cur_t = 0
    variables["cure_percent"] = (float(variables["cure"]) / 1000) * 100
    curer = int(cure_percent / 10)
    for i in range(curer):  # percent to completion
        cur += ColorSplash.Green_Squarexx + "|" + ColorSplash.Reset
        cur_t += 10
    for i in range(10 - int(curer)):  # Distance from completion
        cur += ColorSplash.Red_Squarexxxx + "." + ColorSplash.Reset
    cur2 = str(cur) + "] " + str(cur_t) + "% Cure"
    print(cur2)

def hea_graph(): # A graph for the amount of variables["healthy"] people
    with open("UniData.txt", 'r') as f:
        variables = json.load(f)
    hea = "["
    alive2 = (float(variables["healthy"])/variables["limit"])
    if alive2 > .99:  #Quick fix for the "less than 100%" Bug
        alive2 = 1
    alive3 = int(alive2 * 100)
    for i in range(alive3):  # Amount variables["healthy"]
        hea += "|"
    for i in range(100 - int(alive3)):  # Amount not variables["healthy"]
        hea += "."
    cur2 = str(hea) + "] " + str(alive3) + "% Healthy"
    print("Healthy People")
    print(cur2)
    print("\n")
    WordCore.word_corex("Healthy |", str(variables["healthy"]) + " People Healthy")
    print("\n")
    time.sleep(1)

def color_hea_graph(): # A graph for the amount of variables["healthy"] people
    with open("UniData.txt", 'r') as f:
        variables = json.load(f)
    hea = "["
    alive2 = (float(variables["healthy"])/variables["limit"])
    if alive2 > .99:  #Quick fix for the "less than 100%" Bug
        alive2 = 1
    alive3 = int(alive2 * 100)
    for i in range(alive3):  # Amount variables["healthy"]
        hea += ColorSplash.Green_Squarexx + "|" + ColorSplash.Reset
    for i in range(100 - int(alive3)):  # Amount not variables["healthy"]
        hea += ColorSplash.Red_Squarexxxx + "." + ColorSplash.Reset
    cur2 = str(hea) + "] " + str(alive3) + "% Healthy"
    print("Healthy People")
    print(cur2)
    print("\n")
    WordCore.word_corex("Healthy |", str(variables["healthy"]) + " People Healthy")
    print("\n")
    time.sleep(1)

def hea_graph_mini():
    with open("UniData.txt", 'r') as f:
        variables = json.load(f)
    hea = "["
    hea_t = 0
    alive2 = (float(variables["healthy"])/variables["limit"])
    if alive2 > .99:  #Quick fix for the "less than 100%" Bug
        alive2 = 1
    alive3 = int(alive2 * 10)
    for i in range(alive3):  # Amount variables["healthy"]
        hea += "|"
        hea_t += 10
    for i in range(10 - int(alive3)):  # Amount not variables["healthy"]
        hea += "."
    cur2 = str(hea) + "] " + str(hea_t) + "% Healthy"
    print(cur2)

def color_hea_graph_mini():
    with open("UniData.txt", 'r') as f:
        variables = json.load(f)
    hea = "["
    hea_t = 0
    alive2 = (float(variables["healthy"])/variables["limit"])
    if alive2 > .99:  #Quick fix for the "less than 100%" Bug
        alive2 = 1
    alive3 = int(alive2 * 10)
    for i in range(alive3):  # Amount variables["healthy"]
        hea += ColorSplash.Green_Squarexx + "|" + ColorSplash.Reset
        hea_t += 10
    for i in range(10 - int(alive3)):  # Amount not variables["healthy"]
        hea += ColorSplash.Red_Squarexxxx + "." + ColorSplash.Reset
    cur2 = str(hea) + "] " + str(hea_t) + "% Healthy"
    print(cur2)

def dea_graph():
    with open("UniData.txt", 'r') as f:
        variables = json.load(f)
    corpse = int((float(variables["dead"]) / variables["limit"]) * 100)
    dea = "["
    for i in range(corpse):  # Amount variables["dead"]
        dea += "|"
    for i in range(100 - int(corpse)):  # Amount not variables["dead"]
        dea += "."
    dea2 = str(dea) + "] " + str(corpse) + "% Dead"
    print("Population Dead")
    print(dea2)
    print("\n")
    WordCore.word_corex("Dead |", str(variables["dead"]) + " People Dead")
    print("\n")
    time.sleep(1)

def color_dea_graph():
    with open("UniData.txt", 'r') as f:
        variables = json.load(f)
    corpse = int((float(variables["dead"]) / variables["limit"]) * 100)
    dea = "["
    for i in range(corpse):  # Amount variables["dead"]
        dea += ColorSplash.Green_Squarexx + "|" + ColorSplash.Reset
    for i in range(100 - int(corpse)):  # Amount not variables["dead"]
        dea += ColorSplash.Red_Squarexxxx + "." + ColorSplash.Reset
    dea2 = str(dea) + "] " + str(corpse) + "% Dead"
    print("Population Dead")
    print(dea2)
    print("\n")
    WordCore.word_corex("Dead |", str(variables["dead"]) + " People Dead")
    print("\n")
    time.sleep(1)

def dea_graph_mini():
    with open("UniData.txt", 'r') as f:
        variables = json.load(f)
    corpse = int((float(variables["dead"]) / variables["limit"]) * 10)
    dea = "["
    dea_t = 0
    for i in range(corpse):  # Amount variables["dead"]
        dea += "|"
        dea += 10
    for i in range(10 - int(corpse)):  # Amount not variables["dead"]
        dea += "."
    dea2 = str(dea) + "] " + str(dea_t) + "% Dead"
    print(dea2)

def color_dea_graph_mini():
    with open("UniData.txt", 'r') as f:
        variables = json.load(f)
    corpse = int((float(variables["dead"]) / variables["limit"]) * 10)
    dea = "["
    dea_t = 0
    for i in range(corpse):  # Amount variables["dead"]
        dea += ColorSplash.Green_Squarexx + "|" + ColorSplash.Reset
        dea += 10
    for i in range(10 - int(corpse)):  # Amount not variables["dead"]
        dea += ColorSplash.Red_Squarexxxx + "." + ColorSplash.Reset
    dea2 = str(dea) + "] " + str(dea_t) + "% Dead"
    print(dea2)

def zom_graph(): # Graph of variables["variables["zombies"]"]
    with open("UniData.txt", 'r') as f:
        variables = json.load(f)
    walkers = int((float(variables["zombies"]) / variables["limit"]) * 100)
    zom = "["
    for i in range(walkers):  # Are zombs
        zom += "|"
    for i in range(100 - int(walkers)):  # Are not zombs
        zom += "."
    zom2 = str(zom) + "] " + str(walkers) + "% Zombies"
    print("Population Zombified")
    print(zom2)
    print("\n")
    WordCore.word_corex("Zombies |", str(variables["zombies"]) + " People Zombified")
    print("\n")
    time.sleep(1)

def color_zom_graph(): # Graph of variables["zombies"]
    with open("UniData.txt", 'r') as f:
        variables = json.load(f)
    walkers = int((float(variables["zombies"]) / variables["limit"]) * 100)
    zom = "["
    for i in range(walkers):  # Are zombs
        zom += ColorSplash.Green_Squarexx + "|" + ColorSplash.Reset
    for i in range(100 - int(walkers)):  # Are not zombs
        zom += ColorSplash.Red_Squarexxxx + "." + ColorSplash.Reset
    zom2 = str(zom) + "] " + str(walkers) + "% Zombies"
    print("Population Zombified")
    print(zom2)
    print("\n")
    WordCore.word_corex("Zombies |", str(variables["zombies"]) + " People Zombified")
    print("\n")
    time.sleep(1)

def zom_graph_mini(): # Graph of variables["zombies"]
    with open("UniData.txt", 'r') as f:
        variables = json.load(f)
    walkers = int((float(variables["zombies"]) / variables["limit"]) * 10)
    zom = "["
    zom_t = 0
    for i in range(walkers):  # Are zombs
        zom += "|"
        zom_t += 10
    for i in range(10 - int(walkers)):  # Are not zombs
        zom += "."
    zom2 = str(zom) + "] " + str(zom_t) + "% Zombies"
    print(zom2)

def color_zom_graph_mini(): # Graph of variables["zombies"]
    with open("UniData.txt", 'r') as f:
        variables = json.load(f)
    walkers = int((float(variables["zombies"]) / variables["limit"]) * 10)
    zom = "["
    zom_t = 0
    for i in range(walkers):  # Are zombs
        zom += ColorSplash.Green_Squarexx + "|" + ColorSplash.Reset
        zom_t += 10
    for i in range(10 - int(walkers)):  # Are not zombs
        zom += ColorSplash.Red_Squarexxxx + "." + ColorSplash.Reset
    zom2 = str(zom) + "] " + str(zom_t) + "% Zombies"
    print(zom2)

def graphical_analysis(): # Displays all world graphs
    inf_graph()
    hea_graph()
    dea_graph()
    zom_graph()
    cure_progress()
    print("\n")
    input(str("Press ENTER to continue..."))

def color_graphical_analysis(): # Displays all world graphs
    color_inf_graph()
    color_hea_graph()
    color_dea_graph()
    color_zom_graph()
    color_cure_progress()
    print("\n")
    input(str("Press ENTER to continue..."))

def graphical_analysis_mini():
    with open("UniData.txt", 'r') as f:
        variables = json.load(f)
    inf_graph_mini()
    hea_graph_mini()
    dea_graph_mini()
    cur_graph_mini()
    plague_status_graph_mini()

def color_plague_status_graph(): # Displays all plague graphs
    with open("UniData.txt", 'r') as f:
        variables = json.load(f)
    tiv = "["
    sev = "["
    let = "["
    status = int((float(variables["infectivity"]) / variables["infectivity_limit"]) * 100)
    for i in range(status):
        tiv += ColorSplash.Green_Squarexx + "|" + ColorSplash.Reset
    for i in range(100-int(status)):
        tiv += ColorSplash.Red_Squarexxxx + "." + ColorSplash.Reset
    status2 = int((float(variables["severity"]) / variables["severity_limit"]) * 100)
    for i in range(status2):
        sev += ColorSplash.Green_Squarexx + "|" + ColorSplash.Reset
    for i in range(100-int(status2)):
        sev += ColorSplash.Red_Squarexxxx + "." + ColorSplash.Reset
    status3 = int((float(variables["lethality"]) / variables["lethality_limit"]) * 100)
    for i in range(status3):
        let += ColorSplash.Green_Squarexx + "|" + ColorSplash.Reset
    for i in range(100-int(status3)):
        let += ColorSplash.Red_Squarexxxx + "." + ColorSplash.Reset
    infective = str(tiv) + "] " + str(status) + "% To Infectivity Max"
    severe = str(sev) + "] " + str(status2) + "% To Severity Max"
    lethal = str(let) + "] " + str(status3) + "% To Lethality Max"
    print("Infectivity Level")
    print(infective)
    print("\n")
    time.sleep(1)
    print("Severity Level")
    print(severe)
    print("\n")
    time.sleep(1)
    print("Lethality Level")
    print(lethal)
    print("\n")
    time.sleep(1)
    input(str("Press ENTER to continue..."))


def plague_status_graph(): # Displays all plague graphs
    with open("UniData.txt", 'r') as f:
        variables = json.load(f)
    tiv = "["
    sev = "["
    let = "["
    status = int((float(variables["infectivity"]) / variables["infectivity_limit"]) * 100)
    for i in range(status):
        tiv += "|"
    for i in range(100-int(status)):
        tiv += "."
    status2 = int((float(variables["severity"]) / variables["severity_limit"]) * 100)
    for i in range(status2):
        sev += "|"
    for i in range(100-int(status2)):
        sev += "."
    status3 = int((float(variables["lethality"]) / variables["lethality_limit"]) * 100)
    for i in range(status3):
        let += "|"
    for i in range(100-int(status3)):
        let += "."
    infective = str(tiv) + "] " + str(status) + "% To Infectivity Max"
    severe = str(sev) + "] " + str(status2) + "% To Severity Max"
    lethal = str(let) + "] " + str(status3) + "% To Lethality Max"
    print("Infectivity Level")
    print(infective)
    print("\n")
    time.sleep(1)
    print("Severity Level")
    print(severe)
    print("\n")
    time.sleep(1)
    print("Lethality Level")
    print(lethal)
    print("\n")
    time.sleep(1)
    input(str("Press ENTER to continue..."))

def plague_status_graph_mini(): # Displays all plague graphs
    with open("UniData.txt", 'r') as f:
        variables = json.load(f)
    tiv = "["
    tiv_t = 0
    sev = "["
    sev_t = 0
    let = "["
    let_t = 0
    status = int((float(variables["infectivity"]) / variables["infectivity_limit"]) * 10)
    for i in range(status):
        tiv += "|"
        tiv_t += 10
    for i in range(10-int(status)):
        tiv += "."
    status2 = int((float(variables["severity"]) / variables["severity_limit"]) * 10)
    for i in range(status2):
        sev += "|"
        sev += 10
    for i in range(10-int(status2)):
        sev += "."
    status3 = int((float(variables["lethality"]) / variables["lethality_limit"]) * 10)
    for i in range(status3):
        let += "|"
        let_t += 10
    for i in range(10-int(status3)):
        let += "."
    infective = str(tiv) + "] " + str(tiv_t) + "% To Infectivity Max"
    severe = str(sev) + "] " + str(sev_t) + "% To Severity Max"
    lethal = str(let) + "] " + str(let_t) + "% To Lethality Max"
    print(infective)
    print(severe)
    print(lethal)
    time.sleep(1)
    input(str("Press ENTER to continue..."))

def color_plague_status_graph_mini(): # Displays all plague graphs
    with open("UniData.txt", 'r') as f:
        variables = json.load(f)
    tiv = "["
    tiv_t = 0
    sev = "["
    sev_t = 0
    let = "["
    let_t = 0
    status = int((float(variables["infectivity"]) / variables["infectivity_limit"]) * 10)
    for i in range(status):
        tiv += ColorSplash.Green_Squarexx + "|" + ColorSplash.Reset
        tiv_t += 10
    for i in range(10-int(status)):
        tiv += ColorSplash.Red_Squarexxxx + "." + ColorSplash.Reset
    status2 = int((float(variables["severity"]) / variables["severity_limit"]) * 10)
    for i in range(status2):
        sev += ColorSplash.Green_Squarexx + "|" + ColorSplash.Reset
        sev += 10
    for i in range(10-int(status2)):
        sev += ColorSplash.Red_Squarexxxx + "." + ColorSplash.Reset
    status3 = int((float(variables["lethality"]) / variables["lethality_limit"]) * 10)
    for i in range(status3):
        let += ColorSplash.Green_Squarexx + "|" + ColorSplash.Reset
        let_t += 10
    for i in range(10-int(status3)):
        let += ColorSplash.Red_Squarexxxx + "." + ColorSplash.Reset
    infective = str(tiv) + "] " + str(tiv_t) + "% To Infectivity Max"
    severe = str(sev) + "] " + str(sev_t) + "% To Severity Max"
    lethal = str(let) + "] " + str(let_t) + "% To Lethality Max"
    print(infective)
    print(severe)
    print(lethal)
    time.sleep(1)
    input(str("Press ENTER to continue..."))

#color_plague_status_graph()