class AnonymousSurvey():
    '''Сбор анонимных ответов на опросы.'''

    def __init__(self, question):
        '''Сохранят вопрос и готовится к сохранению ответов'''
        self.question = question
        self.responses = []

    def show_question(self):
        '''Выводит вопрос'''
        print(self.question)

    def story_response(self, new_response):
        '''Сохраняет один ответ на опрос'''
        self.responses.append(new_response)
    
    def show_results(self):
        print('Survey results:')
        for response in self.responses:
            print(f'-{response}')