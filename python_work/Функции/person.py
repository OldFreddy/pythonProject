def build_person(first_name, last_name, age=None):
    """Возвращает словарь"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


musician = build_person('jimmi', 'hendrix')
print(musician)

musician = build_person('jimmi', 'hendrix', age=27)
print(musician)
