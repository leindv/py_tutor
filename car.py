# Изменение значений атрибутов.
# Применяется три способа:
# 1) ПРЯМОЕ ИЗМЕНЕНИЕ ЗНАЧЕНИЯ АТРИБУТА.

# Чтобы изменить значение атрибута проще всего 
# обратиться к нему ПРЯМО через экземпляр.
# В точке (1) точечная нотация используется для 
# обращения к атрибуту odometer_reading экземпляра 
# и прямо присваивает его значение. Эта строка 
# приказывает проге взять экземпляр my_new_car, 
# найти связанный с ним атрибут odometer_reading и 
# задать значение атрибута равным 23.

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

    def read_odometer(self): #2
        """Выводит пробег машины в милях."""
        print(f"This car has {self.odometer_reading} miles on it.")

my_new_car = Car('audi','a6', 2020)
print(my_new_car.get_descriptivq_name())

my_new_car.odometer_reading = 23 #1
my_new_car.read_odometer()
