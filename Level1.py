from __future__ import print_function
import Globals
import os, platform, time, random, gc, sys, threading

# Operating system

OS = platform.system()

#import parameters from a Globals.py file, allows for user customization of experience

zombies = Globals.zombies
dead = Globals.dead
healthy = Globals.healthy
infected = Globals.infected
week = Globals.week
cure = Globals.cure
influence = Globals.influence
infectivity = Globals.infectivity
infectivity_limit = Globals.infectivity_limit
severity = Globals.severity
severity_limit = Globals.severity_limit
lethality = Globals.lethality
lethality_limit = Globals.lethality_limit
weekly_infections = Globals.weekly_infections
dna_points = Globals.dna_points
burst = Globals.burst
burst_price = Globals.burst_price
necrosis = Globals.necrosis
necrosis_price = Globals.necrosis_price
water = Globals.water
water_price = Globals.water_price
air = Globals.air
air_price = Globals.air_price
blood = Globals.blood
blood_price = Globals.blood_price
saliva = Globals.saliva
saliva_price = Globals.saliva_price
zombify = Globals.zombify
zombify_price = Globals.zombify_price
rise = Globals.rise
rise_price = Globals.rise_price
gene = Globals.gene
limit = Globals.limit

def spinning_cursor():
    while True:
        for cursor in '|/-\\':
            yield cursor

def cursor():
    spinner = spinning_cursor()
    for _ in range(5):
        sys.stdout.write(next(spinner))
        sys.stdout.flush()
        time.sleep(0.1)
        sys.stdout.write('\b')

def word_core(sen, sec): # Human-like typing
    for letter in sen:
        print(letter, end='')
        sys.stdout.flush()  # Needed for Unix based systems
        time.sleep(sec)

def word_corex(stub, sen): # Human-like with a stationary starter
    print(stub + " ", end='')
    sys.stdout.flush()  # Needed for Unix based systems
    time.sleep(0.5)
    for letter in sen:
        print(letter, end='')
        sys.stdout.flush()  # Needed for Unix based systems
        time.sleep(.01)

def word_corez(sen): # Human-like typing
    for letter in sen:
        print(letter, end='')
        sys.stdout.flush()  # Needed for Unix based systems
        time.sleep(0)

def loading(stub,sub, sen, stubs):
    print(stub, end='')
    sys.stdout.flush()  # Needed for Unix based systems
    for letter in sub:
        print(letter, end='')
        sys.stdout.flush()
        time.sleep(0.1)
    for letter in sen:
        print(letter, end='')
        sys.stdout.flush()
        cursor()
        time.sleep(.01)
    print(stubs, end='')

def word_corey(stub, sen, stubs): # Stationary title with a natural typing statement, needs to be 89 characters
    marker = 0
    print(stub, end='')
    marker += int(len(stub))
    sys.stdout.flush()  # Needed for Unix based systems
    time.sleep(0.3)
    for letter in sen:
        print(letter, end='')
        sys.stdout.flush()  # Needed for Unix based systems
        marker += 1
        time.sleep(.01)
    while marker != 97:
        marker += 1
        print(" ", end='')
    print(stubs, end='')

def check_cure_start(): #determines if cure research should start or not
    global severity
    global week
    if severity >= 5:
        cure_value()
    elif week >= 20:
        cure_value()
    else:
        return

def cure_value(): # How fast the cure will increase
    global cure
    cure += 5
    global infected
    global severity
    global lethality
    cure_attack_value = float(infected)/healthy
    if cure_attack_value > 0.5:  # Determines how fast the cure will progress due to "fear"
        cure += int(float(cure) / 5)
        if severity >= 30:
            cure += (1 + int(float(severity) / lethality))
            threat = int(float(zombies) / limit) * 100
            if threat >= 33:
                cure += int(float(zombies) / limit) * 10
    else:
        return

def dna_weekly(): # Weekly supply of DNA for research, used for LAB purchases
    global dna_points
    dna_points += int(float(infected)/(1 + (healthy * 100)))
    dna_random()
    print("Research Points: " + str(dna_points))

def dna_random(): # Random DNA per week, can determine victory or defeat
    global dna_points
    rand_value1 = random.randint(0, 10)
    if rand_value1 > 4:
        random_dna = random.randint(0, 3)
        dna_points += int(random_dna)
    else:
        return

def infecting_agent(): # Determines how many infections occur
    global infected
    infected += 100
    global infectivity
    global lethality
    LETH = lethality
    inf_value = float(infectivity)/(1 + LETH) # Must be kept as int() + lethality, inflates lethality otherwise
    infected += int(inf_value)
    global healthy
    healthy -= 100
    healthy -= int(inf_value)

def inf_graph(): # Visuals for population infection
    global infected
    global healthy
    global limit
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
    word_corex("Infected |", str(infected) + " People Infected")
    print("\n")
    time.sleep(1)

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

def hea_graph(): # A graph for the amount of healthy people
    hea = "["
    global healthy
    global limit
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
    word_corex("Healthy |", str(healthy) + " People Healthy")
    print("\n")
    time.sleep(1)

def dea_graph():
    global dead
    global limit
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
    word_corex("Dead |", str(dead) + " People Dead")
    print("\n")
    time.sleep(1)

def zom_graph(): # Graph of zombies
    global zombies
    global limit
    walkers = int((float(zombies) / limit) * 100)
    zom = "["
    for i in range(walkers):  # Are zombs
        zom += "|"
    for i in range(100 - int(walkers)):  # Are not zombs
        zom += "."
    zom2 = str(zom) + "] " + str(walkers) + "% Zombies"
    print("Population Zombified")
    print(zom2)
    print("\n")
    word_corex("Zombies |", str(zombies) + " People Zombified")
    print("\n")
    time.sleep(1)

def graphical_analysis(): # Displays all world graphs
    inf_graph()
    hea_graph()
    dea_graph()
    zom_graph()
    cure_progress()
    print("\n")
    input(str("Press ENTER to continue..."))
    clear()
    player_menu()

def plague_status_graph(): # Displays all plague graphs
    global infectivity
    global severity
    global lethality
    global severity_limit
    global lethality_limit
    global infectivity_limit
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
    clear()
    player_menu()

def enforce_value_maximums(): #Makes sure that maximum/minumum values are never violated
    global infectivity
    global dead
    global severity
    global lethality
    global infected
    global healthy
    global zombies
    global infectivity_limit
    global severity_limit
    global lethality_limit
    global limit
    if lethality > lethality_limit:
        lethality = lethality_limit
    if lethality < 0:
        lethality = 0
    if infectivity > infectivity_limit: # Max value of infectivity
        infectivity = infectivity_limit
    if infectivity < 0: # Minimum level of infectivity
        infectivity = 0
    if severity > severity_limit: # Max value of severity
        severity = severity_limit
    if severity < 0: # Minimum level of severity
        severity = 0
    if infected > limit: # Max number of infected
        infected = limit
    if infected < 0: # Minimum number of infected
        infected = 0
    if healthy < 0: # Minimum level of healthy
        healthy = 0
    if healthy > limit: # Maximum number of healthy
        healthy = limit
    if dead > limit: # Max number of dead
        dead = limit
    if dead < 0: # Minimum number of dead
        dead = 0
    if zombies > limit: # Max number of zombies
        zombies = limit
    if zombies < 0: # Minimum number of zombies
        zombies = 0

def BURST_store_price(): # Changes burst store price depending on level
    global burst
    global burst_price
    if burst == 1:
        burst_price = "--"
    else:
        return

def BURST_check(): #chekcs if burst is active and applies it every turn
    global burst
    if burst == 1:
        global infectivity
        global infected
        global temp
        temp = int(infected * 0.01)
        global dead
        if temp < 1:
            temp = 1
            infectivity += temp
            infected -= temp
            dead += temp
        else:
            infectivity += temp
            infected -= temp
            dead += temp
    else:
        return

def BURST_info(): #displays info about burst
    word_corey("@@@@", "@@@@@@@@@@@@@@@@@@@@@@@@@@@", "@@@@\n")
    word_corey("@@@@", "@       ;#       .@       @", "@@@@\n")
    word_corey("@@@@", "@       `@@     @@@       @", "@@@@\n")
    word_corey("@@@@", "@        @@@@@@@@@+       @", "@@@@\n")
    word_corey("@@@@", "@       .@  @@@, #@       @", "@@@@\n")
    word_corey("@@@@", "@       @@   @   @@`      @", "@@@@\n")
    word_corey("@@@@", "@      +@@       @`@      @", "@@@@\n")
    word_corey("@@@@", "@      @@@       @@@:     @", "@@@@\n")
    word_corey("@@@@", "@    `@@;         `@@;    @", "@@@@\n")
    word_corey("@@@@", "@  ;@@@             @@@#  @", "@@@@\n")
    word_corey("@@@@", "@    @@#           ,@@.   @", "@@@@\n")
    word_corey("@@@@", "@     `@@@       +@@@     @", "@@@@\n")
    word_corey("@@@@", "@      @;@       @ @      @", "@@@@\n")
    word_corey("@@@@", "@       @@   `   @@;      @", "@@@@\n")
    word_corey("@@@@", "@       +@  +@@  @@       @", "@@@@\n")
    word_corey("@@@@", "@        @.@@.+@:@+       @", "@@@@\n")
    word_corey("@@@@", "@        @@@@@@@@@@       @", "@@@@\n")
    word_corey("@@@@", "@       ,@       @@       @", "@@@@\n")
    word_corey("@@@@", "@       +         :       @", "@@@@\n")
    word_corey("@@@@", "@@@@@@@@@@@@@@@@@@@@@@@@@@@", "@@@@\n")
    word_corey("@@@@", "", "@@@@\n")
    word_corey("@@@@  ", "<<" + gene[0] + ">>", "@@@@\n")
    word_corey("@@@@", "  Nano-Virus disables pressure regulation of host skull, following up with a forced intake","@@@@\n")
    word_corey("@@@@", "  of pressurized oxygen until cranial rupture/explosion occurrs", "@@@@\n")
    word_corey("@@@@", "", "@@@@\n")
    word_corey("@@@@  Affects: ", influence[0] + ", " + influence[1] + ", " + influence[2], "@@@@\n")
    word_corez("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")
    word_corez("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")

