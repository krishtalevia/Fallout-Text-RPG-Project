import os.path

import gui
import lower
import json

def main_menu() -> str:
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

def character_creation(char_name) -> None:
    genesis = gui.input_roleplay_genesis()
    role = gui.input_roleplay_role(genesis)
    perk = lower.perk_define(genesis, role)
    gui.print_start_game_exposition(char_name, perk, role)
    lower.save_start_profile(char_name, genesis, role, perk)
    gui.continue_button()

def prelude_to_the_journey(char_name):

    while True:
        answer = gui.input_stats_or_go()

        if answer == 'stats':
            lower.print_import_stats(char_name)
            gui.continue_button()
            continue

        elif answer == 'go':
            return

def choosing_a_road(char_name):

    roads_list = lower.import_dir_list('paths')
    road = gui.input_choosing_road(roads_list)

    player_data = lower.import_data(f'characters/{char_name}.json')
    player_data['road'] = road
    lower.export_player_data(char_name, player_data)

def passing_the_rooms(char_name):
    player_data = lower.import_data(f'characters/{char_name}.json')

    while True:

        road = player_data['road']
        room_name = player_data['current_location']

        room = lower.convert_room_to_events_matrix(road, room_name)

        for i in range(0, len(room), 1):

            player_data, menu_choice = lower.menu(player_data, char_name)

            if menu_choice == 'exit':
                return 'exit'

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
                gui.print_treasure_info(room[i][0], room[i][1])
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

            player_data = lower.radiation_sickness(player_data)
            player_data = lower.stats_fix()

            if player_data['hp'] <= 0:
                return 'dead'

            elif room[i][2] == 'Исход':
                gui.continue_button()
                return 'end'

def death(char_name):
    with open(f'characters/{char_name}.json', 'r', encoding='utf-8') as file:
        player_data = json.load(file)
        player_data['death_count'] += 1

    with open(f'characters/{char_name}.json', 'w', encoding='utf-8') as file:
        json.dump(player_data, file, ensure_ascii=False)

    status = gui.input_death_menu_choice()

    return status






