# Передача произвольного набора аргументов.
# Звездочка с именем параметра (*toppings) приказывает проге
# создать пустой кортеж с именем toppings и упаковать в него 
# все полученные значения.

def make_pizza(*toppings):
    """Выводит список заказанных топпиноговю"""
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
