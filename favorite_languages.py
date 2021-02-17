# Этот синтаксис применяется для получения 
# соответсвующего ЗНАЧЕНИЯ из словаря (1) с 
# присвоением ему переменной language, 
# для дальнейшего упращения вывода 
# командой print.
#
favorit_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
language = favorit_languages['sarah'].title() #1
print(f"Sarah's favorite language is {language}.")