def NECROSIS_store_price(): #checks to see if it can be bought/alters price
    global necrosis
    global necrosis_price
    if necrosis == 1:
        necrosis_price = "--"
    else:
        return

def NECROSIS_check(): #chekcs if necrosis is active, will be run weekly to continue the rise on infectivity
    global necrosis
    if necrosis == 1:
        global infectivity
        global dead
        global healthy
        infectivity += int(float(dead)/(1 + healthy))
    else:
        return

def NECROSIS_info(): #Displays info about necrosis
    word_corey("@@@@", "@@@@@@@@@@@@@@@@@@@@@@@@@@@", "@@@@\n")
    word_corey("@@@@", "@                         @", "@@@@\n")
    word_corey("@@@@", "@    @@@           @@@    @", "@@@@\n")
    word_corey("@@@@", "@   @. @'         @. @'   @", "@@@@\n")
    word_corey("@@@@", "@   @  .@         @  .@   @", "@@@@\n")
    word_corey("@@@@", "@   @@.@.         @@.@.   @", "@@@@\n")
    word_corey("@@@@", "@    '@.           '@.    @", "@@@@\n")
    word_corey("@@@@", "@                         @", "@@@@\n")
    word_corey("@@@@", "@   `                '    @", "@@@@\n")
    word_corey("@@@@", "@    @              '`    @", "@@@@\n")
    word_corey("@@@@", "@     @`           '@     @", "@@@@\n")
    word_corey("@@@@", "@     ,@@         @@      @", "@@@@\n")
    word_corey("@@@@", "@      @@@@     +@@;      @", "@@@@\n")
    word_corey("@@@@", "@       @@,@@@@@:@@       @", "@@@@\n")
    word_corey("@@@@", "@        +@`    @@        @", "@@@@\n")
    word_corey("@@@@", "@          @@@@@.         @", "@@@@\n")
    word_corey("@@@@", "@@@@@@@@@@@@@@@@@@@@@@@@@@@", "@@@@\n")
    word_corey("@@@@", "", "@@@@\n")
    word_corey("@@@@  ", "<<" + gene[1] + ">>", "@@@@\n")
    word_corey("@@@@", "  Nano-virus enters a low power state while in a dead host, power is diverted to motion","@@@@\n")
    word_corey("@@@@", "  sensors such that individuals within proximity will be attacked before reaction is possible", "@@@@\n")
    word_corey("@@@@", "", "@@@@\n")
    word_corey("@@@@  Affects: ", influence[0] + ", " + influence[1], "@@@@\n")
    word_corez("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")
    word_corez("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")

def WATER_store_price(): # Changes store price of water gene
    global water
    global water_price
    if water == 1:
        water_price += int(float(water_price) / 4)
    elif water == 2:
        water_price += int(float(water_price) / 2)
    elif water == 3:
        water_price = '--'
    else:
        return

def WATER_check(): #chekcs if water is active, will be run when bought
    global water
    global infectivity
    global healthy
    if water == 1:
        infectivity += int(healthy * 0.05)
    elif water == 2:
        infectivity += int(healthy * 0.1)
    elif water == 3:
        infectivity += int(healthy * 0.2)
    else:
        return

def WATER_info(): #Displays info about water
    word_corey("@@@@", "@@@@@@@@@@@@@@@@@@@@@@@@@@@", "@@@@\n")
    word_corey("@@@@", "@                         @", "@@@@\n")
    word_corey("@@@@", "@        @+               @", "@@@@\n")
    word_corey("@@@@", "@         @@              @", "@@@@\n")
    word_corey("@@@@", "@         '@@             @", "@@@@\n")
    word_corey("@@@@", "@          @+@            @", "@@@@\n")
    word_corey("@@@@", "@          @ @.           @", "@@@@\n")
    word_corey("@@@@", "@          @  @           @", "@@@@\n")
    word_corey("@@@@", "@          @  ;@          @", "@@@@\n")
    word_corey("@@@@", "@          @   @`         @", "@@@@\n")
    word_corey("@@@@", "@          @    @         @", "@@@@\n")
    word_corey("@@@@", "@         ++    @         @", "@@@@\n")
    word_corey("@@@@", "@         @     @`        @", "@@@@\n")
    word_corey("@@@@", "@        ,# @@@ ;;        @", "@@@@\n")
    word_corey("@@@@", "@        @  @ @ ;;        @", "@@@@\n")
    word_corey("@@@@", "@        @  @ @ +,        @", "@@@@\n")
    word_corey("@@@@", "@        @  ,@@ @         @", "@@@@\n")
    word_corey("@@@@", "@        #+    .@         @", "@@@@\n")
    word_corey("@@@@", "@         @@@@@@          @", "@@@@\n")
    word_corey("@@@@", "@@@@@@@@@@@@@@@@@@@@@@@@@@@", "@@@@\n")
    word_corey("@@@@", "", "@@@@\n")
    word_corey("@@@@  ", "<<" + gene[2] + ">>", "@@@@\n")
    word_corey("@@@@", "  Nano-Virus is given an instruction set to build waterproofing from genetic material,","@@@@\n")
    word_corey("@@@@", "  can allow for the bypassing of filters with enough biological shielding", "@@@@\n")
    word_corey("@@@@", "", "@@@@\n")
    word_corey("@@@@  Affects: ", influence[0], "@@@@\n")
    word_corez("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")
    word_corez("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")

def AIR_store_price(): # Changes air store price
    global air
    global air_price
    if air == 1:
        air_price += int(float(air_price) / 4)
    elif air == 2:
        air_price += int(float(air_price) / 2)
    elif air == 3:
        air_price = '--'
    else:
        return

def AIR_check(): #Activates when air is bought
    global air
    global infectivity
    if air == 1:
        infectivity += 400
        infectivity += int(float(infected) / 100)
    elif air == 2:
        infectivity += 500
        infectivity += int(float(infected) / 50)
    elif air == 3:
        infectivity += 600
        infectivity += int(float(infected) / 25)
    else:
        return

def AIR_info(): #Displays info about air
    word_corey("@@@@", "@@@@@@@@@@@@@@@@@@@@@@@@@@@", "@@@@\n")
    word_corey("@@@@", "@          `'@+;          @", "@@@@\n")
    word_corey("@@@@", "@        #@@:`.'@@        @", "@@@@\n")
    word_corey("@@@@", "@       @'       `@,      @", "@@@@\n")
    word_corey("@@@@", "@     `@           @`     @", "@@@@\n")
    word_corey("@@@@", "@     @             @     @", "@@@@\n")
    word_corey("@@@@", "@    @;     `@@@    @,    @", "@@@@\n")
    word_corey("@@@@", "@    @     +@  `@`   @    @", "@@@@\n")
    word_corey("@@@@", "@   .@    `@ ;@  @   @    @", "@@@@\n")
    word_corey("@@@@", "@   +.    @` @   @   @    @", "@@@@\n")
    word_corey("@@@@", "@   @     @  @   @   @    @", "@@@@\n")
    word_corey("@@@@", "@   @     @` @',@,  #:    @", "@@@@\n")
    word_corey("@@@@", "@   @     `@  ;+    @     @", "@@@@\n")
    word_corey("@@@@", "@   ':     @'      @`     @", "@@@@\n")
    word_corey("@@@@", "@    @      @@, .@@`      @", "@@@@\n")
    word_corey("@@@@", "@    @        +@+`        @", "@@@@\n")
    word_corey("@@@@", "@    '+                   @", "@@@@\n")
    word_corey("@@@@", "@     @                   @", "@@@@\n")
    word_corey("@@@@", "@     `@                  @", "@@@@\n")
    word_corey("@@@@", "@      ,@                 @", "@@@@\n")
    word_corey("@@@@", "@       .@,               @", "@@@@\n")
    word_corey("@@@@", "@         @@;             @", "@@@@\n")
    word_corey("@@@@", "@           '@            @", "@@@@\n")
    word_corey("@@@@", "@@@@@@@@@@@@@@@@@@@@@@@@@@@", "@@@@\n")
    word_corey("@@@@", "", "@@@@\n")
    word_corey("@@@@  ", "<<" + gene[3] + ">>", "@@@@\n")
    word_corey("@@@@", "  Nano-Virus begins to cut thin sllices of skin from the host to act as a parachute,","@@@@\n")
    word_corey("@@@@", "  carrying itself long distances via updrafts", "@@@@\n")
    word_corey("@@@@", "", "@@@@\n")
    word_corey("@@@@  Affects: ", influence[0], "@@@@\n")
    word_corez("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")
    word_corez("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")

def BLOOD_store_price(): # Changes blood price
    global blood
    global blood_price
    if blood == 1:
        blood_price += int(float(blood_price) / 2)
    elif blood == 2:
        blood_price += int(blood_price)
    else:
        return

def BLOOD_check(): # Will be run when bought to apply effects
    global blood
    global infected
    global infectivity
    global severity
    global lethality
    global zombify
    if blood == 1:
        infectivity += 250
        if zombify > 0:
            infectivity += 250
    elif blood == 2:
        infectivity += 250
        infectivity += int(float(infected)/20) * 1 + int(float(zombies)/100)
        if zombify > 0:
            infectivity += 250
    else:
        return

