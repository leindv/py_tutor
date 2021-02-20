# Перебор всех значений в словаре - применение метода
# values(). Возможны ситуации, когда значения в словаре 
# дублируются, и необходимо в проге эти дубликаты исключить.
# В этом случае применяется метод SET() - множество - этот 
# метод исключает дублирование. В точке 1 set() используется 
# для извлечения уникальных данных.
#
favorit_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
print("The following languages have been mentoned:")
for language in set(favorit_languages.values()): #1
    print(language.title())
