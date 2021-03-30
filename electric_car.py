# НАСЛЕДОВАНИЕ.

# Экземпляры как атрибуты
# 
# При моделировании явлений реального мира в программах классы 
# нередко дополняются все большим количеством подробностей.
# Списки атрибутов и методов растут, и через какое-то время 
# файлы становятся длинными и громозкими.
# В такой ситуации часть одного класса нередко можно записать 
# в виде отдельного класса.
# Большой код разбивается на меньшие классы, которые работают 
# во взаимодействии друг с другом.
# Напимер, при дальнейшей дороботки класса ElectricCar() может 
# оказаться, что в нем появляется слишком много атрибутов и методов, 
# которые  относятся к аккумуляторной батареи. В таком случае можно 
# остановиться и переименовать все эти атрибуты и методы в отдельный 
# класс  с именем Battery(). 
# Затем экземпляр Battery() становится атрибутом класса ElectricCar().

# В (1) определяется новый класс Battery(), который не неаследует ни один 
# из других классов. 
# Метод __init__() в (2) получает один параметр battery_size, кроме self.
# Если значение не представлено, это необязательный параметр задает 
# battery_size значение 75.
# Метод describe_battery() также перемещен в этот класс (3).
# Затем в класс ElectricalCar() добавляется атрибут с именем 
# self.battery (4).
# Эта строка приказывает проге создать новый экземпляр Battery 
# (со значением battery_size по умолчанию равным 75, потому что 
# значение не задано) и сохранить его в атрибуте self.battery. 
# Это будет происходить при каждом вызове __init__(); теперь любой 
# экземпляр ElectricalCar() будет автоматически создаваемый экземпляр 
# Battery().
# В (5) строка приказывает проге обратиться к экземпляру my_tesla, 
# найти его атрибут battery и вызвать метод describe_battery(), 
# связанный с экземпляром Battery из атрибута.



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

class Battery(): #1
    """Простая модель аккумулятора электромобиля."""

    def __init__(self, battery_size = 75): #2
        """Инициализирует атрибуты аккумулятора."""
        self.battery_size = battery_size

    def describe_battery(self): #3
        """Выводит информацию о мощности акуумулятора."""
        print(f"This car has a {self.battery_size} - kWh battery.")




    
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
my_tesla.battery.describe_battery() #5
