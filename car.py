# Изменение значений атрибутов.
# Применяется три способа:
# 2) ИЗМЕНЕНИЕ ЗНАЧЕНИЯ АТРИБУТА ПРИРАЩЕНИЕМ.

# Новый метод increment_odometer() в (1) получает расстояние 
# в милях и прибавляет его к self.odometer_reading. В (2) создается
# экземпляр my_user_car. Мы инициализируем показания его одометра
# значением 23500 (3). В (4) метод increment_odometer(), которому 
# предоставляется значение 100, чтобы увеличить показания одометра
# на 100 миль, пройденные с момента покупки. 

# Данный пример предполагает, что приобретена подержанная машина, 
# на которй с момента покупки мы проехали 100 миль.


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

my_user_car = Car('subaru', 'outback', 2015) #2
print(my_user_car.get_descriptivq_name())

my_user_car.update_odometer(23_500) #3
my_user_car.read_odometer()

my_user_car.increment_odometer(100) #4
my_user_car.read_odometer()

