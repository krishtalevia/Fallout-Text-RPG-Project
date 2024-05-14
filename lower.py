import os
import gui
import json
import random


def check_char_directory() -> None:
    '''
    Проверка на то, существует ли папка "characters" где хранятся профили.
    :return:
    '''

    if not os.path.isdir('characters'):
        os.makedirs('characters')

def character_deifne(load_status: str, char_name: str) -> bool:
    '''
    Определение того, что выбрал игрок (новая игра/загрузить), и в зависимости от ответов - профиль перезаписывается,
    создается новый или загружается уже существующий.
    :param load_status: str (новая игра/загрузить)
    :param char_name: str (имя персонажа)
    :return: bool
    '''

    if load_status == 'new' and os.path.exists(rf'characters/{char_name}.json') == True:
        answer = gui.char_exists()

        if answer == 'rewrite':
            file = open(fr'characters/{char_name}.json', 'w', encoding='utf-8')
            file.close()
            return True
        else:
            return False

    elif load_status == 'new' and os.path.exists(rf'characters/{char_name}.json') == False:
        file = open(fr'characters/{char_name}.json', 'w', encoding='utf-8')
        file.close()
        return True

    elif load_status == 'load' and os.path.exists(rf'characters/{char_name}.json') == False:

        return False

    elif load_status == 'load':

        return True

def perk_define(genesis: str, role: str) -> str:
    '''
    Определение перка в зависимости от происхождения и роли, которые выбрал игрок.
    :param genesis: str (происхождение)
    :param role: str (профессия/роль)
    :return: str: (название перка)
    '''

    if genesis == 'Человек':  # +5 к харизме
        if role == 'Караванщик':
            perk = 'Переговорщик'  # +10 к харизме
        elif role == 'Рейдер':
            perk = 'Адреналин'  # +15 к бонусному урону, если здоровье падает ниже 25

    elif genesis == 'Гуль':  # -15 к харизме, сопротивление к радиации
        if role == 'Караванщик':
            perk = 'Торговец'  # +20 к харизме
        elif role == 'Старатель':
            perk = 'Стрелок'  # +20 к меткости

    elif genesis == 'Супермутант':  # отсутствие харизмы, сопротивление к радиации +20 к исходному здоровью
        if role == 'Тень':
            perk = 'Элита'  # +15 к броне
        elif role == 'Странник':
            perk = 'Солдат'  # +10 к меткости

    return perk


def save_start_profile(char_name: str, genesis: str, role: str, perk: str) -> None:
    '''
    Определение исходных параметров созданного персонажа и создание json файла с этими параметрами.
    :param char_name: str (имя персонажа)
    :param genesis: str (происхождение)
    :param role: str (профессия/роль)
    :param perk: str (перк)
    :return:
    '''

    rad_level = 0

    charisma = 25
    if perk == 'Переговорщик':
        charisma = 35
    if genesis == 'Супермутант':
        charisma = 0
    if perk == 'Торговец':
        charisma = 20
    if perk == 'Стрелок':
        charisma = 5

    accuracy = 55
    if perk == 'Стрелок':
        accuracy = 75
    if perk == 'Солдат':
        accuracy = 65

    armor = 0
    if role == 'Элита':
        armor = 15

    parameters = {'genesis': genesis,
                  'role': role,
                  'perk': perk,
                  'hp': 70 if role == 'Супермутант' else 50,
                  'armor': armor,
                  'damage': 10,
                  'bdamage': 0,
                  'rad_level': rad_level,
                  'charisma': charisma,
                  'accuracy': accuracy,
                  'inventory': [],
                  'death_count': 0,
                  'kill_count': 0,
                  'room_count': 0,
                  'current_location': 'Начало пути.txt',
                  'road': None}

    with open(rf'characters/{char_name}.json', 'w', encoding='utf-8') as profile:
        json.dump(parameters, profile, ensure_ascii=False)

def print_import_stats(char_name: str) -> None:
    '''
    Импорт профиля и вывод его параметров в консоль.
    :param char_name: str (имя персонажа)
    :return:
    '''

    path = rf'characters/{char_name}.json'
    stats = import_data(path)
    gui.print_stats(stats, char_name)

