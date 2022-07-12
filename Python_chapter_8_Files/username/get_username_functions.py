import json
import os
os.chdir('f:\\LocalRepository\\Python_snippets\\Python_chapter_8_Files\\username')



def get_stored_username():
    filename = 'usenname.json'
    try:
        with open (filename,'r') as f:
            username = json.load(f)
    except FileNotFoundError:
        None
    else:
        return username
    
def greet_user():
    username = get-stored_username()
    if username:
        print(f'Wellcome back {username}')
    else:
        username = input('What is your name?')
        filename = 'usenname.json'
        with open (filename,'w') as f:
            json.dump(username,f)
            print(f"We'll remember you when you come back,{username}!")

greet_user()
    