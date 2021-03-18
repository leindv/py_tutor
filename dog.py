# ВЫЗОВ МЕТОДОВ.
# После создания экземпляра на основе класса Dog 
# можно применить точечную нотацию для вызова любых методов,
# определенных в Dog (1) и (2).
# Чтобы вызвать метод указываем экземпляр (в данном случае 
# my_dog) и вызываемый метод, разделив их точкой.
# В ходе обработки my_dog.sit() прога ищет метод sit() в 
# классе Dog и выполняет его. 

class Dog(): 
    """Простая модель собаки.""" 

    def __init__(self, name, age): 
        """Инициализирует атрибуты name и age"""
        self.name = name 
        self.age = age

    def sit(self): 
        """Собака садиться по команде."""
        print(f"{self.name.title()} is now sitting.")

    def roll_over(self):
        """Собака перекатывается по команде."""
        print(f"{self.name.title()} rolled over!")
my_dog = Dog('willie', 6)
my_dog.sit() #1
my_dog.roll_over() #2 

print(f"Me dog`s name is {my_dog.name.title()}.") 
print(f"My dog`s is {my_dog.age} years old.") 
