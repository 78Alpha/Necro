import time, WordCore, UniData, Clear, ColorSplash

infected = UniData.infected
limit = UniData.limit
cure = UniData.cure
healthy = UniData.healthy
dead = UniData.dead
zombies = UniData.zombies
infectivity = UniData.infectivity
severity = UniData.severity
lethality = UniData.lethality
infectivity_limit = UniData.infectivity_limit
severity_limit = UniData.severity_limit
lethality_limit = UniData.lethality_limit

def inf_graph(): # Visuals for population infection
    infect = int((float(infected)/limit)*100)
    inf = "["
    for i in range(infect):  # Visual for infection
        inf += "|"
    for i in range(100-int(infect)):  # Visual for non-infected
        inf += "."
    inf2 = str(inf) + "] " + str(infect) + "% Infected"
    print("Population Infected")
    print(inf2)
    print("\n")
    WordCore.word_corex("Infected |", str(infected) + " People Infected")
    print("\n")
    time.sleep(1)

def color_inf_graph(): # Visuals for population infection
    infect = int((float(infected)/limit)*100)
    inf = "["
    for i in range(infect):  # Visual for infection
        inf += ColorSplash.Green_Square + "|" + ColorSplash.Reset
    for i in range(100-int(infect)):  # Visual for non-infected
        inf += ColorSplash.Red_Square + "." + ColorSplash.Reset
    inf2 = str(inf) + "] " + str(infect) + "% Infected"
    print("Population Infected")
    print(inf2)
    print("\n")
    WordCore.word_corex("Infected |", str(infected) + " People Infected")
    print("\n")
    time.sleep(1)

def color_inf_graph_mini():
    global limit
    global infected
    infect = int((float(infected)/limit) * 10)
    inf = "["
    inf_t = 0
    for i in range(infect):  # Visual for infection
        inf += ColorSplash.Green_Square + "|" + ColorSplash.Reset
        inf_t += 10
    for t in range(10-int(infect)):  # Visual for non-infected
        inf += ColorSplash.Red_Square + "." + ColorSplash.Reset
    inf2 = str(inf) + "] " + str(inf_t) + "% Infected"
    print(inf2)

def inf_graph_mini():
    global limit
    global infected
    infect = int((float(infected)/limit) * 10)
    inf = "["
    inf_t = 0
    for i in range(infect):  # Visual for infection
        inf += "|"
        inf_t += 10
    for t in range(10-int(infect)):  # Visual for non-infected
        inf += "."
    inf2 = str(inf) + "] " + str(inf_t) + "% Infected"
    print(inf2)

def cure_progress(): #notifies if the cure is a threat or not
    global cure_percent
    cure_percent = (float(cure)/1000) * 100
    cur_graph()
    if cure_percent < int(10):
        print("The cure is not yet a threat\n")
    elif cure_percent < int(25):
        print("The cure is becoming an annoyance\n")
    elif cure_percent < int(50):
        print("A threat ensues\n")
    elif cure_percent < int(75):
        print("The cure is a threat\n")
    elif cure_percent < int(90):
        print("The cure has become a severe threat\n")
    elif cure_percent < int(99):
        print("You are screwed\n")
    else:
        print("You will see this message if an uncorrectable error has occurred")
    time.sleep(1)

def cur_graph(): #Displays the percent of cure completion
    cur = "["
    global cure_percent
    curer = int(cure_percent)
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
    cur = "["
    global cure_percent
    curer = int(cure_percent)
    for i in range(curer):  # percent to completion
        cur += ColorSplash.Green_Square + "|" + ColorSplash.Reset
    for i in range(100-int(curer)):  # Distance from completion
        cur += ColorSplash.Red_Square + "." + ColorSplash.Reset
    cur2 = str(cur) + "] " + str(curer) + "% Complete"
    print("Cure Completion")
    print(cur2)
    print("\n")
    time.sleep(1)

def cur_graph_mini():
    cur = "["
    cur_t = 0
    global cure_percent
    cure_percent = (float(cure) / 1000) * 100
    curer = int(cure_percent / 10)
    for i in range(curer):  # percent to completion
        cur += "|"
        cur_t += 10
    for i in range(10 - int(curer)):  # Distance from completion
        cur += "."
    cur2 = str(cur) + "] " + str(cur_t) + "% Cure"
    print(cur2)

def color_cur_graph_mini():
    cur = "["
    cur_t = 0
    global cure_percent
    cure_percent = (float(cure) / 1000) * 100
    curer = int(cure_percent / 10)
    for i in range(curer):  # percent to completion
        cur += ColorSplash.Green_Square + "|" + ColorSplash.Reset
        cur_t += 10
    for i in range(10 - int(curer)):  # Distance from completion
        cur += ColorSplash.Red_Square + "." + ColorSplash.Reset
    cur2 = str(cur) + "] " + str(cur_t) + "% Cure"
    print(cur2)

