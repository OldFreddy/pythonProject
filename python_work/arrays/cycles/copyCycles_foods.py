my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods=my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print('my favorite foods are: ')
print(my_foods)

for food in my_foods:
    print(f'foods is {food}')

print('\n my friend`s favorite foods are: ')
print(friend_foods)