person_0 = {'name': 'Nikitos', 'age': 23}
print(person_0.get('name'))
print(person_0['name'].upper())
print(person_0.get('status'))

person_1 = {'name': 'Vova', 'age': 32}
person_2 = {'name': 'Misha', 'age': 32}

peoples = [person_0, person_1, person_2]

for human in peoples:
    person_name = human.get('name')
    person_age = human.get('age')

    print(f"User name is {person_name} ang the age is {person_age}")