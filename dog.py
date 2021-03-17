# Класс Dog представляет собой собаку, которая имеет кличку и 
# возраст, она умеет садиться (sit) и перекатываться по команде
# (roll_over). Это два вида информации (кличка и возраст) и два 
# вида поведения включены в класс Dog, потому что они являются 
# ОБЩИМИ для большинства собак. КЛАСС сообщает проге, как создать 
# объект, представляющий собаку. После того как КЛАСС написан, 
# мы используем его для СОЗДАНИЯ ЭКЗЕМПЛЯРОВ, каждый из которых 
# будет представлять одну конкретную собаку.

# В КАЖДОМ ЭКЗЕМПЛЯРЕ, созданном на основе КЛАССА Dog, будет 
# храниться кличка (name), возраст (age); будут присутсвовать 
# МЕТОДЫ sit() и roll_over().

# В 1 определяется класс с именем Dog()(начинается с символа 
# верхнего регистра, круглые скобки пусты). В 2 приведена ДОКУМЕНТАЦИЯ 
# с кратким описанием класса.
# 3- это специальный метод, который автоматически выполняется при 
# создании каждого нового экземплярана базе класса Dog.
# Каждая из двух переменных (4) снабжена преффиксом self
# В (5) определены два метода.

class Dog(): #1
    """Простая модель собаки.""" #2

    def __init__(self, name, age): #3
        """Инициализирует атрибуты name и age"""
        self.name = name #4
        self.age = age

    def sit(self): #5
        """Собака садиться по команде."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Собака перекатывается по команде."""
        print(f"{self.name} rolled over!")
