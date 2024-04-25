import gui
import lower

def new_or_load_game():
    char_status = gui.ask_new_or_load()
    char_name = gui.character_name()
    lower.check_char_directory()

    if char_status == 'new':

        pass
    else:
        pass
