# Словарь в словаре.
# В проге определяется словарь, содержащий два ключа.
# В процессе перебора словаря (1) прога сохраняет каждый 
# ключ в переменной username, а словарь с каждым именем 
# пользователя сохраняется в переменной user_info. 
# Внутри основного цикла в словаре выводится имя 
# пользователя (3). В точке 3 начинается работа с 
# внутренним словарем. Переменная user_info содержит 
# словарь с инфо о пользоватеое, который содержит три ключа 
# 'first', 'last' и 'location', каждый из которых 
# используется для построения аккуратно отформатированных 
# данных.
#
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris'
        },
    }
for username, user_info in users.items(): #1
    print(f"\nUsername: {username}") #2
    full_name =f"{user_info['first']} {user_info['last']}" #3
    location =user_info['location']
    print(f"\tFull name: {full_name.title()}") #4
    print(f"\tLocation: {location.title()}")
