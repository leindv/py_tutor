# РЕФАКТОРИНГ - процесс уссовершенствования кода путем 
# разбиения его на функции, каждая из которых решает 
# свою конкретную задачу.

# С переходом на функцию комментарии дополняются строкой, 
# которые описывают работу кода в текущей версии (1).


import json

def greet_user():
    """Приветсвует пользователя по имени.""" #1
    filename = 'username.json'
    try:
        with open(filename) as f: 
            username = json.load(f) 
    except FileNotFoundError: #3
        username = input('What is your name? ') 
        with open(filename, 'w') as f: 
            json.dump(username, f)
            print(f"We shell remember you when you com back, {username}!")
    else:
        print(f"Welcom back, {username}!")
greet_user()

