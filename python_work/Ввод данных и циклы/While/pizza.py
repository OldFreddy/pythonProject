topping = ''
while topping != 'quit':
    topping = input('Введите топпинг или выйдите из приложения')
    if topping != 'quit':
        print(f'Вы добавили {topping}')