def BLOOD_info(): # Displays info about blood
    word_corey("@@@@", "@@@@@@@@@@@@@@@@@@@@@@@@@@@", "@@@@\n")
    word_corey("@@@@", "@ @                     ''@", "@@@@\n")
    word_corey("@@@@", "@ '@                   '@ @", "@@@@\n")
    word_corey("@@@@", "@  '@                 '@  @", "@@@@\n")
    word_corey("@@@@", "@   '@               '@   @", "@@@@\n")
    word_corey("@@@@", "@    '@             '@    @", "@@@@\n")
    word_corey("@@@@", "@     '@'@       '@'@     @", "@@@@\n")
    word_corey("@@@@", "@      '@         +@      @", "@@@@\n")
    word_corey("@@@@", "@  '                   '  @", "@@@@\n")
    word_corey("@@@@", "@  '@                 '@  @", "@@@@\n")
    word_corey("@@@@", "@   '@               '@   @", "@@@@\n")
    word_corey("@@@@", "@    '@             '@    @", "@@@@\n")
    word_corey("@@@@", "@     '@           '@     @", "@@@@\n")
    word_corey("@@@@", "@      '@ @     @ '@      @", "@@@@\n")
    word_corey("@@@@", "@       '@'      @@       @", "@@@@\n")
    word_corey("@@@@", "@   '    :            '   @", "@@@@\n")
    word_corey("@@@@", "@   '@               '@   @", "@@@@\n")
    word_corey("@@@@", "@    '@             '@    @", "@@@@\n")
    word_corey("@@@@", "@     '@           '@     @", "@@@@\n")
    word_corey("@@@@", "@      '@         '@      @", "@@@@\n")
    word_corey("@@@@", "@       '@ @   @ '@       @", "@@@@\n")
    word_corey("@@@@", "@        '@'    @@        @", "@@@@\n")
    word_corey("@@@@", "@         ,               @", "@@@@\n")
    word_corey("@@@@", "@@@@@@@@@@@@@@@@@@@@@@@@@@", "@@@@\n")
    word_corey("@@@@", "", "@@@@\n")
    word_corey("@@@@  ", "<<" + gene[4] + ">>", "@@@@\n")
    word_corey("@@@@", "  Nano-Virus attaches drone colonies to blood cells, both red and white, weakening the","@@@@\n")
    word_corey("@@@@", "  hosts immune system and capability to fight back. Transmission Becomes possible through", "@@@@\n")
    word_corey("@@@@", "  contact with blood, but only on an open wound or intake","@@@@\n")
    word_corey("@@@@", "", "@@@@\n")
    word_corey("@@@@  Affects: ",influence[0] + ", " + influence[1] + ", " + influence[2], "@@@@\n")
    word_corez("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")
    word_corez("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")

def SALIVA_store_price(): # Changes saliva price
    global saliva
    global saliva_price
    if saliva == 1:
        saliva_price += int(float(saliva_price) / 2)
    elif saliva == 2:
        saliva_price += int(saliva_price)
    else:
        return

def SALIVA_check(): # checks and applies saliva when bought
    global saliva
    global infectivity
    global infected
    global zombies
    global zombify
    if saliva == 1:
        infectivity += 100
        if zombify > 0:
            infectivity += 200
    elif saliva == 2:
        infectivity += 400
        infectivity += int(float(infected)/20) * 1 + int(float(zombies)/100)
        if zombify > 0:
            infectivity += 600
    else:
        return

def SALIVA_info(): # Shows saliva info
    word_corey("@@@@", "@@@@@@@@@@@@@@@@@@@@@@@@@@@", "@@@@\n")
    word_corey("@@@@", "@                         @", "@@@@\n")
    word_corey("@@@@", "@  '`                 `'  @", "@@@@\n")
    word_corey("@@@@", "@   @'               .@   @", "@@@@\n")
    word_corey("@@@@", "@    @@`            @@    @", "@@@@\n")
    word_corey("@@@@", "@      @@,        +@;     @", "@@@@\n")
    word_corey("@@@@", "@      @ #@@@@@@@@;@      @", "@@@@\n")
    word_corey("@@@@", "@      @     @     @      @", "@@@@\n")
    word_corey("@@@@", "@      ';    @     @      @", "@@@@\n")
    word_corey("@@@@", "@       @    @    :+      @", "@@@@\n")
    word_corey("@@@@", "@  @#   @    @    @   +@  @", "@@@@\n")
    word_corey("@@@@", "@   #@  #'   @   .@  @@   @", "@@@@\n")
    word_corey("@@@@", "@    `@@ @   @   @ .@'    @", "@@@@\n")
    word_corey("@@@@", "@      ,@@@, @ ,@'@@      @", "@@@@\n")
    word_corey("@@@@", "@         +@@@@@@;        @", "@@@@\n")
    word_corey("@@@@", "@                         @", "@@@@\n")
    word_corey("@@@@", "@@@@@@@@@@@@@@@@@@@@@@@@@@@", "@@@@\n")
    word_corey("@@@@", "", "@@@@\n")
    word_corey("@@@@  ", "<<" + gene[5] + ">>", "@@@@\n")
    word_corey("@@@@", "  Nano-Virus replicates in salivary glands, transmitting itself through touch with food,","@@@@\n")
    word_corey("@@@@", "  Drink, or human contact", "@@@@\n")
    word_corey("@@@@", "", "@@@@\n")
    word_corey("@@@@  Affects: ", influence[0], "@@@@\n")
    word_corez("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")
    word_corez("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")

def ZOMBIFY_store_price(): # Changes store price of zombify
    global zombify
    global zombify_price
    if zombify == 0:
        zombify_price += int(float(zombify_price) / 4)
    elif zombify == 1:
        zombify_price = '--'
    else:
        return

def ZOMBIFY_check(): # Applied weekly
    global zombify
    global infectivity
    global infected
    global zombies
    global lethality
    global infected
    global healthy
    global severity
    global dead
    global necrosis
    global cure
    zomb_limb = (float(zombies) / limit)
    if zombify == 1:
        z = (1 + int(float(infected) / (1 + (float(limit) / 1000))))
        zombies += z
        infectivity += int((float(infected) / (1 + healthy)) * 100 * lethality) + int(10 * necrosis)
        severity += (1 + int(zomb_limb))
        lethality += int(zomb_limb) * (1 + (float(healthy) / (1 + infected)))
        o = int(zomb_limb * 100 * (float(healthy) / 100))
        infected += o
        m = int(float(zomb_limb * 100 * (float(healthy) / 100)) / 100)
        dead += m
        cure_burst = random.randint(1, 100)
        healthy -= z + o + m
        if cure_burst >= 98:
            cure -= int(float(cure) / 10)
        else:
            return
    else:
        return

def ZOMBIFY_info(): # Explains what zombify is
    word_corey("@@@@  ", "@@@@@@@@@@@@@@@@@@@@@@@@@@@", "@@@@\n")
    word_corey("@@@@  ", "@                         @", "@@@@\n")
    word_corey("@@@@  ", "@   @'  .@       @@@@.    @", "@@@@\n")
    word_corey("@@@@  ", "@    @';@       @:   @    @", "@@@@\n")
    word_corey("@@@@  ", "@     @@        @    @    @", "@@@@\n")
    word_corey("@@@@  ", "@    @@@'       @    @    @", "@@@@\n")
    word_corey("@@@@  ", "@    +  @'      '@  :@    @", "@@@@\n")
    word_corey("@@@@  ", "@                '@@@     @", "@@@@\n")
    word_corey("@@@@  ", "@                         @", "@@@@\n")
    word_corey("@@@@  ", "@                         @", "@@@@\n")
    word_corey("@@@@  ", "@                         @", "@@@@\n")
    word_corey("@@@@  ", "@  ,'                 '   @", "@@@@\n")
    word_corey("@@@@  ", "@   @@               @@   @", "@@@@\n")
    word_corey("@@@@  ", "@   @+@`            @#@   @", "@@@@\n")
    word_corey("@@@@  ", "@   ;+.@@`        @@`@    @", "@@@@\n")
    word_corey("@@@@  ", "@    @@  @@@#++@@@.@;@    @", "@@@@\n")
    word_corey("@@@@  ", "@    @:  @ @..@.@   @;    @", "@@@@\n")
    word_corey("@@@@  ", "@        '@    @@         @", "@@@@\n")
    word_corey("@@@@  ", "@         ,    :@         @", "@@@@\n")
    word_corey("@@@@  ", "@                         @", "@@@@\n")
    word_corey("@@@@  ", "@@@@@@@@@@@@@@@@@@@@@@@@@@@", "@@@@\n")
    word_corey("@@@@", "", "@@@@\n")
    word_corey("@@@@  ", "<<" + gene[6] + ">>", "@@@@\n")
    word_corey("@@@@", "  Nano-Virus burrows into brainstem and hijacks the hosts nervous system. The electrical","@@@@\n")
    word_corey("@@@@", "  surge of the virus has the potential to bring even the most severely wounded back to life", "@@@@\n")
    word_corey("@@@@", "", "@@@@\n")
    word_corey("@@@@  Affects: ", influence[0] + ", " + influence[1] + ", " + influence[2], "@@@@\n")
    word_corez("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")
    word_corez("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")

def RISE_store_price(): # Changes rise store price
    global rise
    global rise_price
    if rise == 0:
        return
    elif rise == 1:
        rise_price += int(float(rise_price) / 4)
    elif rise == 2:
        rise_price += int(float(rise_price) / 3)
    elif rise == 3:
        rise_price += int(float(rise_price) / 2)
    elif rise == 4:
        rise_price += int(float(rise_price) / 1)
    elif rise == 1:
        rise_price = '--'
    else:
        return

