import sys, random

inf3 = ''

def randommizer():
    rand_int = random.randint(1, 100)
    limit = 100
    infect = int((float(rand_int) / limit) * 100)
    inf = "["
    for i in range(infect):  # Visual for infection
        inf += "|"
    for i in range(100 - int(infect)):  # Visual for non-infected
        inf += "."
    global inf3
    inf3 = str(inf) + "] " + str(infect) + "% Healthy"
    print("Population Infected")
    print("\n")
    return(inf3)