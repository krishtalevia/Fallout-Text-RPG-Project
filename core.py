import upper
import gui

def main():
    # Приветственное окно и меню "новая/загрузить/выйти"
    while True:
        gui.print_start()
        char_name = upper.main_menu()

        if char_name == 'exit':
            return

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
                status = upper.death(char_name)

            if status == 'to_main_menu':
                break

            elif status == 'again':
                continue

            elif status == 'exit':
                print('Завершение программы.')
                return


