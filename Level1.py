import os, platform, time, secrets, gc, sys, threading, Clear, WordCore, Loading, UI, Graph, Generation, json
from json_system import *
from ColorSplash import *

OS = platform.system()


def check_cure_start():  #determines if cure research should start or not
    with open("UniData.txt", 'r') as f:
        variables = json.load(f)
    if variables["severity"] >= 5:
        cure_value()
    elif variables["week"] >= 20:
        cure_value()
    else:
        return


def cure_value(): # How fast the cure will increase
    with open("UniData.txt", 'r') as f:
        variables = json.load(f)
    variables["cure"] += 5
    cure_attack_value = float(variables["infected"])/variables["healthy"]
    if cure_attack_value > 0.5:  # Determines how fast the cure will progress due to "fear"
        variables["cure"] += int(float(variables["cure"]) / 5)
        if variables["severity"] >= 30:
            variables["cure"] += (1 + int(float(variables["severity"]) / variables["lethality"]))
            threat = int(float(variables["zombies"]) / variables["limit"]) * 100
            if threat >= 33:
                variables["cure"] += int(float(variables["zombies"]) / variables["limit"]) * 10
    else:
        return
    with open("UniData.txt", 'w') as f2:
        json.dump(variables, f2, indent=3)


def infecting_agent(): # Determines how many infections occur
    with open("UniData.txt", 'r') as f:
        variables = json.load(f)
    inf_value = float(variables["infectivity"])/(1 + variables["lethality"]) # Must be kept as int() + lethality, inflates lethality otherwise
    variables["infected"] += int(inf_value) + int(variables["weekly_infections"])
    variables["healthy"] -= int(inf_value) + int(variables["weekly_infections"])
    with open("UniData.txt", 'w') as f2:
        json.dump(variables, f2, indent=3)


def enforce_value_maximums(): #Makes sure that maximum/minumum values are never violated
    with open("UniData.txt", 'r') as f:
        variables = json.load(f)
    if variables["lethality"] > variables["lethality_limit"]:
        variables["lethality"] = variables["lethality_limit"]
    if variables["lethality"] < 0:
        variables["lethality"] = 0
    if variables["infectivity"] > variables["infectivity_limit"]: # Max value of infectivity
        variables["infectivity"] = variables["infectivity_limit"]
    if variables["infectivity"] < 0: # Minimum level of infectivity
        variables["infectivity"] = 0
    if variables["severity"] > variables["severity_limit"]: # Max value of severity
        variables["severity"] = variables["severity_limit"]
    if variables["severity"] < 0: # Minimum level of severity
        variables["severity"] = 0
    if variables["infected"] > variables["limit"]: # Max number of infected
        variables["infected"] = variables["limit"]
    if variables["infected"] < 0: # Minimum number of infected
        variables["infected"] = 0
    if variables["healthy"] < 0: # Minimum level of healthy
        variables["healthy"] = 0
    if variables["healthy"] > variables["limit"]: # Maximum number of healthy
        variables["healthy"] = 0
    if variables["dead"] > variables["limit"]: # Max number of dead
        variables["dead"] = variables["limit"]
    if variables["dead"] < 0: # Minimum number of dead
        variables["dead"] = 0
    if variables["zombies"] > variables["limit"]: # Max number of zombies
        variables["zombies"] = variables["limit"]
    if variables["zombies"] < 0: # Minimum number of zombies
        variables["zombies"] = 0
    with open("UniData.txt", 'w') as f2:
        json.dump(variables, f2, indent=3)


def BURST_store_price(): # Changes burst store price depending on level
    with open("UniData.txt", 'r') as f:
        variables = json.load(f)
    if variables["burst"] == 1:
        variables["burst_price"] = "--"
    else:
        return


def BURST_check(): #chekcs if burst is active and applies it every turn
    with open("UniData.txt", 'r') as f:
        variables = json.load(f)
    if variables["burst"] == 1:
        temp = int(variables["infected"] * 0.01)
        if temp < 1:
            temp = 1
            variables["infectivity"] += temp
            variable["infected"] -= temp
            variables["dead"] += temp
        else:
            variables["infectivity"] += temp
            variables["infected"] -= temp
            variables["dead"] += temp
    else:
        return
    with open("UniData.txt", 'w') as f2:
        json.dump(variables, f2, indent=3)


def BURST_info(): #displays info about burst
    with open("UniData.txt", 'r') as f:
        variables = json.load(f)
    if variables["color"] != 0:
        UI.Color_Burst()
    else:
        UI.BURST_icon()
    WordCore.word_corey("@@@@", "", "@@@@\n")
    WordCore.word_corey("@@@@  ", "<<" + variables["gene[0]"] + ">>", "@@@@\n")
    WordCore.word_corey("@@@@", "  Nano-Virus disables pressure regulation of host skull, following up with a forced intake","@@@@\n")
    WordCore.word_corey("@@@@", "  of pressurized oxygen until cranial rupture/explosion occurrs", "@@@@\n")
    WordCore.word_corey("@@@@", "", "@@@@\n")
    WordCore.word_corey("@@@@  Affects: ", variables["influence[0]"] + ", " + variables["influence[1]"] + ", " + variables["influence[2]"], "@@@@\n")
    WordCore.word_corez("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")
    WordCore.word_corez("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")


