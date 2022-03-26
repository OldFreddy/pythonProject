pet_1 = {'name': 'sharik', 'type': 'dog', 'owner': 'misha' }
pet_2 = {'name': 'losharik', 'type': 'fish', 'owner': 'vova' }
pet_3 = {'name': 'piska', 'type': 'cat', 'owner': 'nik' }

pets = [pet_1, pet_2, pet_3]

for pet in pets:
    name = pet['name']
    type = pet['type']
    owner = pet['owner']
    print(f'\nMy name is {name.title()}, my type is {type.upper()}, my owner is {owner.title()}')
