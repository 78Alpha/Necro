import json

variables = {"healthy" : 100000, "infected" : 1, "zombies" : 0, "dead" : 0, "cure" : 0, "week" : 0, "infectivity" : 0, "infectivity_limit" : 10000, "severity" : 0, "severity_limit" : 100, "lethality" : 0, "lethality_limit" : 10, "weekly_infections" : 10, "dna_points" : 0, "burst" : 0, "burst_price" : 10, "necrosis" : 0, "necrosis_price" : 20, "water" : 0, "water_price" : 10, "air" : 0, "air_price" : 10, "blood" : 0, "blood_price" : 20, "saliva" : 0, "saliva_price" : 20, "zombify" : 0, "zombify_price" : 20, "rise" : 0, "rise_price" : 20, "limit" : 100001}

def save():
    global variables
    with open("data.txt", "w") as file:
        json.dump(variables, file, indent=3)
        #print(json.dumps(variables, indent=4))

save()
