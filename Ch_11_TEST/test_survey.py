# Метод setUp().

# Данный метод решает две задачи: он создает экземпляр опроса(1) и
# список ответов(2). Каждый из этих атрибутов снабжается префиксом self,
# поэтому от может использоваться где угодно в классе.

import unittest
from survey import AnonymousSurvey
class TestAnonymousSurvey(unittest.TestCase): 
    """Тесты для класса AnonymousSurvey."""

    def setUp(self):
        """Создание опроса и набора ответов для всех тестовых методов."""
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question) #1
        self.responses = ['English', 'Spanish', 'Mandarin'] #2

    def test_store_single_response(self): 
        """Проверяет , что один ответ сохранен правильно."""
        self.my_survey.store_response(self, responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)
      
    def test_store_three_responses(self):
        """Проверяет, что три ответа сохраняются праильно."""
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

if __name__ == '__mine__':
    unittest.main()


