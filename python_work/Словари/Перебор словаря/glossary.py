glossary = {
    'Массив': 'массив',
    'Переменная': 'переменная',
    'Ключ': 'ключ',
    'Значение': 'значение',
    'Словарь': 'словарь',
}

for znachenie in glossary.keys():
    znachenie_value = glossary.get(znachenie, 'default')
    print(f'{znachenie} это {znachenie_value}')

print('____________________________')

glossary = {
    'Массив': 'массив',
    'Переменная': 'переменная',
    'Ключ': 'ключ',
    'Значение': 'значение',
    'Словарь': 'словарь',
}

for key, value in glossary.items():
    print(f'{key} - это {value}')
