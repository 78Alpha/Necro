import secrets, UniData

dna_points = UniData.dna_points
infected = UniData.infected
healthy = UniData.healthy

def dna_weekly(): # Weekly supply of DNA for research, used for LAB purchases
    global dna_points
    dna_points += int(float(infected)/(1 + (healthy * 100)))
    dna_random()
    with open('UniData.py', 'r') as file:
        data = file.readlines()
    data[13] = "dna_points = " + str(dna_points) + "\n"
    with open("UniData.py", 'w') as file:
        file.writelines(data)
    print("Research Points: " + str(dna_points))

def dna_random(): # Random DNA per week, can determine victory or defeat
    global dna_points
    rand_value1 = secrets.randbelow(10)
    if rand_value1 > 4:
        random_dna = secrets.randbelow(3)
        dna_points += int(random_dna)
    else:
        return