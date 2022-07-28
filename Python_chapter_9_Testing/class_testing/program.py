import os

os.chdir('f:\\LocalRepository\\Eric_Matiz\\HW\\Chapter_11\\11.3')

def get_user_name():
    while True:
        fname = input('Inter your first name')
        if fname == 'q':
            break
        lname = input('Inter your last name')
        if fname == 'q':
            break
        current_salary = input('Inter your current_salary')
        if fname == 'q':
            break