def RISE_check(): # Applies effect when bought
    global rise
    global dead
    global zombies
    global infected
    global severity
    if rise == 1:
        i_v = int(float(dead) / 10)
        dead -= i_v
        if zombify <= 0:
            infected += i_v
        else:
            zombies += i_v
        severity += 5
    elif rise == 2:
        i_v2 = int(float(dead) / 8)
        dead -= i_v2
        if zombify <= 0:
            infected += i_v2
        else:
            zombies += i_v2
        severity += 10
    elif rise == 3:
        i_v3 = int(float(dead) / 6)
        dead -= i_v3
        if zombify <= 0:
            infected += i_v3
        else:
            zombies += i_v3
        severity += 15
    elif rise == 4:
        i_v4 = int(float(dead) / 4)
        dead -= i_v4
        if zombify <= 0:
            infected += i_v4
        else:
            zombies += i_v4
        severity += 20
    elif rise == 5:
        i_v5 = int(float(dead) / 2)
        dead -= i_v5
        if zombify <= 0:
            infected += i_v5
        else:
            zombies += i_v5
        severity += 25
    else:
        return

def RISE_info(): # more info
    word_corey("@@@@  ", "@@@@@@@@@@@@@@@@@@@@@@@@@@@", "@@@@\n")
    word_corey("@@@@  ", "@                         @", "@@@@\n")
    word_corey("@@@@  ", "@                 .       @", "@@@@\n")
    word_corey("@@@@  ", "@              @@@+@@     @", "@@@@\n")
    word_corey("@@@@  ", "@            @@.    `@    @", "@@@@\n")
    word_corey("@@@@  ", "@           @'.      @.   @", "@@@@\n")
    word_corey("@@@@  ", "@          @,  ,      @   @", "@@@@\n")
    word_corey("@@@@  ", "@         @'   @      @   @", "@@@@\n")
    word_corey("@@@@  ", "@        @'#   ,@     @   @", "@@@@\n")
    word_corey("@@@@  ", "@       @;  ;   @;    @   @", "@@@@\n")
    word_corey("@@@@  ", "@      @,   @   ,@@   @   @", "@@@@\n")
    word_corey("@@@@  ", "@    `@`    '@   @`@@'@   @", "@@@@\n")
    word_corey("@@@@  ", "@    `@`    '@   @`@@'@   @", "@@@@\n")
    word_corey("@@@@  ", "@   .@@@@@#  @,  @   '@   @", "@@@@\n")
    word_corey("@@@@  ", "@  ,@+    @+ @@. @        @", "@@@@\n")
    word_corey("@@@@  ", "@          @@@ @@+        @", "@@@@\n")
    word_corey("@@@@  ", "@           `             @", "@@@@\n")
    word_corey("@@@@  ", "@@@@@@@@@@@@@@@@@@@@@@@@@@@", "@@@@\n")
    word_corey("@@@@", "", "@@@@\n")
    word_corey("@@@@  ", "<<" + gene[7] + ">>", "@@@@\n")
    word_corey("@@@@", "  Nano-virus attaches to all vital organs of corpses and applies rapid surges to bring", "@@@@\n")
    word_corey("@@@@", "  Them to a semi-living state, the energy drain takes away from the ability to", "@@@@\n")
    word_corey("@@@@", "  Turna non-hijacked host into a zombie but will bring back infected persons", "@@@@\n")
    word_corey("@@@@", "", "@@@@\n")
    word_corey("@@@@  Affects: ", influence[1], "@@@@\n")
    word_corez("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")
    word_corez("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")

def attribute_menu(): # This is the lab, where all genes are synthed and researched
    global burst
    global necrosis
    global water
    global air
    global blood
    global saliva
    global zombify
    global rise
    global gene
    global severity
    global lethality
    global infectivity
    clear()
    lux()
    word_corez("@@@@  Welcome back to your lab!                                                                  @@@@\n")
    word_corey("@@@@", "", "@@@@\n")
    word_corey("@@@@ >>> EVOLVE | ", "Research genes to inject into your virus", "@@@@\n")
    word_corey("@@@@", "", "@@@@\n")
    word_corey("@@@@ >>> LEVEL | ", "Check the research level of gene paths", "@@@@\n")
    word_corey("@@@@", "", "@@@@\n")
    word_corey("@@@@ >>> INFO | ", "Study the possible gene paths", "@@@@\n")
    word_corey("@@@@", "", "@@@@\n")
    word_corey("@@@@ >>> LEAVE | ", "Leave your lab", "@@@@\n")
    word_corey("@@@@", "", "@@@@\n")
    word_corez("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")
    word_corez("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")
    decide = input(str("Command: "))
    if decide == "INFO":
        clear()
        lux()
        BURST_info()
        input(str("Press ENTER to continue..."))
        clear()
        lux()
        NECROSIS_info()
        input(str("Press ENTER to continue..."))
        clear()
        lux()
        WATER_info()
        input(str("Press ENTER to continue..."))
        clear()
        lux()
        AIR_info()
        input(str("Press ENTER to continue..."))
        clear()
        lux()
        BLOOD_info()
        input(str("Press ENTER to continue..."))
        clear()
        lux()
        SALIVA_info()
        input(str("Press ENTER to continue..."))
        clear()
        lux()
        ZOMBIFY_info()
        input(str("Press ENTER to continue..."))
        clear()
        lux()
        RISE_info()
        input(str("Press ENTER to continue..."))
        clear()
        attribute_menu()
    elif decide == "LEVEL":
        clear()
        lux()
        word_corey("@@@@","  Burst Level: " + str(burst), "@@@@\n")
        word_corey("@@@@", "", "@@@@\n")
        word_corey("@@@@", "  Necrosis Level: " + str(necrosis), "@@@@\n")
        word_corey("@@@@", "", "@@@@\n")
        word_corey("@@@@", "  Water Level: " + str(water), "@@@@\n")
        word_corey("@@@@", "", "@@@@\n")
        word_corey("@@@@", "  Air Level: " + str(air), "@@@@\n")
        word_corey("@@@@", "", "@@@@\n")
        word_corey("@@@@", "  Blood Level: " + str(blood), "@@@@\n")
        word_corey("@@@@", "", "@@@@\n")
        word_corey("@@@@", "  Saliva Level: " + str(saliva), "@@@@\n")
        word_corey("@@@@", "", "@@@@\n")
        word_corey("@@@@", "  Zombify Level: " + str(zombify), "@@@@\n")
        word_corey("@@@@", "", "@@@@\n")
        word_corey("@@@@", "  Rise Level: " + str(rise), "@@@@\n")
        word_corez("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")
        word_corez("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")
        input(str("Press ENTER to continue..."))
        clear()
        attribute_menu()
    elif decide == "EVOLVE":
        clear()
        lux()
        BURST_store_price()
        NECROSIS_store_price()
        WATER_store_price()
        AIR_store_price()
        BLOOD_store_price()
        SALIVA_store_price()
        ZOMBIFY_store_price()
        RISE_store_price()
        global dna_points
        global burst_price
        global necrosis_price
        global water_price
        global air_price
        global blood_price
        global saliva_price
        global zombify_price
        global rise_price
        word_corey("@@@@", "  " + gene[0] + " | Research Cost: " + str(burst_price), "@@@@\n")
        word_corey("@@@@", "", "@@@@\n")
        word_corey("@@@@", "  " + gene[1] + " | Research Cost: " + str(necrosis_price), "@@@@\n")
        word_corey("@@@@", "", "@@@@\n")
        word_corey("@@@@", "  " + gene[2] + " | Research Cost: " + str(water_price), "@@@@\n")
        word_corey("@@@@", "", "@@@@\n")
        word_corey("@@@@", "  " + gene[3] + " | Research Cost: " + str(air_price), "@@@@\n")
        word_corey("@@@@", "", "@@@@\n")
        word_corey("@@@@", "  " + gene[4] + " | Research Cost: " + str(blood_price), "@@@@\n")
        word_corey("@@@@", "", "@@@@\n")
        word_corey("@@@@", "  " + gene[5] + " | Research Cost: " + str(saliva_price), "@@@@\n")
        word_corey("@@@@", "", "@@@@\n")
        word_corey("@@@@", "  " + gene[6] + " | Research Cost: " + str(zombify_price), "@@@@\n")
        word_corey("@@@@", "", "@@@@\n")
        word_corey("@@@@", "  " + gene[7] + " | Research Cost: " + str(rise_price), "@@@@\n")
        word_corey("@@@@", "", "@@@@\n")
        word_corey("@@@@  RESEARCH POINTS | ", str(dna_points), "@@@@\n")
        word_corez("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")
        word_corez("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")
        evo = input(str("Synthesize: "))
        if evo == gene[0]:
            if burst_price != '--':
                if dna_points >= burst_price:
                    clear()
                    burst += 1
                    lethality += 3
                    severity += 25
                    dna_points -= burst_price
                    word_corex(gene[0] + " |", "Successfully synthesized!")
                    time.sleep(2)
                    clear()
                    attribute_menu()
                elif dna_points <= burst_price:
                    clear()
                    word_corex(gene[0] + " |", "Synthesis Failed!")
                    time.sleep(2)
                    clear()
                    attribute_menu()
                else:
                    attribute_menu()
            else:
                clear()
                word_core("There is nothing more to research on this gene...", 0.01)
                time.sleep(1)
                attribute_menu()
        elif evo == gene[1]:  # // passive
            if necrosis_price != '--':
                if dna_points >= necrosis_price:
                    clear()
                    necrosis += 1
                    severity += 10
                    dna_points -= necrosis_price
                    word_corex(gene[1] + " |", "Successfully synthesized!")
                    time.sleep(2)
                    clear()
                    attribute_menu()
                elif dna_points <= necrosis_price:
                    clear()
                    word_corex(gene[1] + " |", "Synthesis Failed!")
                    time.sleep(2)
                    clear()
                    attribute_menu()
                else:
                    attribute_menu()
            else:
                clear()
                word_core("There is nothing more to research on this gene...", 0.01)
                time.sleep(1)
                attribute_menu()
        elif evo == gene[2]:
            if water_price != '--':
                if dna_points >= water_price:
                    clear()
                    water += 1
                    dna_points -= water_price
                    word_corex(gene[2] + " |", "Successfully synthesized!")
                    WATER_check()
                    time.sleep(2)
                    clear()
                    attribute_menu()
                elif dna_points <= water_price:
                    clear()
                    word_corex(gene[2] + " |", "Synthesis Failed!")
                    time.sleep(2)
                    attribute_menu()
                else:
                    attribute_menu()
            else:
                clear()
                word_core("There is nothing more to research on this gene...", 0.01)
                time.sleep(1)
                attribute_menu()
        elif evo == gene[3]:
            if air_price != '--':
                if dna_points >= air_price:
                    clear()
                    air += 1
                    dna_points -= air_price
                    word_corex(gene[3] + " |", "Successfully synthesized!")
                    AIR_check()
                    time.sleep(2)
                    clear()
                    attribute_menu()
                elif dna_points <= air_price:
                    clear()
                    word_corex(gene[3] + " |", "Synthesis Failed!")
                    time.sleep(2)
                    clear()
                    attribute_menu()
                else:
                    attribute_menu()
            else:
                clear()
                word_core("There is nothing more to research on this gene...", 0.01)
                time.sleep(1)
                attribute_menu()
        elif evo == gene[4]:
            if blood_price != '--':
                if dna_points >= blood_price:
                    clear()
                    blood += 1
                    dna_points -= blood_price
                    word_corex(gene[4] + " |", "Successfully synthesized!")
                    BLOOD_check()
                    time.sleep(2)
                    clear()
                    attribute_menu()
                elif dna_points <= blood_price:
                    clear()
                    word_corex(gene[4] + " |", "Synthesis Failed!")
                    time.sleep(2)
                    clear()
                    attribute_menu()
                else:
                    attribute_menu()
            else:
                clear()
                word_core("There is nothing more to research on this gene...", 0.01)
                time.sleep(1)
                attribute_menu()
        elif evo == gene[5]:
            if saliva_price != '--':
                if dna_points >= saliva_price:
                    clear()
                    saliva += 1
                    dna_points -= saliva_price
                    word_corex(gene[5] + " |", "Successfully synthesized!")
                    SALIVA_check()
                    time.sleep(2)
                    clear()
                    attribute_menu()
                elif dna_points <= saliva_price:
                    clear()
                    word_corex(gene[5] + " |", "Synthesis Failed!")
                    time.sleep(2)
                    clear()
                    attribute_menu()
                else:
                    attribute_menu()
            else:
                clear()
                word_core("There is nothing more to research on this gene...", 0.01)
                time.sleep(1)
                attribute_menu()
        elif evo == gene[6]:  # // passive
            if zombify_price != '--':
                if dna_points >= zombify_price:
                    clear()
                    zombify += 1
                    dna_points -= zombify_price
                    word_corex(gene[6] + " |", "Successfully synthesized!")
                    time.sleep(2)
                    clear()
                    attribute_menu()
                elif dna_points <= zombify_price:
                    clear()
                    word_corex(gene[6] + " |", "Synthesis Failed!")
                    time.sleep(2)
                    clear()
                    attribute_menu()
                else:
                    attribute_menu()
            else:
                clear()
                word_core("There is nothing more to research on this gene...", 0.01)
                time.sleep(1)
                attribute_menu()
        elif evo == gene[7]:
            if rise_price != '--':
                if dna_points >= rise_price:
                    clear()
                    rise += 1
                    dna_points -= rise_price
                    word_corex(gene[7] + " |", "Successfully synthesized!")
                    RISE_check()
                    time.sleep(2)
                    clear()
                    attribute_menu()
                elif dna_points <= rise_price:
                    clear()
                    word_corex(gene[6] + " |", "Synthesis Failed!")
                    time.sleep(2)
                    clear()
                    attribute_menu()
                else:
                    attribute_menu()
            else:
                clear()
                word_core("There is nothing more to research on this gene...", 0.01)
                time.sleep(1)
                attribute_menu()
        else:
            attribute_menu()
    elif decide == "LEAVE":
        clear()
        print("Goodbye!\n")
        time.sleep(0.4)
        clear()
        player_menu()
    else:
        clear()
        attribute_menu()

