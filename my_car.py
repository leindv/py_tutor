# Импортирование нескольких классов из модуля.

# Импортирование нескольктх классов из модуля(1), 
# имена классов разделяются запятыми.
# После импорта создается столько экземпляров класса, 
# сколько потребуется (2) и (3).

from car import Car,ElectricalCar #1

my_beetle = Car('volkswagen', 'beetle', 2019) #2
print(my_beetle.get_descriptive_name())

my_tesla = ElectricalCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())


my_new_car = Car('audi', 'a8', 2019)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()