def NECROSIS_store_price(): #checks to see if it can be bought/alters price
    with open("UniData.txt", 'r') as f:
        variables = json.load(f)
    if variables["necrosis"] == 1:
        variables["necrosis_price"] = "--"
    else:
        return


def NECROSIS_check(): #chekcs if necrosis is active, will be run weekly to continue the rise on infectivity
    with open("UniData.txt", 'r') as f:
        variables = json.load(f)
    if variables["necrosis"] == 1:
        variables["infectivity"] += int(float(variables["dead"])/(1 + variables["healthy"]))
    else:
        return
    with open("UniData.txt", 'w') as f2:
        json.dump(variables, f2, indent=3)


def NECROSIS_info(): #Displays info about necrosis
    with open("UniData.txt", 'r') as f:
        variables = json.load(f)
    if variables["color"] != 0:
        UI.Color_Necrosis()
    else:
        UI.NECROSIS_icon()
    #UI.NECROSIS_icon()
    WordCore.word_corey("@@@@", "", "@@@@\n")
    WordCore.word_corey("@@@@  ", "<<" + variables["gene[1]"] + ">>", "@@@@\n")
    WordCore.word_corey("@@@@", "  Nano-virus enters a low power state while in a dead host, power is diverted to motion","@@@@\n")
    WordCore.word_corey("@@@@", "  sensors such that individuals within proximity will be attacked before reaction is possible", "@@@@\n")
    WordCore.word_corey("@@@@", "", "@@@@\n")
    WordCore.word_corey("@@@@  Affects: ", variables["influence[0]"] + ", " + variables["influence[1]"], "@@@@\n")
    WordCore.word_corez("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")
    WordCore.word_corez("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")


def WATER_store_price(): # Changes store price of water gene
    with open("UniData.txt", 'r') as f:
        variables = json.load(f)
    if variables["water"] == 1:
        variables["water_price"] += int(float(variables["water_price"]) / 4)
    elif variables["water"] == 2:
        variables["water_price"] += int(float(variables["water_price"]) / 2)
    elif variables["water"] == 3:
        variables["water_price"] = '--'
    else:
        return
    with open("UniData.txt", 'w') as f2:
        json.dump(variables, f2, indent=3)


def WATER_check(): #chekcs if water is active, will be run when bought
    with open("UniData.txt", 'r') as f:
        variables = json.load(f)
    if variables["water"] == 1:
        variables["infectivity"] += int(variables["infected"] * 0.05)
    elif variables["water"] == 2:
        variables["infectivity"] += int(variables["infected"] * 0.1)
    elif variables["water"] == 3:
        variables["infectivity"] += int(variables["infected"] * 0.2)
    else:
        return
    with open("UniData.txt", 'w') as f2:
        json.dump(variables, f2, indent=3)


def WATER_info(): #Displays info about water
    with open("UniData.txt", 'r') as f:
        variables = json.load(f)
    if variables["color"] != 0:
        UI.Color_Water()
    else:
        UI.WATER_icon()
    #UI.WATER_icon()
    WordCore.word_corey("@@@@", "", "@@@@\n")
    WordCore.word_corey("@@@@  ", "<<" + variables["gene[2]"] + ">>", "@@@@\n")
    WordCore.word_corey("@@@@", "  Nano-Virus is given an instruction set to build waterproofing from genetic material,","@@@@\n")
    WordCore.word_corey("@@@@", "  can allow for the bypassing of filters with enough biological shielding", "@@@@\n")
    WordCore.word_corey("@@@@", "", "@@@@\n")
    WordCore.word_corey("@@@@  Affects: ", variables["influence[0]"], "@@@@\n")
    WordCore.word_corez("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")
    WordCore.word_corez("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")


def AIR_store_price(): # Changes air store price
    with open("UniData.txt", 'r') as f:
        variables = json.load(f)
    if variables["air"] == 1:
        variables["air_price"] += int(float(variables["air_price"]) / 4)
    elif variables["air"] == 2:
        variables["air_price"] += int(float(variables["air_price"]) / 2)
    elif variables["air"] == 3:
        variables["air_price"] = '--'
    else:
        return
    with open("UniData.txt", 'w') as f2:
        json.dump(variables, f2, indent=3)


def AIR_check(): #Activates when air is bought
    with open("UniData.txt", 'r') as f:
        variables = json.load(f)
    if variables["air"] == 1:
        variables["infectivity"] += 400
        variables["infectivity"] += int(float(variables["infected"]) / 100)
    elif variables["air"] == 2:
        variables["infectivity"] += 500
        variables["infectivity"] += int(float(variables["infected"]) / 50)
    elif variables["air"] == 3:
        variables["infectivity"] += 600
        variables["infectivity"] += int(float(variables["infected"]) / 25)
    else:
        return
    with open("UniData.txt", 'w') as f2:
        json.dump(variables, f2, indent=3)


