import os.path

import gui
import lower
import json

def main_menu() -> str:
    '''
    Выполняет роль главного меню, возвращает имя персонажа и выбор "начать новую игру"/"загрузить"/"выйти".
    :return: char_name: str (имя персонажа); load_status: str статус новой игры/загрузки/выхода
    '''

    lower.check_char_directory()

    while True:
        load_status = gui.input_main_menu_choice()

        if load_status == 'exit':
            return None, 'exit'

        char_name = gui.character_name()

        if lower.character_deifne(load_status, char_name) == False:
            continue
        else:
            break

    return char_name, load_status

def is_profile_empty(char_name: str) -> bool:
    '''
    Делает проверку на то, пустой ли файл с профилем в папке characters и возвращает True или False.
    :param char_name: выбранное ранее имя персонажа.
    :return: bool
    '''

    if os.path.getsize(rf'characters/{char_name}.json') == 0:
        return True
    else:
        return False

def character_creation(char_name: str) -> None:
    '''
    Создание персонажа, включающее в себя выбор параметров персонажа и экспорт этих параметров в json файл.
    :param char_name: str (имя персонажа)
    :return:
    '''

    # Выбор происхождения, роли и определение перка
    genesis = gui.input_roleplay_genesis()
    role = gui.input_roleplay_role(genesis)
    perk = lower.perk_define(genesis, role)

    # Экспозиция по выбранным параметрам и сохранение их в json файле
    gui.print_start_game_exposition(char_name, perk, role)
    lower.save_start_profile(char_name, genesis, role, perk)
    gui.continue_button()

def prelude_to_the_game(char_name: str) -> None:
    '''
    Меню перед началом игры, выбор просмотра статистики/продолжить/перейти к выбору подземелья (пути)
    :param char_name: str (имя персонажа)
    :return:
    '''

    while True:
        answer = gui.input_stats_or_go()

        if answer == 'stats':
            lower.print_import_stats(char_name)
            gui.continue_button()
            continue

        elif answer == 'go':
            return

def choosing_a_road(char_name: str) -> None:
    '''
    Выбор подземелья (в данном случае "пути") с сохранением его в профиль, в json файл.
    :param char_name: str (имя персонажа)
    :return:
    '''

    roads_list = lower.import_dir_list('paths')
    road = gui.input_choosing_road(roads_list)

    player_data = lower.import_data(f'characters/{char_name}.json')
    player_data['road'] = road
    lower.export_player_data(char_name, player_data)

def passing_the_rooms(char_name: str) -> str:
    '''
    Зацикленное прохождение комнат (в данном случае "локаций"), состоящих из событий "Враг", "Сокровище", "Ловушка",
    "Разветвление". Если встречается событие "Равзветвление": импортируется новая комната и начинается ее прохождение.
    Если встречается событие "Исход" - подземелье завершается и игрок возвращается к выбору подземелья.
    :param char_name: str (имя персонажа)
    :return:
    '''

    player_data = lower.import_data(f'characters/{char_name}.json')

    while True:

        # Определение подземелья и комнаты
        road = player_data['road']
        room_name = player_data['current_location']

        room = lower.convert_room_to_events_matrix(road, room_name)

        # Зацикленное прохождение комнаты
        for i in range(0, len(room), 1):

            # Меню перед каждым событием для возможности использовать предмет или выйти из игры
            player_data, menu_choice = lower.menu(player_data, char_name)

            if menu_choice == 'exit':
                return 'exit'
            elif player_data == 'dead':
                return 'dead'

            # В начале каждого события импортируется вся нужная информация о противнике/сокровище/ловушке.
            # После, игрок взаимодействует с событием и его данные сохраняются в рамках прохождения комнаты.

            if room[i][2] == 'Враг':
                enemy_data = lower.import_item_data(room[i][1],'enemies')
                gui.print_enemy_info(enemy_data, room[i][0])
                choice = gui.input_choice(room[i][3][0], room[i][3][1])

                if choice == '1':
                    player_data = lower.state_of_combat(char_name, player_data, enemy_data)

                elif choice == '2':
                    if lower.charisma_check(player_data,enemy_data) == False:
                        player_data = lower.state_of_combat(char_name, player_data, enemy_data)
                    else:
                        player_data = lower.player_get_loot_for_win(enemy_data, player_data, 'charisma')

            elif room[i][2] == 'Сокровище':
                item_data, item_category = lower.import_item_data(room[i][1], 'items')
                gui.print_treasure_info(room[i][0], item_data, item_category, room[i][1])
                choice = gui.input_choice(room[i][3][0], room[i][3][1])

                if choice == '1':
                    player_data = lower.take_item(room[i][1], player_data)

            elif room[i][2] == 'Задача':
                gui.print_trap_info(room[i][0])
                trap_data = lower.import_item_data(room[i][1], 'traps')
                choice = gui.input_choice(room[i][3][0], room[i][3][1], room[i][3][2])

                player_data = lower.trap(choice, player_data, trap_data)

            elif room[i][2] == 'Разветвление':
                gui.print_branching_info(room[i][0])
                choice = gui.input_choice(room[i][3][0], room[i][3][1])
                player_data = lower.location_change(room[i][3][0], room[i][3][1], choice, player_data)

                lower.export_player_data(char_name, player_data)
                break

            elif room[i][2] == 'Описание':
                gui.print_description_event_info(room[i][0], room[i][1])
                gui.continue_button()


            # В случае если персонаж имеет некорректные параметры, они заменяются здесь
            player_data = lower.stats_fix(player_data)

            # В случае если персонаж имеет высокий уровень радиации у него отнимается здоровье
            player_data = lower.radiation_sickness(player_data)

            if player_data['hp'] <= 0:
                return 'dead'

            elif room[i][2] == 'Исход':
                lower.export_player_data(char_name, player_data)
                gui.continue_button()
                return 'end'

def death(char_name: str) -> str:
    '''
    Если игрок умирает, он получает +1 к кол-во смертей. После чего у игрока запрашиваются дальнейшие действия -
    начать снова/главное меню/выйти.
    :param char_name: str (имя персонажа)
    :return:
    '''

    player_data = lower.import_data(f'characters/{char_name}.json')
    player_data['death_count'] += 1
    lower.export_player_data(char_name, player_data)

    status = gui.input_death_menu_choice()

    return status



