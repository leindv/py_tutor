# РЕФАКТОРИНГ - процесс уссовершенствования кода путем 
# разбиения его на функции, каждая из которых решает 
# свою конкретную задачу.

# С переходом на функцию комментарии дополняются строкой, 
# которые описывают работу кода в текущей версии (1).
# Однако функция greet_user() из предыдущего коммита не только 
# приветсвует пользователя - она также загружает хранимое имя 
# пользователя, если оно существует, и запрашивает новое имя, 
# если оно не было сохранено ранее.
# Поэтом здесь переработаем функцию greet_user().  

# 

import json

def get_stored_username():
    """Получает хранимое имя пользователя, если оно существует""" #1
    filename = 'username.json'
    try:
        with open(filename) as f: 
            username = json.load(f) 
    except FileNotFoundError: 
        return None #2
    else:
        return username

def greet_user():
    """Приветствует пользователя по имени."""
    username = get_stored_username()
    if username: #3
        print(f"Welcome back, {username}!")
    else:
        username = input('What is your name? ') 
        with open(filename, 'w') as f: 
            json.dump(username, f)
            print(f"We shell remember you when you com back, {username}!")

greet_user()

