cities = {
    'Rostov': {
        'country': 'Russia',
        'population': 1000000,
        'fact': 'trade city'
    },
    'Moscow': {
        'country': 'Russia',
        'population': 12000000,
        'fact': 'zalupa'
    },
    'New York': {
        'country': 'USA',
        'population': 30000000,
        'fact': 'GOOD'
    }
}

for city, info in cities.items():
    print(f"\ncity is {city} \n\tcountry is {info['country']}, \n\tpopulation is {info['population']}, \n\tfact is {info['fact']}")