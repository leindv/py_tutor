# Использование произвольного набораименнованых аргументов.
# Функция build_profile() всегда получит имя и фамилию.
# но также может получить произвольное количество ИМЕННОВАННЫХ
# АРГУМЕНТОВ в виде пар "кимя-значение". В теле build_profile()
# в словарь user_info добавляется имя и фамилия, потому что эти 
# два значения вскегда передаются пользователем (1) и они еще не 
# были помещены в словарь. Затем словарь user_info ВОЗВРАЩАЕТСЯ в
# точкувызова функции.
# Вызовем функцию build_profile() и передадим ей имя, фамилию 
# и ЕЩЕ ДВЕ ПАРЫ "ключ-значение" - location = 'princerton' и 
# field = 'physics'. Программа сохраняет возвращенный словарь в 
# user_profile и выводи ее содержимое.
#
#
def build_profile(first, last, **user_info):
    """Строит словарь с информацией о пользователе."""
    user_info['first_name'] = first #1
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein', 
                            location = 'princerton',
                            field = 'physics')
print(user_profile)
