import upper
import gui

def main():
    # Приветственное окно и меню "новая/загрузить/выйти"
    gui.print_start()
    char_name = upper.new_or_load_game()

    if upper.is_profile_empty(char_name) == True:
        upper.character_creation(char_name)

    while True:
        # Выбор пути
        upper.prelude_to_the_journey(char_name)
        road = upper.choosing_a_road()
        while True:
            # Прохождение комнат
            status = upper.passing_the_rooms(road, char_name)

            if status == 'dead':
                continue
            elif status == 'load':
                pass


