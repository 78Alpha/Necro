healthy = 100000
infected = 1 # Must have at least 1 infected
zombies = 0
dead = 0
cure = 0 # Limit of 1000
week = 0

influence = ["Infectivity", "Severity", "Lethality"]
infectivity = 0 #Max of 10000
infectivity_limit = 10000
severity = 0 #Max of 100
severity_limit = 100
lethality = 0 #Max of 10
lethality_limit = 10
weekly_infections = 10
dna_points = 0
burst = 0 #Max of 1
burst_price = 10 #base price
necrosis = 0 #Max of 1
necrosis_price = 20 #base price
water = 0 #Max of 3
water_price = 10 #base price
air = 0 #Max of 3
air_price = 10 #base price
blood = 0 #Max of 2
blood_price = 20 #base price
saliva = 0 #Max of 2
saliva_price = 20 #base price
zombify = 0 #Max of 1
zombify_price = 20 #base price
rise = 0 #Max of 5
rise_price = 20 #base price
gene = ["BURST", "NECROSIS", "WATER", "AIR", "BLOOD", "SALIVA", "ZOMBIFY", "RISE"]
limit = int(healthy + infected + dead + zombies)
