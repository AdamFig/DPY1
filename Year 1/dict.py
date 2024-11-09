import os
os.system('clear')

# Problem 1: Create a Colony Dictionary

thalaxion_colony = {
    'name': "New Horizon",
    'population': 5000,
    'resources': ["water", "minerals", "oxygen"],
    'established': 2120
}
print(thalaxion_colony)

# Problem 2: Access Colony Information

colony_name = thalaxion_colony['name']
colony_established = thalaxion_colony['established']

print(f"The {colony_name} colony was established in {colony_established}.")

# Problem 3: Update the Population and Add a New Resource

thalaxion_colony['population'] += 1000
thalaxion_colony['resources'].append('Helium-3')
print(thalaxion_colony)

thalaxion_colony['resources'].remove('water')
print(thalaxion_colony)

if 'population' in thalaxion_colony:
    print("Population is a key in the dictionary.")
else:
    print("Population is not a key in the dictionary.")

if 'climate' in thalaxion_colony:
    print("Climate is a key in the dictionary.")
else:
    print("Climate is not a key in the dictionary.")

# Problem 6: Iterate Over the Colony Data

for key in thalaxion_colony:
    print(key)

for value in thalaxion_colony.values():
    print(value)

for key, value in thalaxion_colony.items():
    print(f"Key: {key} - Value: {value}")

# Problem 7: Merging Two Colonies - I can't figure out how to do this

neighboring_colony = {
    "name": "Frontier Base",
    "population": 3000,
    "resources": ["oxygen", "silica"]
}

for key, value in thalaxion_colony.items():
    if key == "resources":
        thalaxion_colony[key] += neighboring_colony[key]
    else:
        thalaxion_colony[key] = neighboring_colony[key]
print(thalaxion_colony)



# Problem 8: Refining the Dictionary After Merging - I can't figure out how to do P7 so I can't do P8.



# I'll come back to this later, because I really need to review physics right now.