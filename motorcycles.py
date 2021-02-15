# Пример с использованием f-строки и метода pop()
# для удаления элемента в произвольной позиции.
# С начала первый элемент извлекается из точки 1.
# Затем в точке 2 выводится сообщение об этом мотоцикле.
#
motorcycles = ['honda', 'yamaha', 'suzuki'] 
first_owned = motorcycles.pop(0) #1
print(f"The first motorcycle I owned was a {first_owned.title()}.") #2
