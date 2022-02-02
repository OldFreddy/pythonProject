requested_toppings = ['mushrooms', 'green pappers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green pappers':
        print('Sorry? we are not have green papper now')
    else:
        print(f'Adding {requested_topping}')
print('\nFinished making your pizza!')

requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}")
else:
    print('Уверен, что хочешь пиццу без ничего?')


