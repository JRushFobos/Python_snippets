import unittest
from survey import AnonymousSurvey
import os

os.chdir('f:\\LocalRepository\\Python_snippets\\Python_chapter_9_Testing\\class_testing')

# Определение вопроса с созданием эксемпляра AnonymousSurvey
question = 'What language did you first learn to speak?'
my_survey = AnonymousSurvey(question)

# Вывод вопроса и сохранение ответов.
my_survey.show_question()
print("Enter 'q' at any time to quit. \n")
while True:
    response = input('Language: ')
    if response == 'q':
        break
    my_survey.story_response(response)

# Вывод результатов опроса.
print('\nThank ypu to everyone who parcipated in the survey!')
my_survey.show_results()