def AIR_info(): #Displays info about air
    with open("UniData.txt", 'r') as f:
        variables = json.load(f)
    if variables["color"] != 0:
        UI.Color_Air()
    else:
        UI.AIR_icon()
    #UI.AIR_icon()
    WordCore.word_corey("@@@@", "", "@@@@\n")
    WordCore.word_corey("@@@@  ", "<<" + variables["gene[3]"] + ">>", "@@@@\n")
    WordCore.word_corey("@@@@", "  Nano-Virus begins to cut thin sllices of skin from the host to act as a parachute,","@@@@\n")
    WordCore.word_corey("@@@@", "  carrying itself long distances via updrafts", "@@@@\n")
    WordCore.word_corey("@@@@", "", "@@@@\n")
    WordCore.word_corey("@@@@  Affects: ", variables["influence[0]"], "@@@@\n")
    WordCore.word_corez("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")
    WordCore.word_corez("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")


def BLOOD_store_price(): # Changes blood price
    with open("UniData.txt", 'r') as f:
        variables = json.load(f)
    if variables["blood"] == 1:
        variables["blood_price"] += int(float(variables["blood_price"]) / 2)
    elif variables["blood"] == 2:
        variables["blood_price"] += int(variables["blood_price"])
    else:
        return
    with open("UniData.txt", 'w') as f2:
        json.dump(variables, f2, indent=3)


def BLOOD_check(): # Will be run when bought to apply effects
    with open("UniData.txt", 'r') as f:
        variables = json.load(f)
    if variables["blood"] == 1:
        variables["infectivity"] += 250
        if variables["zombify"] > 0:
            variables["infectivity"] += 250
    elif variables["blood"] == 2:
        variables["infectivity"] += 250
        variables["infectivity"] += int(float(variables["infected"])/20) * 1 + int(float(variables["zombies"])/100)
        if variables["zombify"] > 0:
            variables["infectivity"] += 250
    else:
        return
    with open("UniData.txt", 'w') as f2:
        json.dump(variables, f2, indent=3)


def BLOOD_info(): # Displays info about blood
    with open("UniData.txt", 'r') as f:
        variables = json.load(f)
    if variables["color"] != 0:
        UI.Color_Blood()
    else:
        UI.BLOOD_icon()
    #UI.BLOOD_icon()
    WordCore.word_corey("@@@@", "", "@@@@\n")
    WordCore.word_corey("@@@@  ", "<<" + variables["gene[4]"] + ">>", "@@@@\n")
    WordCore.word_corey("@@@@", "  Nano-Virus attaches drone colonies to blood cells, both red and white, weakening the","@@@@\n")
    WordCore.word_corey("@@@@", "  hosts immune system and capability to fight back. Transmission Becomes possible through", "@@@@\n")
    WordCore.word_corey("@@@@", "  contact with blood, but only on an open wound or intake","@@@@\n")
    WordCore.word_corey("@@@@", "", "@@@@\n")
    WordCore.word_corey("@@@@  Affects: ",variables["influence[0]"] + ", " + variables["influence[1]"] + ", " + variables["influence[2]"], "@@@@\n")
    WordCore.word_corez("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")
    WordCore.word_corez("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")


def SALIVA_store_price(): # Changes saliva price
    with open("UniData.txt", 'r') as f:
        variables = json.load(f)
    if variables["saliva"] == 1:
        variables["saliva_price"] += int(float(variables["saliva_price"]) / 2)
    elif variables["saliva"] == 2:
        variables["saliva_price"] += int(variables["saliva_price"])
    else:
        return
    with open("UniData.txt", 'w') as f2:
        json.dump(variables, f2, indent=3)


def SALIVA_check(): # checks and applies saliva when bought
    with open("UniData.txt", 'r') as f:
        variables = json.load(f)
    if variables["saliva"] == 1:
        variables["infectivity"] += 100
        if variables["zombify"] > 0:
            variables["infectivity"] += 200
    elif variables["saliva"] == 2:
        variables["infectivity"] += 400
        variables["infectivity"] += int(float(variables["infected"])/20) * 1 + int(float(variables["zombies"])/100)
        if variables["zombify"] > 0:
            variables["infectivity"] += 600
    else:
        return
    with open("UniData.txt", 'w') as f2:
        json.dump(variables, f2, indent=3)


def SALIVA_info(): # Shows saliva info
    with open("UniData.txt", 'r') as f:
        variables = json.load(f)
    if variables["color"] != 0:
        UI.Color_Saliva()
    else:
        UI.SALIVA_icon()
    #UI.SALIVA_icon()
    WordCore.word_corey("@@@@", "", "@@@@\n")
    WordCore.word_corey("@@@@  ", "<<" + variables["gene[5]"] + ">>", "@@@@\n")
    WordCore.word_corey("@@@@", "  Nano-Virus replicates in salivary glands, transmitting itself through touch with food,","@@@@\n")
    WordCore.word_corey("@@@@", "  Drink, or human contact", "@@@@\n")
    WordCore.word_corey("@@@@", "", "@@@@\n")
    WordCore.word_corey("@@@@  Affects: ", variables["influence[0]"], "@@@@\n")
    WordCore.word_corez("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")
    WordCore.word_corez("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")


def ZOMBIFY_store_price(): # Changes store price of zombify
    with open("UniData.txt", 'r') as f:
        variables = json.load(f)
    if variables["zombify"] == 0:
        variables["zombify_price"] += int(float(variables["zombify_price"]) / 4)
    elif variables["zombify"] == 1:
        variables["zombify_price"] = '--'
    else:
        return
    with open("UniData.txt", 'w') as f2:
        json.dump(variables, f2, indent=3)