def exit_game(): # Gotta quit sometime, right?
    clear()
    word_core("You have chosen to exit the game... Are you sure? [y]/[n]", 0.05)
    print("\n")
    ans = input(str())
    print("\n")
    if ans == "Y" or ans == "y" or ans == "Yes" or ans == "yes" or ans == "YES":
        word_core("Exiting game...", 0.05)
        print("\n")
        clear()
        exit()
    elif ans == "n" or ans == "N" or ans == "no" or ans == "NO" or ans == "No":
        word_core("Not Exiting The Game...", 0.05)
        print("\n")
        clear()
        player_menu()
    else:
        exit_game()

def player_menu():
    clear()
    lux()
    word_corey("@@@@", "  Week: " + str(week), "@@@@\n")
    word_corey("@@@@", "", "@@@@\n")
    word_corey("@@@@ >>> WORLD | ", "View world data", "@@@@\n")
    word_corey("@@@@", "", "@@@@\n")
    word_corey("@@@@ >>> VIRUS | ", "View nano-virus data", "@@@@\n")
    word_corey("@@@@", "", "@@@@\n")
    word_corey("@@@@ >>> LAB | ", "Work on your virus in the lab", "@@@@\n")
    word_corey("@@@@", "", "@@@@\n")
    word_corey("@@@@ >>> TURN | ", "Move onto the next week", "@@@@\n")
    word_corey("@@@@", "", "@@@@\n")
    word_corey("@@@@ >>> FAST | ", "Enter fast turn mode", "@@@@\n")
    word_corey("@@@@", "", "@@@@\n")
    word_corey("@@@@ >>> SAVE | ", "Save your progress", "@@@@\n")
    word_corey("@@@@", "", "@@@@\n")
    word_corey("@@@@ >>> LOAD | ", "Load a previous save", "@@@@\n")
    word_corey("@@@@", "", "@@@@\n")
    word_corey("@@@@ >>> EXIT | ", "Quit the game without saving", "@@@@\n")
    word_corey("@@@@", "", "@@@@\n")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    answer = input(str("Command: "))
    if answer == "WORLD":
        clear()
        graphical_analysis()
    elif answer == "VIRUS":
        clear()
        plague_status_graph()
    elif answer == "LAB":
        clear()
        attribute_menu()
    elif answer == "TURN":
        clear()
        turn()
    elif answer == "FAST":
        clear()
        fast_turn()
    elif answer == "SAVE":
        clear()
        delete()
        save()
    elif answer == "LOAD":
        clear()
        load()
    elif answer == "EXIT":
        clear()
        exit_game()
    else:
        player_menu()

def save():
    with open("Save_file.py", "a") as file:
        file.write("healthy = " + str(healthy) + "\n")
        file.write("infected = " + str(infected) + "\n")
        file.write("zombies = " + str(zombies) + "\n")
        file.write("dead = " + str(dead) + "\n")
        file.write("cure = " + str(cure) + "\n")
        file.write("week = " + str(week) + "\n")
        file.write("influence = " + str(influence) + "\n")
        file.write("infectivity = " + str(infectivity) + "\n")
        file.write("infectivity_limit = " + str(infectivity_limit) + "\n")
        file.write("severity = " + str(severity) + "\n")
        file.write("severity_limit = " + str(severity_limit) + "\n")
        file.write("lethality = " + str(lethality) + "\n")
        file.write("lethality_limit = " + str(lethality_limit) + "\n")
        file.write("weekly_infections = " + str(weekly_infections) + "\n")
        file.write("dna_points = " + str(dna_points) + "\n")
        file.write("burst = " + str(burst) + "\n")
        file.write("burst_price = " + str(burst_price) + "\n")
        file.write("necrosis = " + str(necrosis) + "\n")
        file.write("necrosis_price = " + str(necrosis_price) + "\n")
        file.write("water = " + str(water) + "\n")
        file.write("water_price = " + str(water_price) + "\n")
        file.write("air = " + str(air) + "\n")
        file.write("blood = " + str(blood) + "\n")
        file.write("saliva = " + str(saliva) + "\n")
        file.write("zombify = " + str(zombify) + "\n")
        file.write("rise = " + str(rise) + "\n")
        file.write("gene = " + str(gene) + "\n")
        file.write("limit = int(" + str(healthy) + " + " + str(infected) + " + " + str(dead) + " + " + str(zombies) + ")\n")
        file.write("time1 = float( " + str(time1) + ")\n")
    clear()
    word_corex("SAVING |", "Save completed successfully")
    time.sleep(2)
    clear()
    player_menu()

def delete():
    if OS == "Windows":
        os.system("del Save_file.py")
    else:
        os.system("rm Save_file.py")

