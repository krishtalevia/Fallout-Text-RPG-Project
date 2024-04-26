import os
import gui

def check_char_directory() -> None:
    if not os.path.isdir('characters'):
        os.makedirs('characters')
        print('\033[5;36m[test]\033[0m Папки содержащей профили не существовало, папка создана.')

def character_deifne(char_status, char_name) -> None:
    if char_status == 'new' and os.path.exists(rf'characters/{char_name}.txt') == True:
        answer = gui.char_exists()

        if answer == 'rewrite':
            file = open(fr'characters/{char_name}.txt', 'w', encoding='utf-8')
            file.close()
            return True
        else:
            return False

    elif char_status == 'new' and os.path.exists(rf'characters/{char_name}.txt') == False:
        file = open(fr'characters/{char_name}.txt', 'w', encoding='utf-8')
        file.close()
        return True

    elif char_status == 'load':
        return True
