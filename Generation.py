import secrets, json

def dna_weekly(): # Weekly supply of DNA for research, used for LAB purchases
    with open("UniData.txt", 'r') as f:
        variables = json.load(f)
    variables["dna_points"] += int(float(variables["infected"])/(1 + (variables["healthy"] * 100)))
    dna_random()
    with open("UniData.txt", 'w') as f2:
        json.dump(variables, f2, indent=3)
    print("Research Points: " + str(variables["dna_points"]))

def dna_random(): # Random DNA per week, can determine victory or defeat
    with open("UniData.txt", 'r') as f:
        variables = json.load(f)
    rand_value1 = secrets.randbelow(10)
    if rand_value1 > 4:
        random_dna = secrets.randbelow(3)
        variables["dna_points"] += int(random_dna)
        with open("UniData.txt", 'w') as f2:
            json.dump(variables, f2, indent=3)
    else:
        return
