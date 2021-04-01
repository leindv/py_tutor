# Присоединение данных к файлу.

# В точке (1) аргумент 'a' используется для открытия файла 
# в режиме ПРИСОЕДИНЕНИЯ.
# (вместо перезаписи существующего файла). В (2) записываются 
# две новые стоки, добавляющиеся к содержимому txt-файл.

filename = 'programming.txt'

with open(filename, 'a') as file_object: #1
    file_object.write('I also love finding meaning in large datasets.\n') #2
    file_object.write('I love creating apps thet can run in a browser.\n')

