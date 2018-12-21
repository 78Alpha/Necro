import json

with open("data.txt", 'r') as file:
    variables = json.load(file)

print(variables)
print(variables["gene"])
#print(variables["gene"[0]])
print(variables["gene[0]"])