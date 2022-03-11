rivers = {
    'nile': 'egypt',
    'oka': 'russia',
    'moskva': 'russia',
    'potomak': 'usa'
}

for key, value in rivers.items():
    print(f'The {key.title()} runs through {value.title()}')

print('_____________________________')

for river in rivers.keys():
    print(river.title())