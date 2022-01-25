players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3]) #вывод диапазона с первого по третий элемент

print(players[1:4]) #со второго по четвертый

print(players[:4]) #с начала по четвертый

print(players[2:]) #c третьего до конца

print(players[-3:]) #выводит трех последних игроков


print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())