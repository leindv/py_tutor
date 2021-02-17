# Еще один пример перебора всех пар "ключ-значение" 
# из где-то предыдущего коммита.
#
favorit_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
for name, language in favorit_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")
