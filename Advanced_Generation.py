import secrets, json

def Read_val():
    with open("data.txt", 'r') as f:
        variables = json.load(f)

def Write_val():
    with open("data", 'w') as f2:
        json.dump(variables, f2, indent=3)

#Table of Characteristics
# Cell stability: Resisitance to necrosis
# Brain: Resist memory, mania, insanity, etc
# Bone: Resist paralysis, marrow degradation, etc.
# Lungs: Resist pneumonia, lung cancer, resperatory lapse, etc.
# Heart: Resist heart disease, stroke, heart attack, etc.
# Stomach: Resist acid reflux, indigestion, vomiting, etc.
# Genetalia: Resist std, uti, etc.
# Mouth: Resist hyper salivation, tooth decay, bad breath, etc.
# Skin: Resist flesh rot, sweating, etc.
# Blood: Resist hemophilia, sicle cell, anemia, etc.


def Generate_child(): #Make 14% of population, resist varies per daily
    #res_core = secrets.randbelow(50)
    child_cell_stability = secrets.randbelow(range(25, 50))
    child_Brain = child_cell_stability + secrets.randbelow(15) # CAP 65
    child_Bone = child_cell_stability + secrets.randbelow(20) # CAP 70
    child_Lungs = child_cell_stability + secrets.randbelow(range(10, 50)) # MIN 35, CAP 100
    child_Heart = child_cell_stability + secrets.randbelow(range(40, 50)) # MIN 65, CAP 100
    child_Stomach = child_cell_stability + secrets.randbelow((range(-10, 50))) # MIN 15, CAP 100
    child_Genetalia = child_cell_stability + secrets.randbelow((range(40, 50))) # MIN 65, CAP 100
