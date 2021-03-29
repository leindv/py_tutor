# Изменение значений атрибутов.
# Применяется три способа:
# 2) ИЗМЕНЕНИЕ ЗНАЧЕНИЯ АТРИБУТА ПРИ ПОМОЩИ МЕТОДА.

# Метод update_odometer() можно расширить так, что при 
# каждом изменении показаний одометравыполнялась некоторая 
# дополнительная работа. Добавим проверку, которая гарантирует , 
# что никто не будет сбрасывать показания одометра.
# Теперь update_odometer() проверяет новое значение перед измерением 
# атрибута. Если новое значение mileage больше или равно текущему 
# значениию, self.odometer_reading, показания одометра можно обновить 
# новым значением (1). Если же новое значение меньше текущего, получаем 
# предупреждение (2).


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
        if mileage >= self.odometer_reading: #1
            self.odometer_reading = mileage
        else:
            print("You can not roll back an odometer!") #2

my_new_car = Car('audi','a6', 2020)
print(my_new_car.get_descriptivq_name())

my_new_car.update_odometer(23) 
my_new_car.read_odometer()
