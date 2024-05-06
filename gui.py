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

    if answer.lower() in '1 новая игра':
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

    if answer.lower() in '1 перезаписать персонажа':
        answer = 'rewrite'
    else:
        answer = 'back'

    return answer

def char_not_exists() -> None:
    print(f'{gr_color}Персонажа с таким именем не существует.{end_color}')

def print_character_creation_start(char_name) -> None:
    print(f'\033[5;36m[temp]\033[0m В определенном месте и в определенное время сидите вы {char_name}')

def input_roleplay_genesis() -> str:
    print(f'''{gr_color}Ваше происхождение:{end_color}
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

    if genesis.lower() in '1 человек':
        genesis = 'Человек'
    elif genesis.lower() in '2 гуль':
        genesis = 'Гуль'
    else:
        genesis = 'Супермутант'

    return genesis

def input_roleplay_role(genesis: str) -> str:
    print(f'{gr_color}Вашей профессией является:{end_color}')
    if genesis == 'Человек':
        print(f'''{bl_color}[1]{end_color} {gr_color}Караванщик{end_color}
{bl_color}[2]{end_color} {gr_color}Рейдер (мародер, налетчик){end_color}''')
        role = input(f'{gr_color}>> {end_color}')

        while (role != '1' and role != '2'
               and role.lower() != 'караванщик'
               and role.lower() != 'рейдер'
               and role.lower() != 'мародер'
               and role.lower() != 'налетчик'):
            role = input(f'{gr_color}Введите команду или ее номер: {end_color}')

        if role.lower() in '1 караванщик':
            role = 'Караванщик'
        else:
            role = 'Рейдер'

        return role

    elif genesis == 'Гуль':
        print(f'''{bl_color}[1]{end_color} {gr_color}Караванщик{end_color}
{bl_color}[2]{end_color} {gr_color}Старатель{end_color}''')
        role = input(f'{gr_color}>> {end_color}')

        while (role != '1' and role != '2'
               and role.lower() != 'караванщик'
               and role.lower() != 'старатель'):
            role = input(f'{gr_color}Введите команду или ее номер: {end_color}')

        if role.lower() in '1 караванщик':
            role = 'Караванщик'
        else:
            role = 'Старатель'

        return role

    elif genesis == 'Супермутант':
        print(f'''{bl_color}[1]{end_color} {gr_color}Тень{end_color}
{bl_color}[2]{end_color} {gr_color}Странник{end_color}''')
        role = input(f'{gr_color}>> {end_color}')

        while (role != '1' and role != '2'
               and role.lower() != 'тень'
               and role.lower() != 'странник'):
            role = input(f'{gr_color}Введите команду или ее номер: {end_color}')

        if role.lower() in '1 тень':
            role = 'Тень'
        else:
            role = 'Странник'

        return role

def print_start_game_exposition(char_name: str, perk: str) -> None:
    if perk == 'Переговорщик':
        print(f'''{gr_color}В суровом мире пустоши, оставшейся после ядерной катастрофы, ты - {char_name}, 
караванщик нашел прибежище в баре города Хаб. Здесь, среди развалин былой цивилизации, 
ты зарабатываешь на жизнь, перевозя редкие ресурсы и товары между поселениями. 
Твои навыки переговоров делают тебя незаменимым для выживания в этом опасном мире.{end_color}''')

    elif perk == 'Адреналин':
        print(f'''{gr_color}В мрачном мире пустыни, оставшейся после ядерной катастрофы, ты - {char_name}, 
рейдер, нашел прибежище в баре города Хаб. Cреди развалин былой цивилизации, 
ты зарабатываешь на жизнь, грабя неосторожных путешественников и терроризируя поселения. 
Твоя хладнокровность делают тебя грозным противником для всех, кто осмеливается бросить тебе вызов.{end_color}''')

    elif perk == 'Торговец':
        print(f'''{gr_color}В суровом мире пустоши, оставшейся после ядерной катастрофы, ты - {char_name}, 
гуль-караванщик, нашел прибежище в баре города Хаб. Здесь, среди развалин былой цивилизации, 
ты зарабатываешь на жизнь, перевозя редкие ресурсы и товары между поселениями. 
Твоя устойчивость к радиации делают тебя незаменимым для выживания в этом опасном мире.{end_color}''')

    elif perk == 'Изыскатель':
        print(f'''{gr_color}В суровом мире пустоши, оставшейся после ядерной катастрофы,
находясь в городе Хаб, ты - {char_name}, гуль-старатель, нашел свое пристанище в местном баре. 
Несмотря на враждебное отношение многих людей к твоему виду, ты преуспеваешь в своем деле, 
добывая ценные ресурсы из облученной земли. Твоя способность находить ценные вещи 
среди кучи мусора способствуют твоему выживанию в этом опасном мире.{end_color}''')

    elif perk == 'Элита':
        print(f'''{gr_color}В суровом мире пустоши ты - {char_name}, бывший член элитного подразделения армии Создателя, 
находишь себя сидя в баре города Хаба. Твоя сила и выносливость делают тебя идеальным наемником, 
способным выполнять самые сложные задания, а твоя способность передвигаться незамеченным 
позволяет избегать опасностей пустоши.{end_color}''')

    elif perk == 'Адаптивность':
        print(f'''{gr_color}В суровом мире пустоши ты - {char_name}, бывший член армии Создателя, 
находишь себя сидя в баре города Хаба. Твоя сила и выносливость делают тебя идеальным воином, 
способным сражаться с любыми опасностями пустоши, а твоя способность адаптироваться к любым условиям 
позволяет выживать в самых экстремальных ситуациях.{end_color}''')

def button_continue() -> None:
    print(f'{bl_color}[1] {gr_color}Продолжить{end_color}')
    input(f'{gr_color}>> {end_color}')

def print_prelude_to_the_journey() -> None:
    print(f'''{gr_color}Вам предстоит отправиться в дальний путь, чтобы выполнить свои обязанности. 
Будь то перевозка товаров между поселениями, поиск редких ресурсов или борьба с опасными врагами.
Отправляйтесь в путь, чтобы узнать, чего стоит ваша жизнь в этом безжалостном мире.{end_color}''')

def input_stats_or_go():
    print(f'''{bl_color}[1]{end_color} {gr_color}Статистика персонажа{end_color}
{bl_color}[2]{end_color} {gr_color}Отправиться в путь{end_color}''')
    answer = input(f'{gr_color}>> {end_color}')

    while (answer != '1' and answer != '2'
           and answer.lower() != 'статистика'
           and answer.lower() != 'статистика персонажа'
           and answer.lower() != 'отправиться'
           and answer.lower() != 'отправиться в путь'):
        answer = input(f'{gr_color}Введите команду или ее номер: {end_color}')

    if answer.lower() in '1 статистика персонажа':
        answer = 'stats'
    else:
        answer = 'go'

    return answer

def print_stats(stats, char_name):
    print(f'''Имя: {char_name}
Происхождение: {stats['genesis']}
Перк: {stats['perk']}
Здоровье: {stats['hp']}
Броня: {stats['armor']}
Урон: {stats['damage']}
Доп. урон: {stats['bdamage']}
Уровень радиации: {stats['rad_level']}
Инвентарь: {stats['inventory'] if len(stats['inventory']) > 0 else 'пуст'}''')

def input_choosing_a_road(roads_list):
    print(f'''{gr_color}Выберите путь:{end_color}
{bl_color}[1]{end_color} {gr_color}{roads_list[0]}{end_color}
{bl_color}[2]{end_color} {gr_color}{roads_list[1]}{end_color}
{bl_color}[3]{end_color} {gr_color}{roads_list[2]}{end_color}''')
    road = input(f'{gr_color}>> {end_color}')

    while (road != '1' and road != '2' and road != '3'
           and road.lower() != f'{roads_list[0]}'.lower()
           and road.lower() != f'{roads_list[1]}'.lower()
           and road.lower() != f'{roads_list[2]}'.lower()):
        road = input(f'{gr_color}Введите команду или ее номер: {end_color}')

    if road.lower() in f'1 {roads_list[0]}'.lower():
        road = f'{roads_list[0]}'
    elif road.lower() in f'2 {roads_list[1]}'.lower():
        road = f'{roads_list[1]}'
    else:
        road = f'{roads_list[2]}'

    return road

def input_choosing_a_room(road, rooms_list):
    print(f'''{gr_color}Направляясь в локацию {road} вы встречаете различные места,
где потенциально можно найти припасы для дальнейшего пути. В какое из них вы направитесь?
{bl_color}[1]{end_color} {gr_color}{rooms_list[0]}{end_color}
{bl_color}[2]{end_color} {gr_color}{rooms_list[1]}{end_color}
{bl_color}[3]{end_color} {gr_color}{rooms_list[2]}{end_color}''')
    room = input(f'{gr_color}>> {end_color}')

    while (room != '1' and room != '2' and room != '3'
           and room.lower() != f'{rooms_list[0]}'.lower()
           and room.lower() != f'{rooms_list[1]}'.lower()
           and room.lower() != f'{rooms_list[2]}'.lower()):
        room = input(f'{gr_color}Введите команду или ее номер: {end_color}')

    if room.lower() in f'1 {rooms_list[0]}'.lower():
        room = '1'
    elif room.lower() in f'2 {rooms_list[1]}'.lower():
        room = '2'
    else:
        room = '3'

    return room

def print_event(text: str):
    print(rf'{gr_color}{text}{end_color}')

def input_choice(choice_text_1, choice_text_2):
    print(f'''{bl_color}[1]{end_color} {gr_color}{choice_text_1}{end_color}
{bl_color}[2]{end_color} {gr_color}{choice_text_2}{end_color}''')
    choice = input(f'{gr_color}>> {end_color}')

    while (choice != '1' and choice != '2'
           and choice.lower() not in f'{choice_text_1}'.lower()
           and choice.lower() not in f'{choice_text_2}'.lower()):
        choice = input(f'{gr_color}Введите команду или ее номер: {end_color}')

        if choice.lower() in f'1 {choice_text_1}'.lower():
            choice = '1'
        elif choice.lower() in f'2 {choice_text_2}'.lower():
            choice = '2'

        return choice

def print_enemy_info(current_enemy_data: dict):
    print(f'''{gr_color}Имя: {current_enemy_data['name']}
Тип: {current_enemy_data['type']}
Описание: {current_enemy_data['description']}{end_color}''')
    button_continue()

def input_player_attack():
    print('[1] Атака')
    input(f'>>')

def input_enemy_attack(pl_hp):
    print('Вас атаковали.')
    print(f'Ваше здоровье теперь равно: {pl_hp}')