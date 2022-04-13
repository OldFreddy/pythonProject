def build_profile(name, lastName, **userInfo):
    """Строит словарь с информацией о пользователе"""
    userInfo['first_name'] = name
    userInfo['last_name'] = lastName
    return userInfo


user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
user_profile_1 = build_profile('Misha', 'MISHA', location='Rostov', field='Music')

print(user_profile)
print(user_profile_1)
