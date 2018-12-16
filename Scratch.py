with open('UniData.py', 'r') as file:
    data = file.readlines()
data[1] = "hp = " + str(96) + "\n"
with open("UniData.py", 'w') as file:
    file.writelines(data)
