import os
import gui

def check_char_directory() -> None:
    if not os.path.isdir('characters'):
        os.makedirs('characters')
        print('test Папки содержащей профили не существовало, папка создана.')

def character_deifne(char_status, char_name) -> None:
    if char_status == 'new' and os.path.exists(rf'characters/{char_name}'):
        answer = gui.char_exists()

        if answer == 'rewrite':
            pass