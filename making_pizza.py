# Для импортирования функции , сначала необходимо создать 
# модуль, который представляет собой файл
# с расширением .py, содержащий код, который мы 
# хоти импортировать в свою прогу.
# Файл pizza.py
#  def make_pizza(size, *toppings):
#     """Выводит описание пиццы."""
#      print(f"\nMaking a {size}-inch pizza with the following toppings:")
#      for topping in toppings:
#        print(f"- {topping}")
# В процессе обработки вновь созданного файла строка import pizza
# говорит проге открыть файл pizza.py и скопировать все функции из него в 
# файл программы.
# Чтобы вызвать функцию из импортированного модуля надо указать имя модуля 
# (pizza), точку и имя функции (make_pizza()) (1).

# Для имортирования конкретной функции из модуля применяется конструкция:
# FROM ИМЯ_МОДУЛЯ IMPORT ИМЯ_ФУНКЦИИ_0, ИМЯ ФУНКЦИИ_1, ИМЯ ФУНКЦИИ_2



from pizza import make_pizza
make_pizza(16, 'pepperoni') 
make_pizza(12, 'mushrooms','green peppers', 'extra cheese')
