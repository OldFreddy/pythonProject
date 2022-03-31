sandwich_order = ['sandwich1', 'pastrami', 'sandwich2', 'pastrami', 'sandwich3', 'pastrami']
print(sandwich_order)
print('Pastrami not now')
while 'pastrami' in sandwich_order:
    sandwich_order.remove('pastrami')
print(sandwich_order)

    

finished_sandwiches =[]
while sandwich_order:
    current_sandwich = sandwich_order.pop()
    print(f'I made you {current_sandwich}')
    finished_sandwiches.append(current_sandwich)
print(finished_sandwiches)