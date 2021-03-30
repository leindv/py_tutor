# ИМПОРТИРОВАНИЕ КЛАССОВ.

# Импортирование одного класса.

# В (1) включается строка документации уровня модуля с 
# кратким описанием содержания модуля.
# Далее будем создавать файл с иенем my_car.py, который 
# импортирует класс Car() и создает экземпляр этого 
# класса.


"""Класс для представления автомобиля.""" #1
class Car():
    """Простая модель автомобиля."""
    def __init__(self, make, model, year):
        """Инициализирует АТРИБУТЫ описания автомобиля."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Возвращает аккуратно отформатированное описание."""
        long_name = f"{self.make} {self.model} {self.year}"
        return long_name.title()

    def read_odometer(self): 
        """Выводит пробег машины в милях."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage): 
        """
        Устанавливает заданное значение на одометре.
        При попытке обратной прокрутки изменения отклоняются.
        """
        if mileage >= self.odometer_reading: 
            self.odometer_reading = mileage
        else:
            print("You can not roll back an odometer!")

    def increment_odometer(self, miles): #1
        """Увеличение показания одометра с заданным приращением.""" 
        self.odometer_reading += miles


