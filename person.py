# Возвращение словаря.
# Функция получает имя и фамилию и сохраняет полученное значение 
# в словаре (1). Весь словарь с описанием человека возвращается 
# в точке 2. Возвращаемое значение выводится в точке 3.
#
#
def build_person(first_name, last_name):
    """Возвращает словарь с инфо о человеке."""
    person = {'first':first_name, 'last':last_name} #1
    return person #2

musicant = build_person('jimi', 'hendrix')
print(musicant) #3