def ZOMBIFY_check(): # Applied weekly
    with open("UniData.txt", 'r') as f:
        variables = json.load(f)
    zomb_limb = (float(variables["zombies"]) / variables["limit"])
    if variables["zombify"] == 1:
        z = (1 + int(float(variables["infected"]) / (1 + (float(variables["limit"]) / 1000))))
        variables["zombies"] += z
        variables["infectivity"] += int((float(variables["infected"]) / (1 + variables["healthy"])) * 100 * variables["lethality"]) + int(10 * variables["necrosis"])
        variables["severity"] += (1 + int(zomb_limb))
        variables["lethality"] += int(zomb_limb) * (1 + (float(variables["healthy"]) / (1 + variables["infected"])))
        o = int(zomb_limb * 100 * (float(variables["healthy"]) / 100))
        variables["infected"] += o
        m = int(float(zomb_limb * 100 * (float(variables["healthy"]) / 100)) / 100)
        variables["dead"] += m
        variables["cure_burst"] = secrets.choice(range(1, 100))
        variables["healthy"] -= z + o + m
        if variables["cure_burst"] >= 98:
            variables["cure"] -= int(float(variables["cure"]) / 10)
        else:
            return
    else:
        return
    with open("UniData.txt", 'w') as f2:
        json.dump(variables, f2, indent=3)


def ZOMBIFY_info(): # Explains what zombify is
    with open("UniData.txt", 'r') as f:
        variables = json.load(f)
    if variables["color"] != 0:
        UI.Color_Zombify()
    else:
        UI.ZOMBIFY_icon()
    #UI.ZOMBIFY_icon()
    WordCore.word_corey("@@@@", "", "@@@@\n")
    WordCore.word_corey("@@@@  ", "<<" + variables["gene[6]"] + ">>", "@@@@\n")
    WordCore.word_corey("@@@@", "  Nano-Virus burrows into brainstem and hijacks the hosts nervous system. The electrical","@@@@\n")
    WordCore.word_corey("@@@@", "  surge of the virus has the potential to bring even the most severely wounded back to life", "@@@@\n")
    WordCore.word_corey("@@@@", "", "@@@@\n")
    WordCore.word_corey("@@@@  Affects: ", variables["influence[0]"] + ", " + variables["influence[1]"] + ", " + variables["influence[2]"], "@@@@\n")
    WordCore.word_corez("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")
    WordCore.word_corez("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")


def RISE_store_price(): # Changes rise store price
    with open("UniData.txt", 'r') as f:
        variables = json.load(f)
    if variables["rise"] == 0:
        return
    elif variables["rise"] == 1:
        variables["rise_price"] += int(float(variables["rise_price"]) / 4)
    elif variables["rise"] == 2:
        variables["rise_price"] += int(float(variables["rise_price"]) / 3)
    elif variables["rise"] == 3:
        variables["rise_price"] += int(float(variables["rise_price"]) / 2)
    elif variables["rise"] == 4:
        variables["rise_price"] += int(float(variables["rise_price"]) / 1)
    elif variables["rise"] == 1:
        variables["rise_price"] = '--'
    else:
        return
    with open("UniData.txt", 'w') as f2:
        json.dump(variables, f2, indent=3)


def RISE_check(): # Applies effect when bought
    with open("UniData.txt", 'r') as f:
        variables = json.load(f)
    if variables["rise"] == 1:
        i_v = int(float(variables["dead"]) / 10)
        variables["dead"] -= i_v
        if variables["zombify"] <= 0:
            variables["infected"] += i_v
        else:
            variables["zombies"] += i_v
        variables["severity"] += 5
    elif variables["rise"] == 2:
        i_v2 = int(float(variables["dead"]) / 8)
        variables["dead"] -= i_v2
        if variables["zombify"] <= 0:
            variables["infected"] += i_v2
        else:
            variables["zombies"] += i_v2
        variables["severity"] += 10
    elif variables["rise"] == 3:
        i_v3 = int(float(variables["dead"]) / 6)
        variables["dead"] -= i_v3
        if variables["zombify"] <= 0:
            variables["infected"] += i_v3
        else:
            variables["zombies"] += i_v3
        variables["severity"] += 15
    elif rise == 4:
        i_v4 = int(float(variables["dead"]) / 4)
        variables["dead"] -= i_v4
        if variables["zombify"] <= 0:
            variables["infected"] += i_v4
        else:
            variables["zombies"] += i_v4
        variables["severity"] += 20
    elif variables["rise"] == 5:
        i_v5 = int(float(variables["dead"]) / 2)
        variables["dead"] -= i_v5
        if variables["zombify"] <= 0:
            variables["infected"] += i_v5
        else:
            variables["zombies"] += i_v5
        variables["severity"] += 25
    else:
        return
    with open("UniData.txt", 'w') as f2:
        json.dump(variables, f2, indent=3)


