import gui
import lower

def new_or_load_game():
    lower.check_char_directory()
    while True:
        char_status = gui.ask_new_or_load()
        char_name = gui.character_name()
        if lower.character_deifne(char_status, char_name) == False:
            print('\033[5;36m[test]\033[0m Возврат в главное меню т.к. такой персонаж уже есть,'
                  'либо его нет при попытке загрузиться')
            continue
        else:
            print(f'\033[5;36m[test]\033[0m Персонаж {char_name} создан/перезаписан/загружен')
            break

    return char_status


