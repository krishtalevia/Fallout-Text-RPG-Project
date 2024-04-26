import gui
import lower

def new_or_load_game():
    lower.check_char_directory()
    while True:
        char_status = gui.ask_new_or_load()
        char_name = gui.character_name()
        if lower.character_deifne(char_status, char_name) == False:
            print('\033[5;36m[test]\033[0m Был выбран вариант вернуться т.к. такой перс уже есть')
            continue
        else:
            print(f'\033[5;36m[test]\033[0m Персонаж {char_name} создан или перезаписан')
            break


