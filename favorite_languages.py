# Метод keys() можно использовать для проверки того, 
# учствовал ли конкретный человек в опросе.
# Метод keys() не ограничивает перебором: он возвращает  
# список всех ключей, и строка 1 просто проверяет, входит 
# ли ключ 'erin' в список.
#
favorit_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
if 'erin'not in favorit_languages.keys():
    print("Erin, please take out poll!" ) #1
friends = ['phil', 'sarah'] 
for name in favorit_languages.keys(): 
    print(name.title())
    if name in friends: 
        language = favorit_languages[name].title() 
        print(f"\t{name.title()}, I see you love {language}")
