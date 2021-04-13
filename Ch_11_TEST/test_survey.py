# Тест проверяет, что ТРИ ответа сохранились правильно.

# Здесь определяем объект опроса по аналогии с тем, как делалось 
# это в предыдущем коммите. Затем определяем список, содержащий три 
# разных ответа (1) и для каждого из этих ответов вызывается метод 
# store_response(). После того как ответы будут сохранены, следующий 
# цикл проверяет, что каждый ответ присутсвует в my_survey.responses(2).

import unittest
from survey import AnonymousSurvey
class TestAnonymousSurvey(unittest.TestCase): 
    """Тесты для класса AnonymousSurvey."""

    def test_store_single_response(self): 
        """Проверяет , что один ответ сохранен правильно."""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question) 
        my_survey.store_response('English')
        self.assertIn('English', my_survey.responses)

    def test_store_three_responses(self):
        """Проверяет, что три ответа сохраняются праильно."""
        my_survey = AnonymousSurvey(question)
        responses = ['English', 'Spanish', 'Mandarin'] #1
        for response in responses:
            my_survey.store_response(response)

        for response in responses: #2
            self.assertIn(response, my_survey.responses)

if __name__ == '__mine__':
    unittest.main()


