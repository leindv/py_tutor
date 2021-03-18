# Назначение атрибуту значения по умолчанию.
# Добавили атрибут (1) , исходное значение которого
# всегда равно нулю.
# Когда прога вызывает метод __init__ для СОЗДАНИЯ НОВОГО
# экземпляра, этот метод сохраняет "старые" атрибуты, затем 
# создает новый атрибут(1). Так же в класс добавляется 
# новый метод (2).

class Car():
    """Простая модель автомобиля."""
    def __init__(self, make, model, year):
        """Инициализирует АТРИБУТЫ описания автомобиля."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 #1

    def get_descriptivq_name(self):
        """Возвращает аккуратно отформатированное описание."""
        long_name = f"{self.make} {self.model} {self.year}"
        return long_name.title()

    def read_odometer(self): #2
        """Выводит пробег машины в милях."""
        print(f"This car has {self.odometer_reading} miles on it.")

my_new_car = Car('audi','a6', 2020)
print(my_new_car.get_descriptivq_name())
my_new_car.read_odometer()

