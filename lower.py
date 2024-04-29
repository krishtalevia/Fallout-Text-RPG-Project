import os
import gui

def check_char_directory() -> None:
    if not os.path.isdir('characters'):
        os.makedirs('characters')
        print('\033[5;36m[temp]\033[0m Папки содержащей профили не существовало, папка создана.')

def character_deifne(char_status, char_name) -> None:
    if char_status == 'new' and os.path.exists(rf'characters/{char_name}.txt') == True:
        answer = gui.char_exists()

        if answer == 'rewrite':
            file = open(fr'characters/{char_name}.txt', 'w', encoding='utf-8')
            file.close()
            return True
        else:
            return False

    elif char_status == 'new' and os.path.exists(rf'characters/{char_name}.txt') == False:
        file = open(fr'characters/{char_name}.txt', 'w', encoding='utf-8')
        file.close()
        return True

    elif char_status == 'load' and os.path.exists(rf'characters/{char_name}.txt') == False:
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