def import_data(path: str) -> str:
    '''
    Импорт данных в виде строки из указанного по пути файла.
    :param path: str (путь до файла)
    :return: str (данные в виде строки)
    '''

    with open(path, 'r', encoding='utf-8') as profile:
        data = json.load(profile)

    return data

def export_player_data(char_name: str, player_data: dict) -> None:
    '''
    Экспорт данных персонажа в json файл, который находится в папке для персонажей.
    :param char_name: str (имя персонажа)
    :param player_data: dict (данные персонажа)
    :return:
    '''

    with open(f'characters/{char_name}.json', 'w', encoding='utf-8') as profile:
        json.dump(player_data, profile, ensure_ascii=False)

def import_dir_list(path: str) -> list:
    '''
    Импорт списка директорий по указанному пути.
    :param path: str (указанный путь)
    :return: list (список директорий)
    '''

    return os.listdir(path)

def convert_room_to_events_matrix(road: str, room_name='Начало пути.txt') -> list:
    '''
    Импорт и перевод комнаты (локации) из строки в матрицу исходя из заданного подземелья (пути) и названия комнаты.
    :param road: str (подземелье)
    :param room_name: str (комната)
    :return: list (комната в виде матрицы)
    '''

    with open(fr'paths/{road}/{room_name}', 'r', encoding='utf-8') as file:
        room_file = file.read()

    room_lines = room_file.split('|||')

    room = []

    for i in room_lines:
        events = i.split('||')
        choices = events[-1].split('|')
        del events[-1]

        events.append(choices)
        room.append(events)

    return room

def state_of_combat(char_name: str, player_data: dict, enemy_data: dict) -> dict:
    '''
    Состояние боя, где сначала ходит игрок отнимая здоровье противнику, после чего ходит противник. Так до тех пор,
    пока у игрока или противника здоровье не будет меньше или равно нулю.
    :param char_name: str (имя персонажа)
    :param player_data: dict (данные персонажа)
    :param enemy_data: dict (данные противника)
    :return: dict (данные персонажа)
    '''

    move = 'player'

    if enemy_data['is_rad'] == 'Да':
        rad_hit = enemy_data['rad']
    else:
        rad_hit = 0

    while True:
        gui.print_state_of_combat(char_name, player_data, enemy_data)

        if move == 'player':
            dice = random.randint(0,100)

            if dice >= player_data['accuracy']:
                hit_status = 'missed'
            else:
                hit_status = 'hit'

            if player_data['perk'] == 'Адреналин' and player_data['hp'] < 25:
                adrenaline_damage = 15
            else:
                adrenaline_damage = 0

            gui.input_player_attack(player_data, enemy_data, hit_status, adrenaline_damage)

            if hit_status == 'hit':
                enemy_data['hp'] -= (player_data['damage'] + player_data['bdamage'] + adrenaline_damage)


            if enemy_data['hp'] <= 0:
                player_data['kill_count'] += 1

                # Определение предмета упавшего с противника и выбор предмета игроком
                player_data = player_get_loot_for_win(enemy_data, player_data)

                return player_data

            move = 'enemy'
            continue

        else:
            dice = random.randint(0, 100)

            if dice >= enemy_data['accuracy']:
                hit_status = 'missed'
            else:
                hit_status = 'hit'

            gui.input_enemy_attack(player_data, enemy_data, hit_status, rad_hit)

            if hit_status == 'hit':

                if player_data['armor'] > 0:
                    player_data['armor'] -= enemy_data['damage']
                else:
                    player_data['hp'] -= enemy_data['damage']
                    player_data['rad_level'] += rad_hit

            if int(player_data['hp']) <= 0:

                return player_data

            else:
                move = 'player'
                continue

