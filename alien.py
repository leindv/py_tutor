# Прога начинается с определения словаря 
# с выводом снимка текущего его состояния. 
# В точке 1 в словарь добавляется новая пара 
# "ключ-значение"; ключ x_position и значение 0. 
# То же делается в точке 2. 

alien_0 = {'color': 'green', 'points': 5}
print(alien_0) 
alien_0['x_position'] = 0 #1
alien_0['y_position'] = 25 #2
print(alien_0)
