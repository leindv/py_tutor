# Перебор всех значений в словаре - применение метода
# values().
#
favorit_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
print("The following languages have been mentoned:")
for language in favorit_languages.values():
    print(language.title())
