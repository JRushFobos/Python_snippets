import os
from name_function import get_formatted_name

os.chdir('f:\\LocalRepository\\Python_snippets\\Python_chapter_9_Testing\\test_formatted_name_with_3_param')

print ("Enter 'q'  at any time to quit.")

while True:
    first = input ('\nPlease give me a first name:')
    if  first  == 'q':
        break
    last = input ('\nPlease give me a first name:')
    if last == 'q':
        break

formatted_name  = get_formatted_name(first,last)
print(f'\nNeatly formatted name: {formatted_name}.')