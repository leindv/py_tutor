# Кортежи (TUPLES) - это набор элемеентов, 
# значение которых не изменяется.
# Но мы можем присвоить НОВОЕ значение переменной, 
# в которой храниться кортеж.
# В точке 1 определяем исходный кортеж, в 2 
# сохраняется новый кортеж, после чего выводятся 
# новые значения (3)
#
dimensions = (200, 50) #1
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)
dimensions = (400, 100) #2
print("\nModified dimensions:") #3
for dimension in dimensions:
    print(dimension)
