from random import randint, choice

print("Вывод случайного целого числа ", randint(0, 9))

players = ['player1', 'martina', 'condor', 'volosach', 'vipusknik']

first_up = choice(players)

print(first_up)
