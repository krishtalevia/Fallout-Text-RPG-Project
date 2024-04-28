import upper
import gui

def main():
    gui.print_start()
    char_name = upper.new_or_load_game()

    if upper.is_profile_empty(char_name) == True:
        # Создание персонажа с экспозицией
        pass