def RISE_info(): # more info
    with open("UniData.txt", 'r') as f:
        variables = json.load(f)
    if variables["color"] != 0:
        UI.Color_Rise()
    else:
        UI.RISE_icon()
    #UI.RISE_icon()
    WordCore.word_corey("@@@@", "", "@@@@\n")
    WordCore.word_corey("@@@@  ", "<<" + variables["gene[7]"] + ">>", "@@@@\n")
    WordCore.word_corey("@@@@", "  Nano-virus attaches to all vital organs of corpses and applies rapid surges to bring", "@@@@\n")
    WordCore.word_corey("@@@@", "  Them to a semi-living state, the energy drain takes away from the ability to", "@@@@\n")
    WordCore.word_corey("@@@@", "  Turna non-hijacked host into a zombie but will bring back infected persons", "@@@@\n")
    WordCore.word_corey("@@@@", "", "@@@@\n")
    WordCore.word_corey("@@@@  Affects: ", variables["influence[1]"], "@@@@\n")
    WordCore.word_corez("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")
    WordCore.word_corez("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")


def attribute_menu(): # This is the lab, where all genes are synthed and researched
    with open("UniData.txt", 'r') as f:
        variables = json.load(f)
    Clear.clear()
    UI.lux()
    WordCore.word_corez("@@@@  Welcome back to your lab!                                                                  @@@@\n")
    WordCore.word_corey("@@@@", "", "@@@@\n")
    WordCore.word_corey("@@@@ >>> EVOLVE | ", "Research genes to inject into your virus", "@@@@\n")
    WordCore.word_corey("@@@@", "", "@@@@\n")
    WordCore.word_corey("@@@@ >>> LEVEL | ", "Check the research level of gene paths", "@@@@\n")
    WordCore.word_corey("@@@@", "", "@@@@\n")
    WordCore.word_corey("@@@@ >>> INFO | ", "Study the possible gene paths", "@@@@\n")
    WordCore.word_corey("@@@@", "", "@@@@\n")
    WordCore.word_corey("@@@@ >>> LEAVE | ", "Leave your lab", "@@@@\n")
    WordCore.word_corey("@@@@", "", "@@@@\n")
    WordCore.word_corez("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")
    WordCore.word_corez("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")
    decide = input(str("Command: "))
    if decide == "INFO":
        Clear.clear()
        UI.lux()
        BURST_info()
        input(str("Press ENTER to continue..."))
        Clear.clear()
        UI.lux()
        NECROSIS_info()
        input(str("Press ENTER to continue..."))
        Clear.clear()
        UI.lux()
        WATER_info()
        input(str("Press ENTER to continue..."))
        Clear.clear()
        UI.lux()
        AIR_info()
        input(str("Press ENTER to continue..."))
        Clear.clear()
        UI.lux()
        BLOOD_info()
        input(str("Press ENTER to continue..."))
        Clear.clear()
        UI.lux()
        SALIVA_info()
        input(str("Press ENTER to continue..."))
        Clear.clear()
        UI.lux()
        ZOMBIFY_info()
        input(str("Press ENTER to continue..."))
        Clear.clear()
        UI.lux()
        RISE_info()
        input(str("Press ENTER to continue..."))
        Clear.clear()
        attribute_menu()
    elif decide == "LEVEL":
        Clear.clear()
        UI.lux()
        WordCore.word_corey("@@@@","  Burst Level: " + str(variables["burst"]), "@@@@\n")
        WordCore.word_corey("@@@@", "", "@@@@\n")
        WordCore.word_corey("@@@@", "  Necrosis Level: " + str(variables["necrosis"]), "@@@@\n")
        WordCore.word_corey("@@@@", "", "@@@@\n")
        WordCore.word_corey("@@@@", "  Water Level: " + str(variables["water"]), "@@@@\n")
        WordCore.word_corey("@@@@", "", "@@@@\n")
        WordCore.word_corey("@@@@", "  Air Level: " + str(variables["air"]), "@@@@\n")
        WordCore.word_corey("@@@@", "", "@@@@\n")
        WordCore.word_corey("@@@@", "  Blood Level: " + str(variables["blood"]), "@@@@\n")
        WordCore.word_corey("@@@@", "", "@@@@\n")
        WordCore.word_corey("@@@@", "  Saliva Level: " + str(variables["saliva"]), "@@@@\n")
        WordCore.word_corey("@@@@", "", "@@@@\n")
        WordCore.word_corey("@@@@", "  Zombify Level: " + str(variables["zombify"]), "@@@@\n")
        WordCore.word_corey("@@@@", "", "@@@@\n")
        WordCore.word_corey("@@@@", "  Rise Level: " + str(variables["rise"]), "@@@@\n")
        WordCore.word_corez("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")
        WordCore.word_corez("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")
        input(str("Press ENTER to continue..."))
        Clear.clear()
        attribute_menu()
    elif decide == "EVOLVE":
        Clear.clear()
        UI.lux()
        BURST_store_price()
        NECROSIS_store_price()
        WATER_store_price()
        AIR_store_price()
        BLOOD_store_price()
        SALIVA_store_price()
        ZOMBIFY_store_price()
        RISE_store_price()
        WordCore.word_corey("@@@@", "  " + variables["gene[0]"] + " | Research Cost: " + str(variables["burst_price"]), "@@@@\n")
        WordCore.word_corey("@@@@", "", "@@@@\n")
        WordCore.word_corey("@@@@", "  " + variables["gene[1]"] + " | Research Cost: " + str(variables["necrosis_price"]), "@@@@\n")
        WordCore.word_corey("@@@@", "", "@@@@\n")
        WordCore.word_corey("@@@@", "  " + variables["gene[2]"] + " | Research Cost: " + str(variables["water_price"]), "@@@@\n")
        WordCore.word_corey("@@@@", "", "@@@@\n")
        WordCore.word_corey("@@@@", "  " + variables["gene[3]"] + " | Research Cost: " + str(variables["air_price"]), "@@@@\n")
        WordCore.word_corey("@@@@", "", "@@@@\n")
        WordCore.word_corey("@@@@", "  " + variables["gene[4]"] + " | Research Cost: " + str(variables["blood_price"]), "@@@@\n")
        WordCore.word_corey("@@@@", "", "@@@@\n")
        WordCore.word_corey("@@@@", "  " + variables["gene[5]"] + " | Research Cost: " + str(variables["saliva_price"]), "@@@@\n")
        WordCore.word_corey("@@@@", "", "@@@@\n")
        WordCore.word_corey("@@@@", "  " + variables["gene[6]"] + " | Research Cost: " + str(variables["zombify_price"]), "@@@@\n")
        WordCore.word_corey("@@@@", "", "@@@@\n")
        WordCore.word_corey("@@@@", "  " + variables["gene[7]"] + " | Research Cost: " + str(variables["rise_price"]), "@@@@\n")
        WordCore.word_corey("@@@@", "", "@@@@\n")
        WordCore.word_corey("@@@@  RESEARCH POINTS | ", str(variables["dna_points"]), "@@@@\n")
        WordCore.word_corez("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")
        WordCore.word_corez("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")
        evo = input(str("Synthesize: "))
        if evo == variables["gene[0]"]:
            if variables["burst_price"] != '--':
                if variables["dna_points"] >= variables["burst_price"]:
                    Clear.clear()
                    variables["burst"] += 1
                    variables["lethality"] += 3
                    variables["severity"] += 25
                    variables["dna_points"] -= variables["burst_price"]
                    WordCore.word_corex(variables["gene[0]"] + " |", "Successfully synthesized!")
                    time.sleep(2)
                    Clear.clear()
                    attribute_menu()
                elif variables["dna_points"] <= variables["burst_price"]:
                    Clear.clear()
                    WordCore.word_corex(variables["gene[0]"] + " |", "Synthesis Failed!")
                    time.sleep(2)
                    Clear.clear()
                    attribute_menu()
                else:
                    attribute_menu()
            else:
                Clear.clear()
                WordCore.word_core("There is nothing more to research on this gene...", 0.01)
                time.sleep(1)
                attribute_menu()
        elif evo == variables["gene[1]"]:  # // passive
            if variables["necrosis_price"] != '--':
                if variables["dna_points"] >= variables["necrosis_price"]:
                    Clear.clear()
                    variables["necrosis"] += 1
                    vriables["severity"] += 10
                    variables["dna_points"] -= variables["necrosis_price"]
                    WordCore.word_corex(variables["gene[1]"] + " |", "Successfully synthesized!")
                    time.sleep(2)
                    Clear.clear()
                    attribute_menu()
                elif variables["dna_points"] <= variables["necrosis_price"]:
                    Clear.clear()
                    WordCore.word_corex(variables["gene[1]"] + " |", "Synthesis Failed!")
                    time.sleep(2)
                    Clear.clear()
                    attribute_menu()
                else:
                    attribute_menu()
            else:
                Clear.clear()
                WordCore.word_core("There is nothing more to research on this gene...", 0.01)
                time.sleep(1)
                attribute_menu()
        elif evo == variables["gene[2]"]:
            if variables["water_price"] != '--':
                if variables["dna_points"] >= variables["water_price"]:
                    Clear.clear()
                    variables["water"] += 1
                    variables["dna_points"] -= variables["water_price"]
                    WordCore.word_corex(variables["gene[2]"] + " |", "Successfully synthesized!")
                    WATER_check()
                    time.sleep(2)
                    Clear.clear()
                    attribute_menu()
                elif variables["dna_points"] <= variables["water_price"]:
                    Clear.clear()
                    WordCore.word_corex(variables["gene[2]"] + " |", "Synthesis Failed!")
                    time.sleep(2)
                    attribute_menu()
                else:
                    attribute_menu()
            else:
                Clear.clear()
                WordCore.word_core("There is nothing more to research on this gene...", 0.01)
                time.sleep(1)
                attribute_menu()
        elif evo == variables["gene[3]"]:
            if variables["air_price"] != '--':
                if variables["dna_points"] >= variables["air_price"]:
                    Clear.clear()
                    variables["air"] += 1
                    variables["dna_points"] -= variables["air_price"]
                    WordCore.word_corex(variables["gene[3]"] + " |", "Successfully synthesized!")
                    AIR_check()
                    time.sleep(2)
                    Clear.clear()
                    attribute_menu()
                elif variables["dna_points"] <= variables["air_price"]:
                    clear.clear()
                    WordCore.word_corex(variables["gene[3]"] + " |", "Synthesis Failed!")
                    time.sleep(2)
                    Clear.clear()
                    attribute_menu()
                else:
                    attribute_menu()
            else:
                Clear.clear()
                WordCore.word_core("There is nothing more to research on this gene...", 0.01)
                time.sleep(1)
                attribute_menu()
        elif evo == variables["gene[4]"]:
            if variables["blood_price"] != '--':
                if variables["dna_points"] >= variables["blood_price"]:
                    Clear.clear()
                    variables["blood"] += 1
                    variables["dna_points"] -= variables["blood_price"]
                    WordCore.word_corex(variables["gene[4]"] + " |", "Successfully synthesized!")
                    BLOOD_check()
                    time.sleep(2)
                    Clear.clear()
                    attribute_menu()
                elif variables["dna_points"] <= variables["blood_price"]:
                    Clear.clear()
                    WordCore.word_corex(variables["gene[4]"] + " |", "Synthesis Failed!")
                    time.sleep(2)
                    Clear.clear()
                    attribute_menu()
                else:
                    attribute_menu()
            else:
                Clear.clear()
                WordCore.word_core("There is nothing more to research on this gene...", 0.01)
                time.sleep(1)
                attribute_menu()
        elif evo == variables["gene[5]"]:
            if variables["saliva_price"] != '--':
                if variables["dna_points"] >= variables["saliva_price"]:
                    Clear.clear()
                    variables["saliva"] += 1
                    variables["dna_points"] -= variables["saliva_price"]
                    WordCore.word_corex(variables["gene[5]"] + " |", "Successfully synthesized!")
                    SALIVA_check()
                    time.sleep(2)
                    Clear.clear()
                    attribute_menu()
                elif variables["dna_points"] <= variables["saliva_price"]:
                    Clear.clear()
                    WordCore.word_corex(variables["gene[5]"] + " |", "Synthesis Failed!")
                    time.sleep(2)
                    Clear.clear()
                    attribute_menu()
                else:
                    attribute_menu()
            else:
                Clear.clear()
                WordCore.word_core("There is nothing more to research on this gene...", 0.01)
                time.sleep(1)
                attribute_menu()
        elif evo == variables["gene[6]"]:  # // passive
            if variables["zombify_price"] != '--':
                if variables["dna_points"] >= variables["zombify_price"]:
                    Clear.clear()
                    variables["zombify"] += 1
                    variables["dna_points"] -= variables["zombify_price"]
                    WordCore.word_corex(variables["gene[6]"] + " |", "Successfully synthesized!")
                    time.sleep(2)
                    Clear.clear()
                    attribute_menu()
                elif variables["dna_points"] <= variables["zombify_price"]:
                    Clear.clear()
                    WordCore.word_corex(variables["gene[6]"] + " |", "Synthesis Failed!")
                    time.sleep(2)
                    Clear.clear()
                    attribute_menu()
                else:
                    attribute_menu()
            else:
                Clear.clear()
                WordCore.word_core("There is nothing more to research on this gene...", 0.01)
                time.sleep(1)
                attribute_menu()
        elif evo == variables["gene[7]"]:
            if variables["rise_price"] != '--':
                if variables["dna_points"] >= variables["rise_price"]:
                    Clear.clear()
                    variables["rise"] += 1
                    variables["dna_points"] -= variables["rise_price"]
                    WordCore.word_corex(variables["gene[7]"] + " |", "Successfully synthesized!")
                    RISE_check()
                    time.sleep(2)
                    Clear.clear()
                    attribute_menu()
                elif variables["dna_points"] <= variables["rise_price"]:
                    Clear.clear()
                    WordCore.word_corex(variables["gene[7]"] + " |", "Synthesis Failed!")
                    time.sleep(2)
                    Clear.clear()
                    attribute_menu()
                else:
                    attribute_menu()
            else:
                Clear.clear()
                WordCore.word_core("There is nothing more to research on this gene...", 0.01)
                time.sleep(1)
                attribute_menu()
        else:
            attribute_menu()
    elif decide == "LEAVE":
        Clear.clear()
        print("Goodbye!\n")
        time.sleep(0.4)
        Clear.clear()
        player_menu()
    else:
        Clear.clear()
        attribute_menu()


