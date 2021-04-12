# Сбой теста.
# Изменим функцию, get_formatted_name(), чтобы она работала с отчеством
# Первоначальная функция имеет Ex. 1
# В этом случае файл test_name_function.py выдаст другой результат.

def get_formatted_name(first, middle, last):
    """Строит отформатированное полное имя."""
    full_name = f"{first} {middle} {last}"
    return full_name.title()
