# Передача произвольного набора аргументов.
# Звездочка с именем параметра (*toppings) приказывает проге
# создать пустой кортеж с именем toppings и упаковать в него 
# все полученные значения.
# Здесь команду print из предыдущего коммита заменяем циклом,
# котроый перебирает список топпингов и выводит описание заказанной 
# пиццы.

def make_pizza(*toppings):
    """Выводит список заказанных топпиноговю"""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