def load():
    import Save_file as load
    global zombies
    zombies = load.zombies
    global dead
    dead = load.dead
    global healthy
    healthy = load.healthy
    global infected
    infected = load.infected
    global week
    week = load.week
    global cure
    cure = load.cure
    global influence
    influence = load.influence
    global infectivity
    infectivity = load.infectivity
    global severity
    severity = load.severity
    global lethality
    lethality = load.lethality
    global weekly_infections
    weekly_infections = load.weekly_infections
    global dna_points
    dna_points = load.dna_points
    global burst
    burst = load.burst
    global burst_price
    burst_price = load.burst_price
    global necrosis
    necrosis = load.necrosis
    global necrosis_price
    necrosis_price = load.necrosis_price
    global water
    water = load.water
    global water_price
    water_price = load.water_price
    global air
    air = load.air
    global blood
    blood = load.blood
    global saliva
    saliva = load.saliva
    global zombify
    zombify = load.zombify
    global rise
    rise = load.rise
    global gene
    gene = load.gene
    global limit
    limit = load.limit
    global q
    q = load.q
    word_corex("LOADING |", "Loading complete...")
    player_menu()

def turn():
    clear()
    global week
    week += 1
    word_core("A new week has come...", 0.1)
    print("\n")
    print("Week Number: " + str(week))
    time.sleep(1)
    dna_weekly()
    infecting_agent()
    check_cure_start()
    BURST_check()
    NECROSIS_check()
    ZOMBIFY_check()
    enforce_value_maximums()
    print("\n")
    player_menu()

def turn_fast():
    clear()
    global week
    week += 1
    print("A new week has come...")
    print("\n")
    print("Week Number: " + str(week))
    dna_weekly()
    infecting_agent()
    check_cure_start()
    BURST_check()
    NECROSIS_check()
    ZOMBIFY_check()
    enforce_value_maximums()
    Game_Over()
    print("\n")

def fast_turn():
    word_core("Press ENTER to take a turn...", 0.1)
    print("\n")
    word_core("Type STOP to go back to Player Menu...", 0.1)
    print("\n")
    while True:
        turn_fast()
        inp = input(str())
        if inp == "STOP":
            player_menu()

def start_turn(): # The initial turn and story of the game
    clear()
    word_corez("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")
    word_corez("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")
    word_corez("@@@@                                                                                             @@@@\n")
    word_corez("@@@@                                                                                             @@@@\n")
    word_corez("@@@@ @          @; `@@@@@@@  `@@@@@@@@ ;@      @; @@@@@@@@                                       @@@@\n")
    word_corez("@@@@ @@        @@+ @@:::::@@ @@::::::: ;@      @; @:::::::                                       @@@@\n")
    word_corez("@@@@ @@@      @@@+ @      ;@ @# @@@@@@ ;@      @; @::::::                                        @@@@\n")
    word_corez("@@@@ @ @@    @@ @+ @::::::+@ @# @@@@@@ ;@      @; @@@@@@@@.          @@@@@@@@@@@@@@@@@@          @@@@\n")
    word_corez("@@@@ @  @@  @@  @+ @@@@@@@@@ @#      @ ;@      @;        @#         ` @@@@@@@@@@@@@@@@           @@@@\n")
    word_corez("@@@@ @   @@#@   @+ @      ;@ @#      @ ;@      @;        @#         @` #@@@@@@@@@@@@@  @         @@@@\n")
    word_corez("@@@@ @    @@    @+ @      ;@ +@@@@@@@@  @@@@@@@@  @@@@@@@@`         @@: '@@@@@@@@@@@  @@         @@@@\n")
    word_corez("@@@@                                                                @@@' '@@@@@@@@@  @@@         @@@@\n")
    word_corez("@@@@                                                                @@@@' :@@@@@@@  @@@@         @@@@\n")
    word_corez("@@@@                                                                @@@@@# `@@@@@  @@@@@         @@@@\n")
    word_corez("@@@@                                                                @@@@@@   @@@  `@@@@@         @@@@\n")
    word_corez("@@@@                                                                @@@@@  @ `@ `@ `@@@@         @@@@\n")
    word_corez("@@@@                   @;         #@  @@@@@@@. .@ :@                @@@@  @@@  `@@@  @@@         @@@@\n")
    word_corez("@@@@                   @@:       +@@ @@:::::@@ .@ :@                @@@  @@@@@:@@@@@  @@         @@@@\n")
    word_corez("@@@@                   @+@.     ;@+@ @+      @ .@ :@                @@  @@@@@@@@@@@@@  @         @@@@\n")
    word_corez("@@@@                   @:;@`   :@.;@ @#::::::@ .@ :@                @  @@@@@@@@@@@@@@@           @@@@\n")
    word_corez("@@@@                   @: +@` .@: ;@ @@@@@@@@@ .@ :@                 `@@@@@@@@@@@@@@@@@          @@@@\n")
    word_corez("@@@@                   @:  +@`@:  ;@ @+      @ .@ :@                                             @@@@\n")
    word_corez("@@@@                   @:   #@'   ;@ @+      @ .@ :@@@@@@                                        @@@@\n")
    word_corez("@@@@                                                                                             @@@@\n")
    word_corez("@@@@                                                                                             @@@@\n")
    word_corez("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")
    word_corez("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")
    word_corez("@@@@                                                                                             @@@@\n")
    word_corez("@@@@          LeyCone@sidramail.gam             TO              MadLab@Magus.org                 @@@@\n")
    word_corez("@@@@                                                                                             @@@@\n")
    word_corez("@@@@                                                                                             @@@@\n")
    loading("@@@@  ", "Decrypting Message", "....","                                                            Done!    @@@@\n")
    word_corez("@@@@                                                                                             @@@@\n")
    word_corey("@@@@ >>>", "Hello, Doctor, I see the project is going smoothly...","@@@@\n")
    word_corey("@@@@ >>>", "5/19/XX", "@@@@\n")
    word_corez("@@@@                                                                                             @@@@\n")
    loading("@@@@  ", "Decrypting Message", "....","                                                            Done!    @@@@\n")
    word_corez("@@@@                                                                                             @@@@\n")
    word_corey("@@@@ >>>", "The Nano-Virus you've been working on finally managed to infect someone", "@@@@\n")
    word_corey("@@@@ >>>", "Make sure to keep control, we wouldn't want you to die prematurely on us, now would we?", "@@@@\n")
    word_corey("@@@@ >>>", "9/04/XX", "@@@@\n")
    word_corez("@@@@                                                                                             @@@@\n")
    loading("@@@@  ", "Decrypting Message", "....","                                                            Done!    @@@@\n")
    word_corez("@@@@                                                                                             @@@@\n")
    word_corey("@@@@ >>>", "I assure you that you, your family, and whomever else you so wish will be kept safe, so","@@@@\n")
    word_corey("@@@@ >>>", "Worry not. Now, without further ado, let us begin the transition to a new age!","@@@@\n")
    word_corey("@@@@ >>>", "9/012/XX", "@@@@\n")
    word_corez("@@@@                                                                                             @@@@\n")
    word_corez("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")
    word_corez("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")
    input(str("press ENTER to exit Magus..."))
    clear()
    player_menu()

def clear():
    if OS == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def Game_Over():
    global infected
    global zombies
    global cure
    if healthy <= 0:
        if infected <= 0:
            victory()
        else:
            return
    if infected <= 0:
        if zombies <= 0:
            infected_game_over()
        else:
            return
    if cure >= 1000:
        clear()
        cured_game_over()
    else:
        return

def infected_game_over():
    clear()
    word_core("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n", 0.01)
    word_core("{      _____       ___     _     _    _____     ____     _      _   _____   ___     }\n", 0.01)
    word_core("{    //-----\\\\    //-\\\\   | \   / |  ||----   //    \\\\  \ \    / / ||----  || \\\\    }\n", 0.01)
    word_core("{    ||          //   \\\\  | \\\\_// |  ||____   || || ||   \ \  / /  ||____  ||_//    }\n", 0.01)
    word_core("{    ||  _____   ||---||  | |   | |  ||----   || || ||    \ \/ /   ||----  || \\\\    }\n", 0.01)
    word_core("{    \\\\_____//   ||   ||  |_|   |_|  ||____   \\\\____//     \__/    ||____  ||  \\\\   }\n", 0.01)
    print("{	                                                                            }")
    word_core("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n", 0.01)
    time.sleep(1)
    print("\n")
    word_corex("NO INFECTED |", "All infected have been exterminated....")
    print("\n")
    word_corex("NO ZOMBIES |", "All zombies have been exterminated...")
    time.sleep(1)
    print("\n")
    word_corex("CURE COMPLETE |", "All infected have been cured and zombies quarentined....")
    print("\n")
    input(str("Press ENTER to continue...."))
    gc.collect()
    clear()
    os.system("python Main.py")

def cured_game_over(): # You got cured
    clear()
    word_core("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n", 0.01)
    word_core("{      _____       ___     _     _    _____     ____     _      _   _____   ___     }\n", 0.01)
    word_core("{    //-----\\\\    //-\\\\   | \   / |  ||----   //    \\\\  \ \    / / ||----  || \\\\    }\n", 0.01)
    word_core("{    ||          //   \\\\  | \\\\_// |  ||____   || || ||   \ \  / /  ||____  ||_//    }\n", 0.01)
    word_core("{    ||  _____   ||---||  | |   | |  ||----   || || ||    \ \/ /   ||----  || \\\\    }\n", 0.01)
    word_core("{    \\\\_____//   ||   ||  |_|   |_|  ||____   \\\\____//     \__/    ||____  ||  \\\\   }\n", 0.01)
    print("{	                                                                            }")
    word_core("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n", 0.01)
    time.sleep(1)
    print("\n")
    word_corex("CURE COMPLETE |", "All infected have been cured and zombies quarentined....")
    print("\n")
    input(str("Press ENTER to continue...."))
    gc.collect()
    clear()
    os.system("python Main.py")

