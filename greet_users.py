# ПЕРЕДАЧА СПИСКА.
# Функция greet_users() рассчитывает получить список имен,
# который сохраняется в парамете nemes. Функция перебирает 
# полученный список и выводит приветсвие для каждого пользователя.
# В (1) мы определяем список пользователей usernames, который
# затем передается greet_users() в вызове функциии.
#
#
def greet_users(names):
    """Вывод простого приветсвия."""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

usernames = ['hannah', 'ty', 'margot'] #1
greet_users(usernames) 