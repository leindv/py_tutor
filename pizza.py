# Позиционные аргументы с призвольным набором аргументов.
# Если надо, чтобы функция могла вызываться с различным
# количеством аргументов, параметр для получения произвольного 
# количества аргументов долженстоятьна ПОСЛЕДНЕМ месте в определении 
# функции.

def make_pizza(size, *toppings):
    """Выводит список заказанных топпиноговю"""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
