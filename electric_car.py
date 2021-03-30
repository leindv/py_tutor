# НАСЛЕДОВАНИЕ.

# Переопределение методов класса-родителя.

# Любой метод родительского класса, который в моделируемой 
# ситуации делает не то, что нужно, можно переопределить.
# Для этого в классе-потомке определяется метод с тем же 
# имененм, что и у метода класса-родителя.
# Прога игнорит методродителяи обращает внимание только 
# на метод, определенный в потомке.
# Допустим, что в классе Car() имеются атрибуты по емкости 
# бензобака и уровню бензина в нем (1), и метод fill_gas_tank()(1-1). 
# Для электромобиля заправка бензином бессмысслена, поэтому этот 
# метод логично  ПЕРЕОПРЕДЕЛИТЬ, как это сделано в точке (2).
# Информация о переопределении метода представлена в точке (3).



class Car(): 
    """Простая модель автомобиля."""
    def __init__(self, make, model, year):
        """Инициализирует АТРИБУТЫ описания автомобиля."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

        # (1) Емкость бензобака и уровень бензина в нем.
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

    def fill_gas_tank(self): #1-1
        """Заполнение бензобака бензином до полного."""
        self.fuel_level = self.fuel_capacity
        print("Fuel tank is full.")


    
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
        self.battery_size = 75 

    def describe_battery(self): 
        """Выводит информацию о мощности аккумулятора."""
        print(f"This car has a {self.battery_size} - kWh battery.")

    def fill_gas_tank(self): #2
        """У электромобиля нет бензобака."""
        print("This car doesn`t need a gas tank!!!")

    

my_tesla = ElectricalCar('tesla', 'model s', 2019) 
print(my_tesla.get_descriptivq_name())

my_tesla.describe_battery()

my_tesla.fill_gas_tank() #3

