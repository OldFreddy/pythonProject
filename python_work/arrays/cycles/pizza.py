pizzas = ['pepperronni', 'mozzarrellla', 'fucking_pizza']
for pizza in pizzas:
    print(pizza)

for pizza in pizzas:
    print(f'I like {pizza} pizza')

friends_pizzas = pizzas[:]
pizzas.append("new_pizza")
friends_pizzas.append('anotherPizza')

for pizza in pizzas:
    print(f'My favorite pizza are {pizza}')

for pizza in friends_pizzas:
    print(f'my friend`s favorite pizza are {pizza}')