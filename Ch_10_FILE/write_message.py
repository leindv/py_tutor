# Запись в файл.

# Многострочная зпись.
# Если символы ("\n") не были включены в команды 
# write(), то полученные строки в txt-файле получились 
# бы "склееными."



filename = 'programming.txt'

with open(filename, 'w') as file_object: 
    file_object.write('I love programming.\n')
    file_object.write('I love creating new games.\n')
