# Сбой теста.
# Изменим функцию, get_formatted_name(), чтобы она работала с отчеством
# Первоначальная функция имеет Ex. 1
# В этом случае файл test_name_function.py выдаст другой результат.

def get_formatted_name(first, middle, last):
    """Строит отформатированное полное имя."""
    full_name = f"{first} {middle} {last}"
    return full_name.title()

# Результат тестирования в файле test_name_function.py
# 1 E
# ======================================================================
# 2 ERROR: test_first_last_name (__main__.NamesTestCase)
# ----------------------------------------------------------------------
# 3 Traceback (most recent call last):
# File "test_name_function.py", line 8, in test_first_last_name
# formatted_name = get_formatted_name('janis', 'joplin')
# TypeError: get_formatted_name() missing 1 required positional argument:
# 'last'
# ----------------------------------------------------------------------
# 4 Ran 1 test in 0.000s
# 5 FAILED (errors=1)
