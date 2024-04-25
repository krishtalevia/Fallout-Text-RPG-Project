gr_color = '\033[0;32m'
bl_color = '\033[0;34m'
end_color = '\033[0m'

def print_start():
    print(f'{gr_color}Приветственное окно.{end_color}')

def ask_new_or_load():
    print(f'{gr_color}Вы хотите начать новую игру или продолжить?{end_color}')
    print(f'''{bl_color}[1]{end_color} {gr_color}Новая игра{end_color}
{bl_color}[2]{end_color} {gr_color}Загрузить персонажа{end_color}''')

print(f'{gr_color}Вы хотите начать новую игру или продолжить?{end_color}')
print(f'''{bl_color}[1]{end_color} {gr_color}Новая игра{end_color}
{bl_color}[2]{end_color} {gr_color}Загрузить персонажа{end_color}''')