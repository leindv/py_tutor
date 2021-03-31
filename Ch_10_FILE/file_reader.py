# Чтение по строкам.

# В точке (1) имя файла , из которого читается инфо, 
# сохраняется в переменной.
# После вызова open() объект, представляющий файл и 
# его содержимое, сохраняется в переменной 
# file_object (2).
# Мы снова используем синтаксис with, чтобы поручить 
# проге открывать и закрывать файл в нужный момент.
# Для просмотра содержимого все строки файла 
# перебираются в цикле for по объекту файла (3).

# После добавления вызова rstrip() (4) в команде 
# print лишние строки удаляются.


filename = 'pi_digits.txt' #1
with open(filename) as file_object: #2
    for line in file_object: #3
        print(line.rstrip()) #4