def hea_graph(): # A graph for the amount of healthy people
    hea = "["
    alive2 = (float(healthy)/limit)
    if alive2 > .99:  #Quick fix for the "less than 100%" Bug
        alive2 = 1
    alive3 = int(alive2 * 100)
    for i in range(alive3):  # Amount healthy
        hea += "|"
    for i in range(100 - int(alive3)):  # Amount not healthy
        hea += "."
    cur2 = str(hea) + "] " + str(alive3) + "% Healthy"
    print("Healthy People")
    print(cur2)
    print("\n")
    WordCore.word_corex("Healthy |", str(UniData.healthy) + " People Healthy")
    print("\n")
    time.sleep(1)

def color_hea_graph(): # A graph for the amount of healthy people
    hea = "["
    alive2 = (float(healthy)/limit)
    if alive2 > .99:  #Quick fix for the "less than 100%" Bug
        alive2 = 1
    alive3 = int(alive2 * 100)
    for i in range(alive3):  # Amount healthy
        hea += ColorSplash.Green_Square + "|" + ColorSplash.Reset
    for i in range(100 - int(alive3)):  # Amount not healthy
        hea += ColorSplash.Red_Square + "." + ColorSplash.Reset
    cur2 = str(hea) + "] " + str(alive3) + "% Healthy"
    print("Healthy People")
    print(cur2)
    print("\n")
    WordCore.word_corex("Healthy |", str(UniData.healthy) + " People Healthy")
    print("\n")
    time.sleep(1)

def hea_graph_mini():
    hea = "["
    hea_t = 0
    alive2 = (float(healthy)/limit)
    if alive2 > .99:  #Quick fix for the "less than 100%" Bug
        alive2 = 1
    alive3 = int(alive2 * 10)
    for i in range(alive3):  # Amount healthy
        hea += "|"
        hea_t += 10
    for i in range(10 - int(alive3)):  # Amount not healthy
        hea += "."
    cur2 = str(hea) + "] " + str(hea_t) + "% Healthy"
    print(cur2)

def color_hea_graph_mini():
    hea = "["
    hea_t = 0
    alive2 = (float(healthy)/limit)
    if alive2 > .99:  #Quick fix for the "less than 100%" Bug
        alive2 = 1
    alive3 = int(alive2 * 10)
    for i in range(alive3):  # Amount healthy
        hea += ColorSplash.Green_Square + "|" + ColorSplash.Reset
        hea_t += 10
    for i in range(10 - int(alive3)):  # Amount not healthy
        hea += ColorSplash.Red_Square + "." + ColorSplash.Reset
    cur2 = str(hea) + "] " + str(hea_t) + "% Healthy"
    print(cur2)

def dea_graph():
    corpse = int((float(dead) / limit) * 100)
    dea = "["
    for i in range(corpse):  # Amount dead
        dea += "|"
    for i in range(100 - int(corpse)):  # Amount not dead
        dea += "."
    dea2 = str(dea) + "] " + str(corpse) + "% Dead"
    print("Population Dead")
    print(dea2)
    print("\n")
    WordCore.word_corex("Dead |", str(dead) + " People Dead")
    print("\n")
    time.sleep(1)

def color_dea_graph():
    corpse = int((float(dead) / limit) * 100)
    dea = "["
    for i in range(corpse):  # Amount dead
        dea += ColorSplash.Green_Square + "|" + ColorSplash.Reset
    for i in range(100 - int(corpse)):  # Amount not dead
        dea += ColorSplash.Red_Square + "." + ColorSplash.Reset
    dea2 = str(dea) + "] " + str(corpse) + "% Dead"
    print("Population Dead")
    print(dea2)
    print("\n")
    WordCore.word_corex("Dead |", str(dead) + " People Dead")
    print("\n")
    time.sleep(1)

def dea_graph_mini():
    corpse = int((float(dead) / limit) * 10)
    dea = "["
    dea_t = 0
    for i in range(corpse):  # Amount dead
        dea += "|"
        dea += 10
    for i in range(10 - int(corpse)):  # Amount not dead
        dea += "."
    dea2 = str(dea) + "] " + str(dea_t) + "% Dead"
    print(dea2)

def color_dea_graph_mini():
    corpse = int((float(dead) / limit) * 10)
    dea = "["
    dea_t = 0
    for i in range(corpse):  # Amount dead
        dea += ColorSplash.Green_Square + "|" + ColorSplash.Reset
        dea += 10
    for i in range(10 - int(corpse)):  # Amount not dead
        dea += ColorSplash.Red_Square + "." + ColorSplash.Reset
    dea2 = str(dea) + "] " + str(dea_t) + "% Dead"
    print(dea2)

def zom_graph(): # Graph of zombies
    walkers = int((float(UniData.zombies) / UniData.limit) * 100)
    zom = "["
    for i in range(walkers):  # Are zombs
        zom += "|"
    for i in range(100 - int(walkers)):  # Are not zombs
        zom += "."
    zom2 = str(zom) + "] " + str(walkers) + "% Zombies"
    print("Population Zombified")
    print(zom2)
    print("\n")
    WordCore.word_corex("Zombies |", str(UniData.zombies) + " People Zombified")
    print("\n")
    time.sleep(1)

