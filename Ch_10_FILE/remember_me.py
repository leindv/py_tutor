# Сохранение и чтение данных, сгенерированных пользователем.

# Теперь объединим эти две проги из предыдущих коммитов в одну.
#

# В (1) прога пытается открыть файл username.json. Если файл 
# существует, прога читает имя пользователя в память (2) и 
# выводит приветсвенное сообщение в блоке else.
# Если прога запускается впервые, то файл username.json не 
# существует и проиходит исключение FileNotFoundError (3). 
# Прога переходит к блоку except, в котором пользователю 
# предлагают ввести имя (4).
# Затем прога вызывает json.dump() для сохранения и 
# вывода приветсвия (5).

import json

# Программа загружает имя пользователя, если оно было сохранено ранее.
# В противном случаеоно запрашивает имя пользователя и сохраняет его.
filename = 'username.json'
try:
    with open(filename) as f: #1
        username = json.load(f) #2
except FileNotFoundError: #3
    username = input('What is your name? ') #4
    with open(filename, 'w') as f: #5
        json.dump(username, f)
        print(f"We shell remember you when you com back, {username}!")
else:
    print(f"Welcom back, {username}!")
