import os
os.chdir('f:\\LocalRepository\\Python_snippets\\Python_chapter_8_Files\\number')

filename = 'number.json'
with open (filename, 'w') as f:
    numbers = json.load(f)
