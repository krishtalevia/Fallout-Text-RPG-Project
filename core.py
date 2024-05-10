import upper
import gui

def main():
    # Приветственное окно и меню "новая/загрузить/выйти"
    while True:
        gui.print_start()
        char_name, char_status = upper.main_menu()

        if char_status == 'exit':
            return

        if not upper.is_profile_empty(char_name):
            upper.character_creation(char_name)

        status = 'prelude'

        while status == 'prelude':
            # Выбор пути
            upper.prelude_to_the_journey(char_name, char_status)
            road = upper.choosing_a_road(char_status)

            status = 'passing locations'

            while status == 'passing locations':
                # Прохождение комнат
                char_status = upper.passing_the_rooms(road, char_name)

                if char_status == 'dead':
                    print('Вы погибли')
                    char_status = upper.death(char_name)

                if char_status == 'to_main_menu':
                    break

                elif char_status == 'again':
                    status = 'passing locations'
                    continue

                elif char_status == 'exit':
                    print('Завершение программы.')
                    return


