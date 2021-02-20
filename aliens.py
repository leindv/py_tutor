# Иногда требуется сохранить множество словарей в 
# списке или сохранить список как значение элементов 
# словаря. Создание сложных структур такого рода 
# называется "ВЛОЖЕНИЕ".
# В точке 1 каждый словарь заносится в список ALIENS.
#
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2] #1
for alien in aliens:
    print(alien)
