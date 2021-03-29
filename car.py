# Изменение значений атрибутов.
# Применяется три способа:
# 2) ИЗМЕНЕНИЕ ЗНАЧЕНИЯ АТРИБУТА ПРИ ПОМОЩИ МЕТОДА.

# Класс Car() не изменился, в нем только добавился метод
# update_odometer(), который получает пробег в миляхи и 
# сохраняет его в self.odometer_reading. В точке (2) мы 
# вызываем метод update_odometer() и передаеи ему значение 
# 23 в аргументе (соответсвующиему параметру mileage в определении
# метода). Метод устанавливает на одометре значение 23, а метод 
# read_odometer() выводит текущее значение.

class Car():
    """Простая модель автомобиля."""
    def __init__(self, make, model, year):
        """Инициализирует АТРИБУТЫ описания автомобиля."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptivq_name(self):
        """Возвращает аккуратно отформатированное описание."""
        long_name = f"{self.make} {self.model} {self.year}"
        return long_name.title()

    def read_odometer(self): 
        """Выводит пробег машины в милях."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage): #1
        """Устанавливает заданное значение на одометре."""
        self.odometer_reading = mileage

my_new_car = Car('audi','a6', 2020)
print(my_new_car.get_descriptivq_name())

my_new_car.update_odometer(23) #2 
my_new_car.read_odometer()
