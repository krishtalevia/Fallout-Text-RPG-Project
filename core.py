import upper
import gui

def main():
    # Приветственное окно и меню "новая/загрузить/выйти"
    while True:
        gui.print_start()
        char_name = upper.main_menu()

        if upper.is_profile_empty(char_name) == True:
            upper.character_creation(char_name)

        # Выбор пути
        upper.prelude_to_the_journey(char_name)
        road = upper.choosing_a_road()
        while True:
            # Прохождение комнат
            status = upper.passing_the_rooms(road, char_name)

            if status == 'dead':
                print('Вы погибли')
                upper.death(char_name)

            elif status == 'exit':
                print('Завершение программы.')
                break


