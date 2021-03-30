# НАСЛЕДОВАНИЕ.

# Экземпляры как атрибуты
# 
# В дополнении к предудущему коммиту:

# Теперь аккумулятор можно моделировать с любой степенью 
# детализации без  загромаждения класса ElectricalCar().
# Добавим в Battery() ущу один метод, который выводит запас 
# хода на основании мощности аккумулятора.

# Новый метод get_range() в (1) проводит простой анализ.
# Если мощность равна 75, то get_range() устанавливает 
# запас хода 260 миль,
# а при мощности 100 кВт/ч запас хода равен 315 милям.
# Затем прога выводит это значение. Когда мы хотим 
# использовать этот метод, его придется вызвать через 
# атрибут battery в точке (2).

class Car(): 
    """Простая модель автомобиля."""
    def __init__(self, make, model, year):
        """Инициализирует АТРИБУТЫ описания автомобиля."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

        # Емкость бензобака и уровень бензина в нем.
        self.fuel_capacity = 15
        self.fuel_level = 0
        
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

    def increment_odometer(self, miles): 
        """Увеличение показания одометра с заданным приращением.""" 
        self.odometer_reading += miles

    def fill_gas_tank(self): 
        """Заполнение бензобака бензином до полного."""
        self.fuel_level = self.fuel_capacity
        print("Fuel tank is full.")

class Battery(): 
    """Простая модель аккумулятора электромобиля."""

    def __init__(self, battery_size = 75): 
        """Инициализирует атрибуты аккумулятора."""
        self.battery_size = battery_size

    def describe_battery(self): 
        """Выводит информацию о мощности акуумулятора."""
        print(f"This car has a {self.battery_size} - kWh battery.")

    def get_range(self): #1
        """Выводит приблизительный запас хода для аккумулятора."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about {range} miles on full charge.")
    
class ElectricalCar(Car): 
    """
    Представляет аспекты машины, специфичные 
    для электромобилей.
    """
    def __init__(self, make, model, year): 
        """ 
        Инициализирует атрибуты класса-родителя.
        Затем инициализируем атрибуты, специфичные для электромобиля.
        """
        super().__init__(make, model, year)
        self.battery = Battery() #4

    def describe_battery(self): 
        """Выводит информацию о мощности аккумулятора."""
        print(f"This car has a {self.battery_size} - kWh battery.")

    def fill_gas_tank(self): 
        """У электромобиля нет бензобака."""
        print("This car doesn`t need a gas tank!!!")
 
my_tesla = ElectricalCar('tesla', 'model s', 2019) 
print(my_tesla.get_descriptivq_name())
my_tesla.battery.describe_battery() 
my_tesla.battery.get_range() #2
