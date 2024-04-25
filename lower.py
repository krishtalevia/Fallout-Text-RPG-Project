import os

def check_char_directory():
    if not os.path.isdir('characters'):
        os.makedirs('characters')
        print('test Папки содержащей профили не существовало, папка создана.')

def new_profile():
    pass
