# НАСЛЕДОВАНИЕ.

# В (1) строится экземпляр Car. При создании класса-потомка 
# класс-родитель должен быть частью текущего файла, а его 
# определение должно предшествовать определению класса-потомка 
# в файле.
# В (2) определяется класс-потомок ElectricalCar. В определении 
# потомка имя класса-родителя заключается в круглые скобки. 
# Метод __init__() в (3) получает информацию, необходимую 
# для создания экземпляра Car.
# Функция super() d (4) - это спец ф-ция, которая позваляет 
# вызвать метод родительского класса. Эта строка приказывает 
# проге вызвать метод __init__() класса Car, в результате чего
# экземпляр ElectricalCar получит доступ ко всем атрибутам 
# класса-родителя. 
# Имя super происходит от терминалогии: кльасс-родитель наз. 
# СУПЕРКЛАСС, а класс-потомок - ПОДКЛАСС.
# В (5) создаем экземпляр класса ElectricalCar и сохраняем его 
# в my_teala.
# Это строка вызывает метод __init__(), определенный в ElectricalCar,
# который в свою очередь приказывает проге вызвать метод __init__(), 
# определенный в классе-родителе Car.


class Car(): #1
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

class ElectricalCar(Car): #2
    """
    Представляет аспекты машины, специфичные 
    для электромобилей.
    """
    def __init__(self, make, model, year): #3
        """ инициализирует атрибуты класса-родителя."""
        super().__init__(make, model, year) #4

my_teala = ElectricalCar('tesla', 'model s', 2019) #5
print(my_teala.get_descriptivq_name())
