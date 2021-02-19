# Если перебор пары ключ значение применяется метод 
# items(), то для перебора всех ключей в словаре 
# используется метод keys().
# 
#
favorit_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
for name in favorit_languages.keys():
    print(name.title())
