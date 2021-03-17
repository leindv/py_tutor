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

# То есть здесь используется синтаксис IMPORT для ивзлечения всего модуля 
# ИМЯ_МОДУЛЯ.PY в виде ИМЯ_МОДУЛЯ.ИМЯ_ФУНКЦИИ () .


import pizza
pizza.make_pizza(16, 'pepperoni') #1
pizza.make_pizza(12, 'mushrooms','green peppers', 'extra cheese')
