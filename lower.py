import os
import gui
import json


def check_char_directory() -> None:
    if not os.path.isdir('characters'):
        os.makedirs('characters')
        print('\033[5;36m[temp]\033[0m Папки содержащей профили не существовало, папка создана.')


def character_deifne(char_status, char_name) -> bool:
    if char_status == 'new' and os.path.exists(rf'characters/{char_name}.json') == True:
        answer = gui.char_exists()

        if answer == 'rewrite':
            file = open(fr'characters/{char_name}.json', 'w', encoding='utf-8')
            file.close()
            return True
        else:
            return False

    elif char_status == 'new' and os.path.exists(rf'characters/{char_name}.json') == False:
        file = open(fr'characters/{char_name}.json', 'w', encoding='utf-8')
        file.close()
        return True

    elif char_status == 'load' and os.path.exists(rf'characters/{char_name}.json') == False:
        gui.char_not_exists()
        return False

    elif char_status == 'load':
        return True


def perk_define(genesis: str, role: str) -> str:
    if genesis == 'Человек':
        if role == 'Караванщик':
            perk = 'Переговорщик'  # +20 к харизме
        elif role == 'Рейдер':
            perk = 'Адреналин'  # +10 к бонусному урону, если здоровье падает меньше 50%

    elif genesis == 'Гуль':  # -15 к харизме, сопротивление к радиации
        if role == 'Караванщик':
            perk = 'Торговец'  # +20 к харизме
        elif role == 'Старатель':
            perk = 'Изыскатель'  # 30% вероятность найти дополнительный предмет

    elif genesis == 'Супермутант':  # -15 к харизме, +30 к здоровью
        if role == 'Тень':
            perk = 'Элита'  # +25 к броне
        elif role == 'Странник':
            perk = 'Адаптивность'  # 40% резист к отнимающим здоровье предметам

    return perk


def save_start_profile(char_name, genesis, role, perk) -> None:
    rad_level = 0
    if genesis == 'Гуль':
        rad_level = None

    charisma = 20
    if role == 'Переговорщик':
        charisma = 40
    elif genesis == 'Супермутант' or role == 'Изыскатель':
        charisma = 5
    elif role == 'Торговец':
        charisma = 25

    armor = 0
    if role == 'Элита':
        armor = 25

    parameters = {'genesis': genesis,
                  'role': role,
                  'perk': perk,
                  'hp': 100 if role == 'Супермутант' else 70,
                  'armor': armor,
                  'damage': 10,
                  'bdamage': 0,
                  'rad_level': rad_level,
                  'charisma': charisma,
                  'inventory': [],
                  'death_count': 0,
                  'kill_count': 0,
                  'room_count': 0}

    with open(rf'characters/{char_name}.json', 'w', encoding='utf-8') as profile:
        json.dump(parameters, profile, ensure_ascii=False)


def print_import_stats(char_name):
    path = rf'characters/{char_name}.json'
    stats = import_data(path)
    gui.print_stats(stats, char_name)

def import_data(path):
    with open(path, 'r', encoding='utf-8') as profile:
        data = json.load(profile)

    return data

def export_player_data(char_name, player_data):
    with open(f'characters/{char_name}.json', 'w', encoding='utf-8') as profile:
        json.dump(player_data, profile, ensure_ascii=False)

def import_dir_list(path: str) -> list:
    return os.listdir(path)

def convert_room_to_events_matrix(road: str, room_name='Начало пути.txt') -> list:
    with open(fr'paths/{road}/{room_name}', 'r', encoding='utf-8') as file:
        room_file = file.read()

    room_lines = room_file.split('\n')

    buff_events = []
    buff_choices = []
    events = []
    choices = []
    room = []

    for i in room_lines:
        events_and_choices = i.split('||')
        buff_events.append(events_and_choices[0])
        buff_choices.append(events_and_choices[1])

    for i in buff_choices:
        buff = i.split('|')
        choices.append(buff)
        if len(choices[-1][-1]) == 0:
            del choices[-1][-1]

    for i in buff_events:
        buff = i.split(',')
        events.append(buff)
        if len(events[-1][-1]) == 0:
            del events[-1][-1]

    for i in range(0, len(events), 1):
        buff = events[i] + [choices[i]]
        room.append(buff)

    return room


def state_of_combat(char_name, pl_data, enemy_data):

    while True:
        print(f'Здоровье врага равно: {enemy_data['hp']}')
        gui.input_player_attack()
        enemy_data['hp'] -= (pl_data['damage'] + pl_data['bdamage'])
        print(f'Здоровье врага равно: {enemy_data['hp']}')

        if enemy_data['hp'] <= 0:
            print('Враг побежден')

            pl_data['kill_count'] += 1

            break

        print('Вас атакуют.')
        if pl_data['armor'] > 0:
            pl_data['armor'] -= enemy_data['damage']
        else:
            pl_data['hp'] -= enemy_data['damage']

        print(f'Ваше здоровье: {pl_data['hp']}')

        if pl_data['hp'] <= 0:
            return False
            # импорт death_count +1 напрямую

        else:
            continue

    return pl_data

def import_item_data(item_name, type_name):
    buff = import_data(f'{type_name}.json')
    item_data = buff[item_name]

    return item_data

def use_item(player_data):
    item_name = gui.input_item_for_use(player_data)
    if item_name != 'back':
        item_data = import_item_data(item_name, 'items')

        parameter = item_data['aff_parameter']

        print(f'Вы используете {item_data['name']}')

        player_data[parameter] += item_data['aff']
        print(f'Эффект: {item_data['aff_description']}')

        del player_data['inventory'][f'{item_name}']

        return player_data
    else:
        return

def take_item(item_name, player_data):
    player_data['inventory'].append(item_name)
    print(f'Вы взяли предмет {item_name}')

    return player_data

def player_get_loot_for_win(enemy_data, player_data):
    item_name = gui.input_loot_choice(enemy_data)
    if item_name != None:
        player_data['inventory'].append(item_name)
        return player_data
    else:
        return

