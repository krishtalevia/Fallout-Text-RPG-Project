import os
import gui
import json

def check_char_directory() -> None:
    if not os.path.isdir('characters'):
        os.makedirs('characters')
        print('\033[5;36m[temp]\033[0m Папки содержащей профили не существовало, папка создана.')

def character_deifne(char_status, char_name) -> None:
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
    if genesis == 'human':
        if role == 'caravaneer':
            perk = 'negotiator'
        elif role == 'raider':
            perk = 'adrenaline'

    elif genesis == 'ghoul':
        if role == 'caravaneer':
            perk = 'rad_resistance'
        elif role == 'prospector':
            perk = 'fortune_finder'

    elif genesis == 'supermutant':
        if role == 'nightkin':
            perk = 'ghost'
        elif role == 'wanderer':
            perk = 'toughness'

    return perk

def save_start_profile(char_name, genesis, role, perk) -> None:
    parameters = {'genesis': genesis,
                  'role': role,
                  'perk': perk,
                  'hp': 100 if role == 'supermutant' else 70,
                  'armor': 0,
                  'damage': 10,
                  'bdamage': 0,
                  'inventory': []}

    with open(rf'characters/{char_name}.json', 'w', encoding='utf-8') as profile:
        json.dump(parameters, profile, ensure_ascii=False)