def import_item_data(item_name: str, type_name: str) -> dict:
    '''
    Импорт данных предмета/противника.
    :param item_name: str (название противника/предмета)
    :param type_name: str (противник это или предмет)
    :return: dict (данные  противника/предмета)
    '''

    buff = import_data(f'{type_name}.json')

    if type_name != 'items':
        item_data = buff[item_name]

    else:
        if item_name in buff['Обычные']:
            item_data = buff['Обычные'][item_name]

        elif item_name in buff['Редкие']:
            item_data = buff['Редкие'][item_name]

        elif item_name in buff['Легендарные']:
            item_data = buff['Легендарные'][item_name]

        else:
            item_data = buff['Капсула'][item_name]

    return item_data

def use_item(player_data: dict) -> dict:
    '''
    Использование выбранного игроком предмета с выводом эффекта в консоль.
    :param player_data: dict (данные персонажа)
    :return: dict (данные персонажа)
    '''

    # Выбор предмета
    item_name = gui.input_item_for_use(player_data)

    if item_name != 'back':
        item_data = import_item_data(item_name, 'items')
        parameter = item_data['eff_parameter']
        effect = item_data['eff']

        # Определение рандомного параметра, если выбран предмет "Капсула"
        random_parameter_index = random.randint(0, len(parameter)-1)

        if item_name == 'Капсула':
            parameter = parameter[random_parameter_index]

            random_effect_index = random.randint(0, len(effect)-1)
            effect = effect[random_effect_index]

        # Персонаж получает эффект от предмета
        player_data[parameter] += effect

        # Вывод эффекта в консоль
        gui.print_item_use_effect(item_data['eff_description'], item_name, effect, item_data, random_parameter_index)

        # Удаление предмета из инвентаря
        for i in range(0, len(player_data['inventory']), 1):
            if player_data['inventory'][i] == f'{item_name}':
                del player_data['inventory'][i]
                return player_data

    else:
        return player_data

def stats_fix(player_data: dict) -> dict:
    '''
    Коррекция параметров которые не могут быть ниже нуля. Или возвращегие уровня радиации к нулю у персонажей
    с сопротивлением к его изменению.
    :param player_data: dict (данные персонажа)
    :return: dict (данные персонажа)
    '''

    if player_data['bdamage'] < 0:
        player_data['bdamage'] = 0
    if player_data['armor'] < 0:
        player_data['armor'] = 0
    if player_data['rad_level'] < 0:
        player_data['rad_level'] = 0

    if player_data['genesis'] == 'Супермутант' or player_data['genesis'] == 'Гуль':
        player_data['rad_level'] = 0

    return player_data

def take_item(item_name: str, player_data: dict) -> dict:
    '''
    Добавление предмета в инвентарь.
    :param item_name: str (название предмета)
    :param player_data: dict (данные персонажа)
    :return: dict (данные персонажа)
    '''

    player_data['inventory'].append(item_name)

    gui.print_item_taken(item_name)

    return player_data

def get_random_item_from_category(item_category: str) -> dict:
    '''
    Определение случайного предмета из выбранной категории редкости.
    :param item_category: str (название категории редкости (например "Легендарные")
    :return: dict: (данные предмета)
    '''

    items = import_data('items.json')

    category_items = list(items[item_category].keys())

    random_item = random.choice(category_items)

    return random_item

def player_get_loot_for_win(enemy_data: dict, player_data: dict, win_by='combat') -> dict:
    '''
    Определение предмета который получит игрок за победу над противником посредством сражения или харизмы.
    :param enemy_data: dict (данные противника)
    :param player_data: dict (данные персонажа)
    :param win_by: str (победа посредством сражения или харизмы)
    :return: dict (данные персонажа)
    '''

    # Случайное определение категории редкости предмета
    dice = random.randint(0,100)
    categories = ['Обычные', 'Редкие', 'Легендарные']

    for i in range(0, len(categories), 1):
        if categories[i] == enemy_data['loot'][0]:
            del categories[i]
            break

    if dice < 85:
        random_item_1 = get_random_item_from_category(enemy_data['loot'][0])
    else:
        dice = random.randint(0,1)
        random_item_1 = get_random_item_from_category(categories[dice])

    random_item_2 = get_random_item_from_category(enemy_data['loot'][1])

    # Если игрок выиграл посредством сражения ему на выбор дается два предмета
    if win_by == 'combat':
        item_name = gui.input_loot_choice_for_win(random_item_1, random_item_2)

        if item_name != None:
            player_data['inventory'].append(item_name)
            return player_data
        else:
            return player_data

    # Если игрок выиграл посредством харизмы ему предлагается один предмет
    else:
        random_loot = random.randint(0,1)

        if random_loot == 1:
            item_name = random_item_1
        else:
            item_name = random_item_2

        answer = gui.input_loot_for_win_by_charisma(item_name)

        if answer == 'yes':
            player_data['inventory'].append(item_name)
            return player_data
        else:
            return player_data

