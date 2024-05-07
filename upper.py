import os.path

import gui
import lower

def new_or_load_game() -> str:
    '''
    Определяет (посредством коммуникации с игроком) нужно ли создать новую игру или загрузить существующий профиль.
    :return: str: выбранное имя персонажа.
    '''
    lower.check_char_directory()
    while True:
        char_status = gui.ask_new_or_load()
        char_name = gui.character_name()
        if lower.character_deifne(char_status, char_name) == False:
            print('\033[5;36m[temp]\033[0m Возврат в главное меню т.к. такой персонаж уже есть,'
                  'либо его нет при попытке загрузиться')
            continue
        else:
            print(f'\033[5;36m[temp]\033[0m Персонаж {char_name} создан/перезаписан/загружен')
            break

    return char_name

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

def character_creation(char_name) -> None:
    genesis = gui.input_roleplay_genesis()
    role = gui.input_roleplay_role(genesis)
    perk = lower.perk_define(genesis, role)
    gui.print_start_game_exposition(char_name, perk)
    lower.save_start_profile(char_name, genesis, role, perk)
    gui.button_continue()

def prelude_to_the_journey(char_name):
    gui.print_prelude_to_the_journey()
    while True:
        answer = gui.input_stats_or_go()

        if answer == 'stats':
            lower.print_import_stats(char_name)
            gui.button_continue()
            continue

        elif answer == 'go':
            return

def choosing_a_road():
    roads_list = lower.import_dir_list('paths')
    road = gui.input_choosing_a_road(roads_list)
    return road

def passing_the_rooms(road, char_name):
    room_count = 0
    player_data = lower.import_data(f'characters/{char_name}.json')

    while True:

        if room_count == 0:
            room_name = 'Начало пути.txt'

        room = lower.convert_room_to_events_matrix(road, room_name)

        for i in range(0, len(room), 1):
            if player_data == False:
                return 'dead'

            gui.print_event(room[i][0])

            if room[i][2] == 'Враг':
                enemy_data = lower.import_specific_item_data(room[i][1],'enemies')
                gui.print_enemy_info(enemy_data)
                choice = gui.input_choice(room[i][3][0], room[i][3][1])

                if choice == '1':
                    player_data = lower.state_of_combat(char_name, player_data, enemy_data)

                elif choice == '2' and enemy_data['hostility'] > player_data['charisma']:
                    player_data = lower.state_of_combat(char_name, player_data, enemy_data)

                elif choice == '2' and enemy_data['hostility'] < player_data['charisma']:
                    gui.print_dodged_by_charisma()
                    pass

            if room[i][2] == 'Сокровище':
                item_data = lower.import_specific_item_data(room[i][1], 'items')
                choice = gui.input_choice(room[i][3][0], room[i][3][1])

                if choice == '1':
                    lower.use_item(item_data, player_data)

                elif choice == '2':
                    pass
            
        lower.export_player_data(char_name, player_data)







