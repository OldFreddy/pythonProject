flag_to_quit = False
names_and_places = {}
while not flag_to_quit:
    name = input('\nEnter your name: ')
    place = input('Enter your favorite place: ')
    want_to_quit = input('do you want to quit? y/n')

    names_and_places[name] = place

    if want_to_quit == 'y':
        flag_to_quit = True
print(names_and_places)