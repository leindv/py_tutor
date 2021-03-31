# Импортирование всего модуля.

# В точке (1) импортируется весь модуль, после 
# чего прога обращается к нужным классам с 
# использованием синтаксиса:
# ИМЯ_МОДУЛЯ.ИМЯ_КЛАССА() - точки 2 и 3.

import car #1

my_beetle = car.Car('volkswagen', 'beetle', 2019) #2
print(my_beetle.get_descriptive_name())

my_tesla = car.ElectricalCar('tesla', 'roadster', 2019) #3
print(my_tesla.get_descriptive_name())

