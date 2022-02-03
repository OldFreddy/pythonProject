users = ['Admin', 'user1', 'user2', 'user3', 'user4']
#user = []
if users:
    for user in users:
        if user == 'Admin':
            print('Hello admin, would you like to see a status report?')
        else:
            print(f'Hello {user}')
else:
    print("Скисок пользователей пуст")