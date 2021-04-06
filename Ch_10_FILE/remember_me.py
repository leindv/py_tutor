# Сохранение и чтение данных, сгенерированных пользователем.

# В (1) прога запрашивает данные пользователя для сохранения.
# Затем вызывается функция json.dump(), которой передается имя 
# пользователя и объект файла;  функция сохраняет имя пользователя 
# в файле (2).
# Далее выводиться сообщение о том, что имя пользователя сохранено (3).

import json

username = input("Wtat is your name? ") #1

filename = 'username.json'
with open(filename, 'w') as f:
    json.dump(username, f) #2
    print(f"We shell remember you when you come back, {username}!") #3