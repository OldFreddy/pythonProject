alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

#автосоздание 30 пришельцев

aliens = []
for alien_number in range(300):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

#Вывод первых 5 пришельцев
for alien in aliens[:5]:
    print(alien)

# Вывод количества созданных пришельцев
print(f"Total number of aliens: {len(aliens)}")

