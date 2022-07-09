import os
print(os.getcwd())

os.chdir('f:\\LocalRepository\\Python_snippets\\Python_chapter_8_Files\\Python_work')

print(os.getcwd())

file_path = 'pi_1_million.txt'
with open (file_path) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print(pi_string[:52])
print(len(pi_string))