def exit_game(): # Gotta quit sometime, right?
    Clear.clear()
    WordCore.word_core("You have chosen to exit the game... Are you sure? [y]/[n]", 0.05)
    print("\n")
    ans = input(str())
    print("\n")
    if ans in ["Y", "y", "Yes", "yes", "YES"]:
        WordCore.word_core("Exiting game...", 0.05)
        print("\n")
        Clear.clear()
        return
    elif ans in ["n", "N", "no", "NO", "No"]:
        WordCore.word_core("Not Exiting The Game...", 0.05)
        print("\n")
        Clear.clear()
        player_menu()
    else:
        exit_game()


def player_menu():
    Clear.clear()
    with open("UniData.txt", 'r') as f:
        variables = json.load(f)
    if variables["color"] != 0:
        UI.Color_lux()
        UI.Color_player_menu_UI()
        answer = input(str(Green_Blackxx + "Command: "))
        print(Reset, end='')
    else:
        UI.lux()
        UI.player_menu_UI()
        answer = input(str("Command: "))
    if answer == "WORLD":
        Clear.clear()
        if variables["color"] != 0:
            Graph.color_graphical_analysis()
        else:
            Graph.graphical_analysis()
        player_menu()
    elif answer == "VIRUS":
        Clear.clear()
        if variables["color"] != 0:
            Graph.color_plague_status_graph()
        else:
            Graph.plague_status_graph()
        player_menu()
    elif answer == "LAB":
        Clear.clear()
        attribute_menu()
    elif answer == "TURN":
        Clear.clear()
        turn()
    elif answer == "FAST":
        Clear.clear()
        fast_turn()
    elif answer == "SAVE":
        Clear.clear()
        WordCore.word_core("SAVING | ", 0.1)
        save_1()
        print("Save completed successfully")
        time.sleep(2)
        Clear.clear()
        player_menu()
    elif answer == "LOAD":
        Clear.clear()
        WordCore.word_core("LOADING | ", 0.1)
        load_1()
        print("Loading complete...")
        time.sleep(2)
        Clear.clear()
        player_menu()
    elif answer == "EXIT":
        Clear.clear()
        exit_game()
    else:
        player_menu()