def color_zom_graph(): # Graph of zombies
    walkers = int((float(UniData.zombies) / UniData.limit) * 100)
    zom = "["
    for i in range(walkers):  # Are zombs
        zom += ColorSplash.Green_Square + "|" + ColorSplash.Reset
    for i in range(100 - int(walkers)):  # Are not zombs
        zom += ColorSplash.Red_Square + "." + ColorSplash.Reset
    zom2 = str(zom) + "] " + str(walkers) + "% Zombies"
    print("Population Zombified")
    print(zom2)
    print("\n")
    WordCore.word_corex("Zombies |", str(UniData.zombies) + " People Zombified")
    print("\n")
    time.sleep(1)

def zom_graph_mini(): # Graph of zombies
    walkers = int((float(UniData.zombies) / UniData.limit) * 10)
    zom = "["
    zom_t = 0
    for i in range(walkers):  # Are zombs
        zom += "|"
        zom_t += 10
    for i in range(10 - int(walkers)):  # Are not zombs
        zom += "."
    zom2 = str(zom) + "] " + str(zom_t) + "% Zombies"
    print(zom2)

def color_zom_graph_mini(): # Graph of zombies
    walkers = int((float(UniData.zombies) / UniData.limit) * 10)
    zom = "["
    zom_t = 0
    for i in range(walkers):  # Are zombs
        zom += ColorSplash.Green_Square + "|" + ColorSplash.Reset
        zom_t += 10
    for i in range(10 - int(walkers)):  # Are not zombs
        zom += ColorSplash.Red_Square + "." + ColorSplash.Reset
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

def graphical_analysis_mini():
    inf_graph_mini()
    hea_graph_mini()
    dea_graph_mini()
    cur_graph_mini()
    plague_status_graph_mini()

def color_plague_status_graph(): # Displays all plague graphs
    tiv = "["
    sev = "["
    let = "["
    status = int((float(infectivity) / infectivity_limit) * 100)
    for i in range(status):
        tiv += ColorSplash.Green_Square + "|" + ColorSplash.Reset
    for i in range(100-int(status)):
        tiv += ColorSplash.Red_Square + "." + ColorSplash.Reset
    status2 = int((float(severity) / severity_limit) * 100)
    for i in range(status2):
        sev += ColorSplash.Green_Square + "|" + ColorSplash.Reset
    for i in range(100-int(status2)):
        sev += ColorSplash.Red_Square + "." + ColorSplash.Reset
    status3 = int((float(lethality) / lethality_limit) * 100)
    for i in range(status3):
        let += ColorSplash.Green_Square + "|" + ColorSplash.Reset
    for i in range(100-int(status3)):
        let += ColorSplash.Red_Square + "." + ColorSplash.Reset
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
    tiv = "["
    sev = "["
    let = "["
    status = int((float(infectivity) / infectivity_limit) * 100)
    for i in range(status):
        tiv += "|"
    for i in range(100-int(status)):
        tiv += "."
    status2 = int((float(severity) / severity_limit) * 100)
    for i in range(status2):
        sev += "|"
    for i in range(100-int(status2)):
        sev += "."
    status3 = int((float(lethality) / lethality_limit) * 100)
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
    tiv = "["
    tiv_t = 0
    sev = "["
    sev_t = 0
    let = "["
    let_t = 0
    status = int((float(infectivity) / infectivity_limit) * 10)
    for i in range(status):
        tiv += "|"
        tiv_t += 10
    for i in range(10-int(status)):
        tiv += "."
    status2 = int((float(severity) / severity_limit) * 10)
    for i in range(status2):
        sev += "|"
        sev += 10
    for i in range(10-int(status2)):
        sev += "."
    status3 = int((float(lethality) / lethality_limit) * 10)
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

def color_plague_status_graph_mini(): # Displays all plague graphs
    tiv = "["
    tiv_t = 0
    sev = "["
    sev_t = 0
    let = "["
    let_t = 0
    status = int((float(infectivity) / infectivity_limit) * 10)
    for i in range(status):
        tiv += ColorSplash.Green_Square + "|" + ColorSplash.Reset
        tiv_t += 10
    for i in range(10-int(status)):
        tiv += ColorSplash.Red_Square + "." + ColorSplash.Reset
    status2 = int((float(severity) / severity_limit) * 10)
    for i in range(status2):
        sev += ColorSplash.Green_Square + "|" + ColorSplash.Reset
        sev += 10
    for i in range(10-int(status2)):
        sev += ColorSplash.Red_Square + "." + ColorSplash.Reset
    status3 = int((float(lethality) / lethality_limit) * 10)
    for i in range(status3):
        let += ColorSplash.Green_Square + "|" + ColorSplash.Reset
        let_t += 10
    for i in range(10-int(status3)):
        let += ColorSplash.Red_Square + "." + ColorSplash.Reset
    infective = str(tiv) + "] " + str(tiv_t) + "% To Infectivity Max"
    severe = str(sev) + "] " + str(sev_t) + "% To Severity Max"
    lethal = str(let) + "] " + str(let_t) + "% To Lethality Max"
    print(infective)
    print(severe)
    print(lethal)

graphical_analysis_mini()