import unittest
from name_function import get_formatted_name
import os

os.chdir('f:\\LocalRepository\\Python_snippets\\Python_chapter_9_Testing\\test_formatted_name')

class NamesTestCase(unittest.TestCase):
    '''Тесты для 'name_function.py' '''
    def test_ferst_last_name(self):
        '''Имена вида "Janis Polin" работают правильно? '''
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

if __name__ == '__main__':
    unittest.main()