def turn():
    Clear.clear()
    with open("UniData.txt", 'r') as f:
        variables = json.load(f)
        #variables["week"] += 1
        #f.close()
    variables["week"] += 1
    with open("UniData.txt", 'w') as f2:
        json.dump(variables, f2, indent=3)
        #f2.close()
    WordCore.word_core("A new week has come...", 0.01)
    print("\n")
    print("Week Number: " + str(variables["week"]))
    Generation.dna_weekly()
    Generation.dna_random()
    infecting_agent()
    check_cure_start()
    BURST_check()
    NECROSIS_check()
    ZOMBIFY_check()
    enforce_value_maximums()
    print("\n")
    Graph.graphical_analysis_mini()
    #time.sleep(3)
    player_menu()


def turn_fast():
    Clear.clear()
    with open("UniData.txt", 'r') as f:
        variables = json.load(f)
    variables["week"] += 1
    with open("UniData.txt", 'w') as f2:
        json.dump(variables, f2, indent=3)
    print("A new week has come...")
    print("\n")
    print("Week Number: " + str(variables["week"]))
    Generation.dna_weekly()
    Generation.dna_random()
    infecting_agent()
    check_cure_start()
    BURST_check()
    NECROSIS_check()
    ZOMBIFY_check()
    enforce_value_maximums()
    Game_Over()
    print("\n")