def victory(): # Everyone dies
    clear()
    word_core("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n", 0.001)
    word_core("@;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;';;;;;;;';;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;@\n", 0.001)
    word_core("@;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;#;;;;;;;;;;;;;+';;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;@\n", 0.001)
    word_core("@;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;@';;;;;;;;;;;;;;;;#+;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;@\n", 0.001)
    word_core("@;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;#@;;;;;;;;;;;;;;;;;;;'@';;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;@\n", 0.001)
    word_core("@;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;@#;;;;;;;;;;;;;;;;;;;;;;@#;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;@\n", 0.001)
    word_core("@;;;;;;;;;;;;;;;;;;;;;;;;;;;;;'@#;;;;;;;;;;;;;;;;;;;;;;;;@@;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;@\n", 0.001)
    word_core("@;;;;;;;;;;;;;;;;;;;;;;;;;;;;'@@;;;;;;;;;;;;;;;;;;;;;;;;;'@@;;;;;;;;;;;;;;;;;;;;;;;;;;;;;@\n", 0.001)
    word_core("@;;;;;;;;;;;;;;;;;;;;;;;;;;;;@@;;;;;;;;;;;;;;;;;;;;;;;;;;;#@@;;;;;;;;;;;;;;;;;;;;;;;;;;;;@\n", 0.001)
    word_core("@;;;;;;;;;;;;;;;;;;;;;;;;;;;@@#;;;;;;;;;;;;;;;;;;;;;;;;;;;;@@#;;;;;;;;;;;;;;;;;;;;;;;;;;;@\n", 0.001)
    word_core("@;;;;;;;;;;;;;;;;;;;;;;;;;;@@@;;;;;;;;;;;;;;;;;;;;;;;;;;;;;+@@';;;;;;;;;;;;;;;;;;;;;;;;;;@\n", 0.001)
    word_core("@;;;;;;;;;;;;;;;;;;;;;;;;;+@@#;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;@@@;;;;;;;;;;;;;;;;;;;;;;;;;;@\n", 0.001)
    word_core("@;;;;;;;;;;;;;;;;;;;;;;;;;@@@;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;@@@+;;;;;;;;;;;;;;;;;;;;;;;;;@\n", 0.001)
    word_core("@;;;;;;;;;;;;;;;;;;;;;;;;+@@@;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;+@@@;;;;;;;;;;;;;;;;;;;;;;;;;@\n", 0.001)
    word_core("@;;;;;;;;;;;;;;;;;;;;;;;;@@@@;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;@@@+;;;;;;;;;;;;;;;;;;;;;;;;@\n", 0.001)
    word_core("@;;;;;;;;;;;;;;;;;;;;;;;;@@@@;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;@@@@;;;;;;;;;;;;;;;;;;;;;;;;@\n", 0.001)
    word_core("@;;;;;;;;;;;;;;;;;;;;;;;#@@@#;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;@@@@;;;;;;;;;;;;;;;;;;;;;;;;@\n", 0.001)
    word_core("@;;;;;;;;;;;;;;;;;;;;;;;@@@@#;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;@@@@';;;;;;;;;;;;;;;;;;;;;;;@\n", 0.001)
    word_core("@;;;;;;;;;;;;;;;;;;;;;;;@@@@#;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;@@@@#;;;;;;;;;;;;;;;;;;;;;;;@\n", 0.001)
    word_core("@;;;;;;;;;;;;;;;;;;;;;;;@@@@@;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;@@@@@;;;;;;;;;;;;;;;;;;;;;;;@\n", 0.001)
    word_core("@;;;;;;;;;;;;;;;;;;;;;;;@@@@@;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;'@@@@@;;;;;;;;;;;;;;;;;;;;;;;@\n", 0.001)
    word_core("@;;;;;;;;;;;;;;;;;;;;;;'@@@@@;;;;;;;;;;;;;'+++';;;;;;;;;;;;;#@@@@@;;;;;;;;;;;;;;;;;;;;;;;@\n", 0.001)
    word_core("@;;;;;;;;;;;;;;;;;;;;;;'@@@@@+;;;;;;;;+@@@@@@@@@@@@;;;;;;;;;@@@@@@;;;;;;;;;;;;;;;;;;;;;;;@\n", 0.001)
    word_core("@;;;;;;;;;;;;;;;;;;;;;;'@@@@@@;;;;;;@@@@@@@@@@@@@@@@@+;;;;;;@@@@@@;;;;;;;;;;;;;;;;;;;;;;;@\n", 0.001)
    word_core("@;;;;;;;;;;;;;;;;;;;;;;;@@@@@@;;;;#@@@@@@@@@@@@@@@@@@@@';;;@@@@@@@;;;;;;;;;;;;;;;;;;;;;;;@\n", 0.001)
    word_core("@;;;;;;;;;;;;;;;;;;;;;;;@@@@@@@;;@@@@@@@@@@@@@@@@@@@@@@@+;;@@@@@@@;;;;;;;;;;;;;;;;;;;;;;;@\n", 0.001)
    word_core("@;;;;;;;;;;;;;;;;;;;;;;;@@@@@@@+;;@@@@@@@@@#+##@@@@@@@@@;;@@@@@@@+;;;;;;;;;;;;;;;;;;;;;;;@\n", 0.001)
    word_core("@;;;;;;;;;;;;;;;;;;;;;;;@@@@@@@@;;'@@@@+;;;;;;;;;;#@@@@;;@@@@@@@@;;;;;;;;;;;;;;;;;;;;;;;;@\n", 0.001)
    word_core("@;;;;;;;;;;;;;;;;;;;;;;;+@@@@@@@@;;;@';;;;;;;;;;;;;;##;;#@@@@@@@@;;;;;;;;;;;;;;;;;;;;;;;;@\n", 0.001)
    word_core("@;;;;;;;;;;;;;;;;;;;;;;;;@@@@@@@@@;;;;;;;;;;;;;;;;;;;;;#@@@@@@@@@;;;;;;;;;;;;;;;;;;;;;;;;@\n", 0.001)
    word_core("@;;;;;;;;;;;;;;;;;;;;;;#@@@@@@@@@@@+;;;;;;;;;;;;;;;;;;@@@@@@@@@@#+;;;;;;;;;;;;;;;;;;;;;;;@\n", 0.001)
    word_core("@;;;;;;;;;;;;;;;;;;;#@@@@@@@@@@@@@@@@;;;;;;;;;;;;;;;+@@@@@@@@@@@@@@@#;;;;;;;;;;;;;;;;;;;;@\n", 0.001)
    word_core("@;;;;;;;;;;;;;;;;;@@@@@@@@@@@@@@@@@@@@@+;;;;;;;;;;#@@@@@@@@@@@@@@@@@@@@';;;;;;;;;;;;;;;;;@\n", 0.001)
    word_core("@;;;;;;;;;;;;;;;#@@@@@@@@@@@@@@@@@@@@@@@@@@#;'@@@@@@@@@@@@@@@@@@@@@@@@@@@;;;;;;;;;;;;;;;;@\n", 0.001)
    word_core("@;;;;;;;;;;;;;;@@@@@@@@@@@@@@@@@@@@@@@@@@@@@;'@@@@@@@@@@@@@@@@@@@@@@@@@@@@';;;;;;;;;;;;;;@\n", 0.001)
    word_core("@;;;;;;;;;;;;;@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@;'@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#;;;;;;;;;;;;;@\n", 0.001)
    word_core("@;;;;;;;;;;;;@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@;'@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#;;;;;;;;;;;;@\n", 0.001)
    word_core("@;;;;;;;;;;;@@@@@@@@@#+++#@@@@@@@@@@@@@@@@;;;;;'@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+;;;;;;;;;;;@\n", 0.001)
    word_core("@;;;;;;;;;;@@@@@@@;;;;;;;;;;;+@@@@@@@@@@@;;;;;;;'@@@@@@@@@@@#;;;;;;;;;'@@@@@@@';;;;;;;;;;@\n", 0.001)
    word_core("@;;;;;;;;;#@@@@@;;;;;;;;;#+;;;;'@@@@@@@@';;;;;;;;@@@@@@@@@+;;;;;';;;;;;;;#@@@@@;;;;;;;;;;@\n", 0.001)
    word_core("@;;;;;;;;;@@@@';;;;;;;;;;@@@@#;;;@@@@@@@;;;;;;;;;'@@@@@@@;;;+@@@@;;;;;;;;;;@@@@@;;;;;;;;;@\n", 0.001)
    word_core("@;;;;;;;;@@@@;;;;;;;;;;;;@@@@@;;;;+@@@@@;;;;;;;;;;@@@@@+;;;;@@@@@;;;;;;;;;;;#@@@;;;;;;;;;@\n", 0.001)
    word_core("@;;;;;;;;@@@;;;;;;;;;;;;;@@@@@;;;;;+@@@@;;;;;;;;;'@@@@';;;;;@@@@@;;;;;;;;;;;;#@@@;;;;;;;;@\n", 0.001)
    word_core("@;;;;;;;#@@;;;;;;;;;;;;;;@@@@@;;;;;;#@@#;;;;;;;;;;@@@+;;;;;;@@@@@;;;;;;;;;;;;;#@@;;;;;;;;@\n", 0.001)
    word_core("@;;;;;;;@@';;;;;;;;;;;;;;@@@@@;;;;;;;@;;;;;;;;;;;;;'@;;;;;;'@@@@@;;;;;;;;;;;;;;@@#;;;;;;;@\n", 0.001)
    word_core("@;;;;;;;@@;;;;;;;;;;;;;;;@@@@@;;;;;;;;;;@@;;;;;'@#;;;;;;;;;#@@@@#;;;;;;;;;;;;;;;@@;;;;;;;@\n", 0.001)
    word_core("@;;;;;;+@;;;;;;;;;;;;;;;;#@@@@#;;;;;;;#@@@@@##@@@@@';;;;;;;@@@@@;;;;;;;;;;;;;;;;@@;;;;;;;@\n", 0.001)
    word_core("@;;;;;;@@;;;;;;;;;;;;;;;;;@@@@@;;;;;;;;@@@@@@@@@@@@;;;;;;;;@@@@@;;;;;;;;;;;;;;;;;@;;;;;;;@\n", 0.001)
    word_core("@;;;;;;@';;;;;;;;;;;;;;;;;@@@@@+;;;;;;;@@@@@@@@@@@#;;;;;;;@@@@@@;;;;;;;;;;;;;;;;;@+;;;;;;@\n", 0.001)
    word_core("@;;;;;;@;;;;;;;;;;;;;;;;;;#@@@@@;;;;;;;#@@@@@@@@@@;;;;;;;;@@@@@';;;;;;;;;;;;;;;;;+#;;;;;;@\n", 0.001)
    word_core("@;;;;;;@;;;;;;;;;;;;;;;;;;;@@@@@@;;;;;;'@@@@@@@@@@;;;;;;;@@@@@@;;;;;;;;;;;;;;;;;;;@;;;;;;@\n", 0.001)
    word_core("@;;;;;;@;;;;;;;;;;;;;;;;;;;#@@@@@#;;;;;;@@@@@@@@@@;;;;;;@@@@@@';;;;;;;;;;;;;;;;;;;@;;;;;;@\n", 0.001)
    word_core("@;;;;;;#;;;;;;;;;;;;;;;;;;;;@@@@@@+;;;;;@@@@@@@@@@;;;;;#@@@@@@;;;;;;;;;;;;;;;;;;;;@;;;;;;@\n", 0.001)
    word_core("@;;;;;;#;;;;;;;;;;;;;;;;;;;;;@@@@@@#;;;;@@@@@@@@@@;;;;@@@@@@@;;;;;;;;;;;;;;;;;;;;;#;;;;;;@\n", 0.001)
    word_core("@;;;;;;#;;;;;;;;;;;;;;;;;;;;;+@@@@@@@';;@@@@@@@@@@;;;@@@@@@@';;;;;;;;;;;;;;;;;;;;;+;;;;;;@\n", 0.001)
    word_core("@;;;;;;#;;;;;;;;;;;;;;;;;;;;;;+@@@@@@@;;@@@@@@@@@@;'@@@@@@@+;;;;;;;;;;;;;;;;;;;;;;;;;;;;;@\n", 0.001)
    word_core("@;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;+@@@@@@;;@@@@@@@@@@;;@@@@@@+;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;@\n", 0.001)
    word_core("@;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;'@@@@#;+@@@@@@@@@@;;@@@@@';;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;@\n", 0.001)
    word_core("@;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;@@@;;@@@@@@@@@@@';@@@@;;;;;;;;;;;;;;;;;;;;;;;;;';;;;;;;@\n", 0.001)
    word_core("@;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;@;;@@@@@@@@@@@@;;@;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;@\n", 0.001)
    word_core("@;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;#@@@@@@@@@@@@;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;@\n", 0.001)
    word_core("@;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;@@@@@@@@@@@@@#;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;@\n", 0.001)
    word_core("@;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;@@@@@@@@@@@@@@@;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;@\n", 0.001)
    word_core("@;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;'@@@@@@@@@@@@@@@@;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;@\n", 0.001)
    word_core("@;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;@@@@@@@@+@@@@@@@@#;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;@\n", 0.001)
    word_core("@;;;;;;;;;;;';;;;;;;;;;;;;;;;;;;;;;@@@@@@@@#;;@@@@@@@@#;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;@\n", 0.001)
    word_core("@;;;;;;;;;;;;';;;;;;;;;;;;;;;;;;;+@@@@@@@@#;;;'@@@@@@@@@;;;;;;;;;;;;;;;;;;;;';;;;;;;;;;;;@\n", 0.001)
    word_core("@;;;;;;;;;;;;;'+;;;;;;;;;;;;;;;;@@@@@@@@@+;;;;;;@@@@@@@@@;;;;;;;;;;;;;;;;;';;;;;;;;;;;;;;@\n", 0.001)
    word_core("@;;;;;;;;;;;;;;;@+;;;;;;;;;;;;#@@@@@@@@@';;;;;;;;@@@@@@@@@@;;;;;;;;;;;;;'@;;;;;;;;;;;;;;;@\n", 0.001)
    word_core("@;;;;;;;;;;;;;;;;'@@+;;;;;'#@@@@@@@@@@#;;;;;;;;;;;'@@@@@@@@@@+;;;;;;;;#@+;;;;;;;;;;;;;;;;@\n", 0.001)
    word_core("@;;;;;;;;;;;;;;;;;;'@@@@@@@@@@@@@@@@#;;;;;;;;;;;;;;;+@@@@@@@@@@@@@@@@@+;;;;;;;;;;;;;;;;;;@\n", 0.001)
    word_core("@;;;;;;;;;;;;;;;;;;;;;+@@@@@@@@@@#;;;;;;;;;;;;;;;;;;;;;@@@@@@@@@@@@@';;;;;;;;;;;;;;;;;;;;@\n", 0.001)
    word_core("@;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;'+++';;;;;;;;;;;;;;;;;;;;;;;;;@\n", 0.001)
    word_core("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n", 0.001)
    print("\n")
    word_core("  +@@         @@.@@    @@@@@@@@@@ @@@@@@@@@@@@   @@@@@@@@:   @@@@@@@@@@.  @@        #@`\n", 0.001)
    word_core("   @@.       #@# @@  :@@@@@@@@@@@ @@@@@@@@@@@@ :@@@@@@@@@@@  @@@@@@@@@@@# @@        #@`\n", 0.001)
    word_core("    @@       @@  @@  @@:               @@      @@:       @@  @@       `@@ @@        #@`\n", 0.001)
    word_core("    #@#     @@.  @@  @@                @@      @@        @@  @@        @@ @@        #@`\n", 0.001)
    word_core("     @@    :@@   @@  @@                @@      @@        @@  @@        @@ @@        #@`\n", 0.001)
    word_core("     `@@   @@    @@  @@                @@      @@        @@  @@@@@@@@@@@@ +@@@@@@@@@@@`\n", 0.001)
    word_core("      @@; @@:    @@  @@                @@      @@        @@  @@@@@@@@@@@   @@@@@@@@@@@`\n", 0.001)
    word_core("       @@`@@     @@  @@                @@      @@        @@  @@   @@@               #@`\n", 0.001)
    word_core("       ,@@@      @@  @@@@@@@@@@@@      @@      @@@@@@@@@@@@  @@    #@@'     @@@@@@@@@@\n", 0.001)
    word_core("        @@'      @@   @@@@@@@@@@@      @@       @@@@@@@@@@#  @@     `@@@    @@@@@@@@@@\n", 0.001)
    print("\n")
    word_corex("VICTORY |", "All life on earth, except you and your select, have been exterminated")
    input(str("Press ENTER to continue...."))
    gc.collect()
    os.system("python Main.py")

