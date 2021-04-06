# Сохранение и чтение данных, сгенерированных пользователем.

# Если прога remember_me.py сохраняет имя пользователя в файле 
# username.json при помощи функции json.dump(),
# то программа ниже приветсвует пользователя по ранее 
# сохраненному имени.

# В (1) вызов json.load() читает информацию из файла 
# username.json в переменную username.
# После того как данные успешно прочитаны, прога 
# приветсвует (2).

import json

filename = 'username.json'

with open(filename) as f:
    username = json.load(f) #1
    print(f"Welcome back, {username}!") #2
