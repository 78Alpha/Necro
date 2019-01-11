import secrets, json, random

def dna_weekly(): # Weekly supply of DNA for research, used for LAB purchases
    with open("UniData.txt", 'r') as f:
        variables = json.load(f)
    #print("DNA POINTS (DEBUG): " + str(variables["dna_points"]))
    variables["dna_points"] += 1 + int(float(variables["infected"])/(1 + (variables["healthy"] * 100)))
    #print("DNA POINTS (DEBUG): " + str(variables["dna_points"]))
    #dna_random()
    #print("DNA POINTS (DEBUG): " + str(variables["dna_points"]))
    with open("UniData.txt", 'w') as f2:
        json.dump(variables, f2, indent=3)
    with open("UniData.txt", 'r') as f3:
        variables = json.load(f3)


def dna_random(): # Random DNA per week, can determine victory or defeat
    with open("UniData.txt", 'r') as f:
        variables = json.load(f)
    rand_value1 = secrets.randbelow(100)
    #print("RAND VALUE (DEBUG): " + str(rand_value1))
    if rand_value1 >= 70:
        random_dna = random.randint(1, 5)
    #    print("RANDOM DNA (DEBUG: " + str(random_dna))
        variables["dna_points"] += int(random_dna)
    #    print("DNA POINTS (DEBUG): " + str(variables["dna_points"]))
        with open("UniData.txt", 'w') as f2:
            json.dump(variables, f2, indent=3)
    #    print("DNA POINTS (DEBUG): " + str(variables["dna_points"]))
    print("Research Points: " + str(variables["dna_points"]))
