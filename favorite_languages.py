# Перебор ключей в определенном порядке, который 
# основан на сортировке ключей , возвращаемых циклом FOR.
# Здесь используется sorted(), вкоторую включен метод keys().
#
favorit_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
for name in sorted(favorit_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")
