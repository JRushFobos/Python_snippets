import json
import os
os.chdir('f:\\LocalRepository\\Python_snippets\\Python_chapter_8_Files\\username')

filename = 'username.json'
with open (filename,'r') as f:
    username = json.load(f)
    print(f'Wellcome back {username}')