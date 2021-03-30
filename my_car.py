# Импортирование одного класса.

# Команда import в (1) приказывает проге 
# открыть модуль car и импортировать 
# класс Car().


from car import Car #1

my_new_car = Car('audi', 'a8', 2019)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()
