# Данная прога предназначена для проверки правильности работы функции 
# get_formatted_name(), расположенной в файле name_function.py (Ex. 1).
# Данная функция строит полное имя и фамилию, разделив их пробелами и 
# преобразуя первый символы слов в заглавные буквы.

# Проверка проводится путем импорта функции get_formatted_name() из модуля 
# name_function.

from name_function import get_formatted_name

print("Enter 'q' at any time ti quit.")
while True:
    first = input("\nPlease give me a first name: ")
    if first =='q':
        break
    last = input("Please give me a last name: ")
    if last =='q':
        break

    formatted_name = get_formatted_name(first, last)
    print(f"\tNeatly formatted name: {formatted_name}.")
    

