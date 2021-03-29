# НАСЛЕДОВАНИЕ.

# Определение атрибутов и методов класса-потомка.

# В точке (1) добавляется новый атрибут self.battery_size, 
# которому присваивается значение - 75.
# Этот атрибут будет присутсовать во всех экземплярах, 
# созданных на основе клавсса ElectricalCar()
# (но не во всяком экзепляре Car()).
# Также добавляется метод describe_battery(), 
# который выводит инфо об аккумуляторк в точке (2).
# При вызове этого метода выводится описание, 
# которое явно относится к электромобилям.



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

    def increment_odometer(self, miles): 
        """Увеличение показания одометра с заданным приращением.""" 
        self.odometer_reading += miles

    
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
        self.battery_size = 75 #1

    def describe_battery(self): #2
        """Выводит информацию о мощности аккумулятора."""
        print(f"This car has a {self.battery_size} - kWh battery.")

    

my_tesla = ElectricalCar('tesla', 'model s', 2019) 
print(my_tesla.get_descriptivq_name())

my_tesla.describe_battery()
