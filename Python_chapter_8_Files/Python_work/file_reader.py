import os
print(os.getcwd())

os.chdir('f:\\LocalRepository\\Python_snippets\\Python_chapter_8_Files\\Python_work')

print(os.getcwd())

file_path = 'pi_digits.txt'
with open (file_path) as file_object:
    content = file_object.read()
print(content)