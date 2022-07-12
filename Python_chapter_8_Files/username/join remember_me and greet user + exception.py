import json
import os
os.chdir('f:\\LocalRepository\\Python_snippets\\Python_chapter_8_Files\\username')

filename = 'usenname.json'

try:
    with open (filename,'r') as f:
        username = json.load(f)
        
except FileNotFoundError:
    username = input ('What is your name?')
    with open (filename,'w') as f:
        json.dump(username,f)
        print(f"We'll remember you when you come back,{username}!")
else:
    print(f'Wellcome back {username}')