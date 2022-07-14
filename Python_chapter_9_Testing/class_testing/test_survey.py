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

if __name__ == '__main__':
    unittest.main()
