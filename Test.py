import sys, random

inf2 = ''

def randommizer():
    rand_int = random.randint(1, 100)
    limit = 100
    infect = int((float(rand_int) / limit) * 100)
    inf = "["
    for i in range(infect):  # Visual for infection
        inf += "|"
    for i in range(100 - int(infect)):  # Visual for non-infected
        inf += "."
    global inf2
    inf2 = str(inf) + "] " + str(infect) + "% Infected"
    print("Population Infected")
    print("\n")
    return(inf2)