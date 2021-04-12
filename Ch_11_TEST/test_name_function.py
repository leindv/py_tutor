# Добавление новых тестов.

# Чтобы протестировать функцию мы вызываем get_formatted_name()
# с тремя компонентами (1), после чего используем assertEqual()
# для проверки того, что возвращаемое полное имя совпадает с 
# ожидаемым.

import unittest
from name_function import get_formatted_name 

class NameTestCase(unittest.TestCase): 
    """Тесты для name_function.py."""

    def test_first_last_name(self):
        """Имена вида 'Dim Lein' работают правильно."""
        formatted_name = get_formatted_name('dim', 'lein') 
        self.assertEqual(formatted_name, 'Dim Lein') 

    def test_first_last_middle_name(self): #2
        """Работаю ли такие имена как 'Wolfgang Amadeus Mozart'?"""
        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

if __name__ == '__main__': 
    unittest.main()