def charisma_check(player_data: dict, enemy_data: dict) -> bool:
    '''
    Проверка на харизму.
    :param player_data: dict (данные персонажа)
    :param enemy_data: dict (данные противника)
    :return: bool
    '''

    if player_data['charisma'] > enemy_data['hostility']:
        gui.print_dodged_by_charisma()
        return True
    else:
        gui.failed_charisma()
        return False

def menu(player_data: dict, char_name: str) -> dict:
    '''
    Меню с выбором продолжить/использовать предмет/выйти.
    :param player_data: dict (данные персонажа)
    :param char_name: str (имя персонажа)
    :return: dict (данные персонажа) опционально: str: (выход)
    '''

    while True:
        menu_choice = gui.input_menu_choice(player_data, char_name)

        if menu_choice == 'go':
            return player_data, menu_choice

        elif menu_choice == 'use_item':
            if len(player_data['inventory']) == 0:
                gui.inventory_is_empty()
                gui.continue_button()

            else:
                player_data = use_item(player_data)
                player_data = stats_fix(player_data)

                if player_data['hp'] <= 0:
                    return 'dead', None

            continue

        elif menu_choice == 'exit':
            return player_data, menu_choice

def trap(choice: str, player_data: dict, trap_data: dict) -> dict:
    '''
    Определение параметров и результата события "ловушка".
    :param choice: str (выбор сделанный ранее игроком)
    :param player_data: dict (данные персонажа)
    :param trap_data: dict (данные "ловушки")
    :return: dict (данные персонажа)
    '''

    eff_parameter = trap_data['eff_parameter']
    eff_parameter_name = trap_data['eff_parameter_name']
    win = trap_data['win']
    eff = trap_data['eff']

    # Определение шанса на успех
    dice = random.randint(1, 100)

    res = 'lose'

    if choice == '1':
        if dice < trap_data['1st chance']:
            player_data[eff_parameter] += eff
        else:
            res = 'win'

    elif choice == '2':
        if dice < trap_data['2nd chance']:
            player_data[eff_parameter] += eff
        else:
            res = 'win'

    elif choice == '3':
        if dice < trap_data['3rd chance']:
            player_data[eff_parameter] += eff
        else:
            res = 'win'

    if res == 'lose':
        gui.print_trap_fail(eff, eff_parameter_name)

    elif res == 'win':
        player_data[win['parameter']] + win['eff']
        gui.print_trap_success(trap_data['is_succ_eff'], win['eff'], win['name'])
        
    return player_data

def location_change(location_name_1: str, location_name_2: str, choice: str, player_data: dict) -> dict:
    '''
    Смена комнаты (локации), которая будет записана в профиль персонажа (json файл)
    :param location_name_1: str (название локации)
    :param location_name_2: str (название локации)
    :param choice: str (выбор игрока)
    :param player_data: dict (данные персонажа)
    :return: dict (данные персонажа)
    '''

    if choice == '1':
        player_data['current_location'] = f'{location_name_1}.txt'
    else:
        player_data['current_location'] = f'{location_name_2}.txt'

    return player_data

def radiation_sickness(player_data: dict) -> dict:
    '''
    При высоком уровне радиации у персонажа, у него отнимается здоровье.
    :param player_data: dict (данные персонажа)
    :return: dict (данные персонажа)
    '''

    if player_data['genesis'] == 'Человек':
        if player_data['rad_level'] > 100:
            gui.print_radiation_sickness()
            player_data['hp'] -= 20

    return player_data

