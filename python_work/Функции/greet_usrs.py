def greet_users(names):
    """Вывод простого приветствия для каждого пользователя из списка """
    for name in names:
        msg = f"Hello {name.title()}"
        print(msg)


usernames = ['hannah', 'john', 'boba']

greet_users(usernames)
