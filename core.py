import upper
import gui

def main():
    gui.print_start()
    char_name = upper.new_or_load_game()

    if upper.is_profile_empty(char_name) == True:
        upper.character_creation(char_name)

    upper.prelude_to_the_journey(char_name)
    # выбор данжа