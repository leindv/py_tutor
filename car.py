# Работа с классами и экземплярами.
# Одной из задач, которая встречается разработчику, это 
# изменение атрибутов, связанных с конкретным экземпляром.
# Атрибуты экземпляра можно изменять напрямую или же 
# написать методы, изменяющие атрибуты по особым правилам.
# 
class Car():
    """Простая модель автомобиля."""
    def __init__(self, make, model, year):
        """Инициализирует АТРИБУТЫ описания автомобиля."""
        self.make = make
        self.model = model
        self.year = year

    def get_descriptivq_name(self):
        """Возвращает аккуратно отформатированное описание."""
        long_name = f"{self.make} {self.model} {self.year}"
        return long_name.title()

my_new_car = Car('audi','a6', 2020)
print(my_new_car.get_descriptivq_name())
