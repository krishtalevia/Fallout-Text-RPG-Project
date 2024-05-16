import upper
import gui

def main():

    while True:
        # Меню "новая/загрузить/выйти"
        char_name, load_status = upper.main_menu()

        if load_status == 'exit':
            return

        # Создание персонажа
        if upper.is_profile_empty(char_name):
            upper.character_creation(char_name)

        status = 'prelude'

        while status == 'prelude':

            if load_status != 'load':
                # Выбор пути
                upper.prelude_to_the_game(char_name)
                upper.choosing_a_road(char_name)

            status = 'passing locations'

            while status == 'passing locations':
                # Прохождение локаций
                char_status = upper.passing_the_rooms(char_name)

                if char_status == 'dead':
                    print('Вы погибли')
                    char_status = upper.death(char_name)

                if char_status == 'to_main_menu':
                    break

                elif char_status == 'again':
                    status = 'passing locations'
                    continue

                elif char_status == 'exit':
                    return

                elif char_status == 'end':
                    status = 'prelude'
                    load_status = 'playing'
                    break


