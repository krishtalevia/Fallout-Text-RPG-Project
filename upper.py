import gui
import lower

def new_or_load_game():
    lower.check_char_directory()
    while True:
        char_status = gui.ask_new_or_load()
        char_name = gui.character_name()
        if lower.character_deifne(char_status, char_name) == False:
            continue
        else:
            break

