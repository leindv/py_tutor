# СОХРАНЕНИЕ ДАННЫХ.

# Функции json dump() и json load().

# Функция json load() используется для чтения списка обратно в память.

# В (1) для чтения используется тот же файл, который был создан 
# в файле number_writer.py, но открывается в режиме чтения (2).
# В (3) функция json.load() используется для загрузки инфо из 
# файла numbers.json, эта инфо сохраняется в переменной numbers.



import json
filename = 'numbers.json'#1
with open(filename) as f: #2
    numbers = json.load(f) #3
print(numbers)
