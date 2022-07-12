import json
import os
os.chdir('f:\\LocalRepository\\Python_snippets\\Python_chapter_8_Files\\username')

username = input ('What is your name?')
filename = 'usenname.json'

with open (filename,'w') as f:
    json.dump(username,f)
    print(f"We'll remember you when you come back,{username}!")