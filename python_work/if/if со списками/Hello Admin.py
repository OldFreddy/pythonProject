users = ['Admin', 'user1', 'user2', 'user3', 'user4']
# user = []
if users:
    for user in users:
        if user == 'Admin':
            print('Hello admin, would you like to see a status report?')
        else:
            print(f'Hello {user}')
else:
    print("Скисок пользователей пуст")

current_users = ['User1', 'user2', 'user3', 'user4', 'user5']
new_users = ['user1', 'user2', 'user6', 'user7', 'user8']
current_users_lower_case = []
for user in current_users:
    current_users_lower_case.append(user.lower())
for user in new_users:
    if user in current_users_lower_case:
        print(f'пользователь с именем {user} уже есть, выберите новое имя')
    else:
        print(f'имя {user} свободно, можешь юзать его')