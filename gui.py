gr_color = '\033[0;32m'
bl_color = '\033[0;34m'
end_color = '\033[0m'

def print_start():
    print(f'{gr_color}Приветственное окно.{end_color}')

def ask_new_or_load():
    print(f'{gr_color}Вы хотите начать новую игру или продолжить?{end_color}')
    print(f'''{bl_color}[1]{end_color} {gr_color}Новая игра{end_color}
{bl_color}[2]{end_color} {gr_color}Загрузить персонажа{end_color}''')
    answer = input('')

    while (answer != '1' and answer != '2' and answer.lower() != 'новая игра'
           and answer.lower() != 'новая' and answer.lower() != 'загрузить' and answer.lower() != 'загрузить персонажа'):
        answer = input(f'{gr_color}Введите команду или ее номер: {end_color}')

    if answer in '1 новая игра':
        answer = 'new'
    else:
        answer = 'load'

    return answer