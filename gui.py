gr_color = '\033[0;32m'
bl_color = '\033[0;34m'
end_color = '\033[0m'

def print_start():
    print(f'{gr_color}Приветственное окно.{end_color}')

def ask_new_or_load() -> str:
    '''
    Запрашивает у игрока хочет ли он начать игру с начала или продолжить.
    :return: str: Ответ "new" или "load".
    '''
    print(f'{gr_color}Вы хотите начать новую игру или продолжить?{end_color}')
    print(f'''{bl_color}[1]{end_color} {gr_color}Новая игра{end_color}
{bl_color}[2]{end_color} {gr_color}Загрузить персонажа{end_color}''')
    answer = input(f'{gr_color}>> {end_color}')

    while (answer != '1' and answer != '2' and answer.lower() != 'новая игра'
           and answer.lower() != 'новая' and answer.lower() != 'загрузить' and answer.lower() != 'загрузить персонажа'):
        answer = input(f'{gr_color}Введите команду или ее номер: {end_color}')

    if answer in '1 новая игра':
        answer = 'new'
    else:
        answer = 'load'

    return answer

def character_name() -> str:
    '''
    Запрашивает у игрока имя персонажа.
    :return: str: имя персонажа.
    '''
    char_name = input(f'{gr_color}Введите имя персонажа: {end_color}')

    return char_name

def char_exists() -> str:
    print(f'''{gr_color}Персонаж с таким именем уже существует.{end_color}
{bl_color}[1]{end_color} {gr_color}Перезаписать персонажа.{end_color}
{bl_color}[2]{end_color} {gr_color}Вернуться к выбору "загрузить/новая игра".{end_color}''')
    answer = input(f'{gr_color}>> {end_color}')

    while (answer != '1' and answer != '2'
           and answer.lower() != 'перезаписать'
           and answer.lower() != 'перезаписать персонажа'
           and answer.lower() != 'вернуться'
           and answer.lower() != 'вернуться к выбору'):
        answer = input(f'{gr_color}Введите команду или ее номер: {end_color}')

    if answer in '1 перезаписать персонажа':
        answer = 'rewrite'
    else:
        answer = 'back'

    return answer

def char_not_exists() -> None:
    print(f'{gr_color}Персонажа с таким именем не существует.{end_color}')

def print_character_creation_start(char_name) -> None:
    print(f'\033[5;36m[temp]\033[0m В определенном месте и в определенное время сидите вы {char_name}')

def input_roleplay_genesis() -> str:
    print(f'''{gr_color}Вашей происхождение:{end_color}
    {bl_color}[1]{end_color} {gr_color}Человек{end_color}
    {bl_color}[2]{end_color} {gr_color}Гуль{end_color}
    {bl_color}[3]{end_color} {gr_color}Супермутант{end_color}''')
    genesis = input(f'{gr_color}>> {end_color}')

    while (genesis != '1' and genesis != '2' and genesis != '3'
           and genesis.lower() != 'человек'
           and genesis.lower() != 'гуль'
           and genesis.lower() != 'супермутант'
           and genesis.lower() != 'мутант'):
        genesis = input(f'{gr_color}Введите команду или ее номер: {end_color}')

        if genesis in '1 человек':
            genesis = 'caravaneer'
        elif genesis in '2 гуль':
            genesis = 'ghoul'
        else:
            genesis = 'supermutant'

        return genesis

def input_roleplay_role() -> str:
    pass
    # print(f'''{gr_color}Вашей профессией является:{end_color}
    # {bl_color}[1]{end_color} {gr_color}Караванщик{end_color}
    # {bl_color}[2]{end_color} {gr_color}Рейдер (мародер, налетчик){end_color}''')
    # role = input(f'{gr_color}>> {end_color}')
    #
    # while (role != '1' and role != '2'
    #        and role.lower() != 'караванщик'
    #        and role.lower() != 'рейдер'
    #        and role.lower() != 'мародер'
    #        and role.lower() != 'налетчик'):
    #     role = input(f'{gr_color}Введите команду или ее номер: {end_color}')
    #
    #     if role in '1 караванщик':
    #         role = 'caravaneer'
    #     else:
    #         role = 'raider'
    #
    #     return role