def lux():
    word_corez("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")
    word_corez("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")
    word_corez("@@@@ @@        .@@         @@ +@@@         #@@#                                                  @@@@\n")
    word_corez("@@@@ @@        .@@         @@  `@@@       @@@.                                                   @@@@\n")
    word_corez("@@@@ @@        .@@         @@    @@@.   `@@@                                                     @@@@\n")
    word_corez("@@@@ @@        .@@         @@     #@@# +@@@                                                      @@@@\n")
    word_corez("@@@@ @@        .@@         @@      .@@@@@:                                                       @@@@\n")
    word_corez("@@@@ @@        .@@         @@        @@@`                                                        @@@@\n")
    word_corez("@@@@ @@        .@@         @@      .@@@@@'                                                       @@@@\n")
    word_corez("@@@@ @@        .@@         @@     #@@+ :@@@                                                      @@@@\n")
    word_corez("@@@@ @@        `@@        :@@    @@@.    @@@                                                     @@@@\n")
    word_corez("@@@@ @@@@@@@@@@ @@@@@@@@@@@@#  .@@@       @@@;                                                   @@@@\n")
    word_corez("@@@@ @@@@@@@@@@ `@@@@@@@@@@#  +@@@         '@@@                                                  @@@@\n")
    word_corez("@@@@                                                                                             @@@@\n")
    word_corez("@@@@                                                                                             @@@@\n")
    word_corez("@@@@                                                :     # @@@@@@@@@ +@@@@@@@@ #     :          @@@@\n")
    word_corez("@@@@                                               @@   :@@ @:     :@ @@        @@:   @@         @@@@\n")
    word_corez("@@@@                                             #@+   @@.  @:     .@ #@@@@@@@`  .@@   +@#       @@@@\n")
    word_corez("@@@@                                             @;   #@`   @:     .@  ;@@@@@@@   `@#   ;@       @@@@\n")
    word_corez("@@@@                                              @@:  :@@  @:     .@        `@  @@:  :@@        @@@@\n")
    word_corez("@@@@                                               :@    #@ @@:::::@@ :::::::#@ @#    @:         @@@@\n")
    word_corez("@@@@                                                        :@@@@@@@: @@@@@@@@'                  @@@@\n")
    word_corez("@@@@                                                                                             @@@@\n")
    word_corez("@@@@                                                                                             @@@@\n")
    word_corez("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")
    word_corez("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")
    word_corez("@@@@                                                                                             @@@@\n")
    word_corez("@@@@                                                                                             @@@@\n")

start_turn()

