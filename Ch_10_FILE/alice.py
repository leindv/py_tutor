# Обработка исключения FileNotFoundError.

# Файл alice.txt в рабочей директории в частности и 
# на компе вообще не существует, используемый аргумет 
# encoding необходим в том случае, когда кодировка 
# нашей системы по умолчанию не совпадает с кодировкой 
# читаемого файла.


filename = 'alice.txt'

with open (filename, encoding = 'uef-8') as f:
    contents = f.read()