# Тест проверяет, что один ответ на опрос сщхраняется правильно.

# После того как метод будет сохранен, метод assertIn() проверят, 
# что он действительно находиться в списке ответов.

# Прга начинается с импорта модуля unittest и тестируемого класса 
# AnonymousSurvey. Тестовый сценарий TestAnonymousSurvey наследует
# unittest.TestCase(1). Первый тестовый метод проверяет, что сохраненный 
# ответ действительно попадает в список ответов опроса. Этому методу 
# присваивается имя test_store_single()(2).
# Чтобы протестировать поведение класса, надо создать экземпляр класса.
# В (3) создается экземпляр с именем my_survey для вопроса 
#  "What language did you first learn to speak?". 
#  Один ответ (English) сохраняется с использованием метода 
#  store_response(). Затем прога убеждается в том, что ответ был
#  сохранен правильно; для этого она проверяет, что значение English 
#  присутсвует в списке my_survey.response (4). 


import unittest
from survey import AnonymousSurvey
class TestAnonymousSurvey(unittest.TestCase): #1
    """Тесты для класса AnonymousSurvey."""

    def test_store_single_response(self): #2
        """Проверяет , что один ответ сохранен правильно."""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question) #3
        my_survey.store_response('English')
        self.assertIn('English', my_survey.responses) #4

if __name__ == '__mine__':
    unittest.main()


