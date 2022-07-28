import unittest
from survey import AnonymousSurvey
import os

os.chdir('f:\\LocalRepository\\Python_snippets\\Python_chapter_9_Testing\\class_testing')

class TestAnonmyousSurvey(unittest.TestCase):
    '''Тесты для класса AnonymousSurvey'''

    def test_story_single_response(self):
        '''Проверяет, что один ответ сохранен правильно.'''

        question = 'What language did you first learn to speak?'
        my_survey = AnonymousSurvey(question)
        my_survey.story_response('English')
        self.assertIn('English', my_survey.responses)

    def test_story_three_responses(self):
        '''Проверяет что 3 ответа сохранились правильно'''
        question = 'What language did you first learn to speak?'
        my_survey = AnonymousSurvey(question)
        responses = ['English','Spanish','Mandarin']
        for response in responses:
            my_survey.story_response(response)

        for response in responses:
            self.assertIn(response, my_survey.responses)

if __name__ == '__main__':
    unittest.main()
