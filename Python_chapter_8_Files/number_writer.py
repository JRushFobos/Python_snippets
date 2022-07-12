import os
os.chdir('f:\\LocalRepository\\Python_snippets\\Python_chapter_8_Files')

import json

numbers = [2,3,5,11,13]

filename = 'number.json'
with open (filename, 'w') as f:
    json.dump(numbers,f)
