# Необходимо превратить ПЕРВЫХ ТРЕХ пришельцев из проги 
# в предыдущем коммите в желтых, которые двигаются со 
# средней скоростью и приносят по 10 очков, то можно действовать 
# как в точке (1).
#

# Создание пустого списка для хранения пришельцев:
aliens = []

# Создвние 30 зеленых пришельцев.
for alien_number in range(30): 
    new_alien ={'color': 'green', 'points': 5, 'speed': 'slow'} 
    aliens.append(new_alien)

for alien in aliens[0:3]: #1
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

# Вывод первых пяти пришельцев:
for alien in aliens[:5]: 
    print(alien)
print('...')

# Вывод количества созданных пришельцев.
print(f"Total number of aliens: {len(aliens)}") 
