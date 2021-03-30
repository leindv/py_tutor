# Аналогичен файлк my_car.py

from car import ElectricalCar

my_tesla = ElectricalCar('tesla', 'model s', 2019)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
