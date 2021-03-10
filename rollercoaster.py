# Функуия input() выводит строковое значение, для 
# его преобразования в числовое значение используется 
# функция int()(1). 
#
height = input("How tall are you, in inches? ")
height = int(height) #1
if height >= 48:
    print("\nYou are tall enough to ride!")
else:
    print("\nYou will be able to ride when you are a little older.")
