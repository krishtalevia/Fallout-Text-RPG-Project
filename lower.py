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
            perk = 'Переговорщик'  # 30% шанс мирного решения конфликтных ситуаций, -20% цены (если будет)
        elif role == 'Рейдер':
            perk = 'Адреналин'  # +10 к бонусному урону, если здоровье падает меньше 50%

    elif genesis == 'Гуль':
        if role == 'Караванщик':
            perk = 'Сопротивление рад.'  # уровень радиации всегда равен 0
        elif role == 'Старатель':
            perk = 'Изыскатель'  # 30% вероятность найти дополнительный предмет

    elif genesis == 'Супермутант':
        if role == 'Тень':
            perk = 'Стелс-бой'  # атака с использованием этого перка дает возможность удвоить урон
        elif role == 'Странник':
            perk = 'Адаптивность'  # 40% резист к отнимающим здоровье предметам

    return perk


def save_start_profile(char_name, genesis, role, perk) -> None:
    parameters = {'genesis': genesis,
                  'role': role,
                  'perk': perk,
                  'hp': 100 if role == 'Супермутант' else 70,
                  'armor': 0,
                  'damage': 10,
                  'bdamage': 0,
                  'rad_level': 0,
                  'inventory': []}

    with open(rf'characters/{char_name}.json', 'w', encoding='utf-8') as profile:
        json.dump(parameters, profile, ensure_ascii=False)


def print_import_stats(char_name):
    stats = import_profile_data(char_name)
    gui.print_stats(stats, char_name)

def import_profile_data(char_name):
    with open(rf'characters/{char_name}.json', 'r', encoding='utf-8') as profile:
        data = json.load(profile)

    return data

def import_dir_list(path: str) -> list:
    return os.listdir(path)