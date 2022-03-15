users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },

    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

for username, userIinfo in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{userIinfo['first']} {userIinfo['last']}"
    location = userIinfo['location']
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")