import unittest
from survey import AnonymousSurvey
import os

os.chdir('f:\\LocalRepository\\Python_snippets\\Python_chapter_9_Testing\\class_testing')

class TestAnonmyousSurvey(unittest.TestCase):
    '''Тесты для класса AnonymousSurvey'''
    
    def setUp(self):
        '''Создания опроса и набора ответов для всех тестовых методов'''
        question = 'What language did you first learn to speak?'
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English','Spanish','Mandarin']


    def test_story_single_response(self):
        '''Проверяет, что один ответ сохранен правильно.'''
        self.my_survey.story_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_story_three_responses(self):
        '''Проверяет что 3 ответа сохранились правильно'''

        for response in self.responses:
            self.my_survey.story_response(response)

        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

if __name__ == '__main__':
    unittest.main()