def fast_turn():
    WordCore.word_core("Press ENTER to take a turn...", 0.1)
    print("\n")
    WordCore.word_core("Type STOP to go back to Player Menu...", 0.1)
    print("\n")
    while True:
        turn_fast()
        inp = input(str())
        if inp == "STOP":
            player_menu()


def Save_Check():
    with open("UniData.txt", 'r') as file:
        variables = json.load(file)
    if variables["old"] == 1:
        load_3()
        Clear.clear()
        player_menu()
    else:
        load_3()
        variables["old"] = 1
        with open("UniData.txt", 'w') as f2:
            json.dump(variables, f2, indent=3)
        start_turn()


def start_turn():
    Clear.clear()
    with open("UniData.txt", 'r') as f:
        variables = json.load(f)
    if variables["color"] != 0:
        UI.Color_Mail()
        UI.intro_sq_c_nano()
        input(str(Green_Blackxx + "press ENTER to exit Magus..."))
        print(Reset, end='')
        #time.sleep(3)
        #answer = input(str(Green_Blackxx + "Command: "))
    else:
        UI.mail()
        UI.intro_sq()
        input(str("press ENTER to exit Magus..."))
        #answer = input(str("Command: "))
    player_menu()


def Game_Over():
    with open("UniData.txt", 'r') as f:
        variables = json.load(f)
    if variables["healthy"] <= 0:
        if variables["infected"] <= 0:
            victory()
        else:
            return
    if variables["infected"] <= 0:
        if variables["zombies"] <= 0:
            infected_game_over()
        else:
            return
    if variables["cure"] >= 1000:
        Clear.clear()
        cured_game_over()
    else:
        return


def infected_game_over():
    Clear.clear()
    UI.infected_game_over_icon()
    time.sleep(1)
    print("\n")
    WordCore.word_corex("NO INFECTED |", "All infected have been exterminated....")
    print("\n")
    WordCore.word_corex("NO ZOMBIES |", "All zombies have been exterminated...")
    time.sleep(1)
    print("\n")
    WordCore.word_corex("CURE COMPLETE |", "All infected have been cured and zombies quarentined....")
    print("\n")
    input(str("Press ENTER to continue...."))
    gc.collect()
    Clear.clear()


def cured_game_over(): # You got cured
    Clear.clear()
    UI.cured_game_over_icon()
    time.sleep(1)
    print("\n")
    WordCore.word_corex("CURE COMPLETE |", "All infected have been cured and zombies quarentined....")
    print("\n")
    input(str("Press ENTER to continue...."))
    gc.collect()
    Clear.clear()


def victory(): # Everyone dies
    Clear.clear()
    UI.victory_icon()
    WordCore.word_corex("VICTORY |", "All life on earth, except you and your select, have been exterminated")
    input(str("Press ENTER to continue...."))
    gc.collect()

