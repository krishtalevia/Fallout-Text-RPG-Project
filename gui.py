import gui_headers
import os

gr_color = '\033[0;32m'
bl_color = '\033[0;34m'
end_color = '\033[0m'
line = f'{gr_color}----------------------------------------------------------------------{end_color}'

def input_main_menu_choice() -> str:
    '''
    Запрашивает у игрока желает ли он начать игру с начала, продолжить или выйти из игры.
    :return: str: Ответ "new", "load" или "exit".
    '''
    try_count = 0

    while True:
        os.system('cls')

        gui_headers.main_menu_header_ascii()
        gui_headers.header('Главное меню')
        print(f'{bl_color}[1]{end_color} {gr_color}Новая игра{end_color}')
        print(f'{bl_color}[2]{end_color} {gr_color}Загрузить персонажа{end_color}')
        print(f'{bl_color}[3]{end_color} {gr_color}Выйти{end_color}')
        print(line)

        if try_count == 0:
            answer = input(f'{gr_color}> {end_color}')
        else:
            answer = input(f'{bl_color}(введите команду или ее номер) {gr_color}> {end_color}')

        if (answer != '1' and answer != '2' and answer != '3' and
           answer.lower() != 'новая игра' and
           answer.lower() != 'новая' and
           answer.lower() != 'загрузить' and
           answer.lower() != 'загрузить персонажа' and
           answer.lower() != 'выйти'):

            try_count += 1

            continue
        else:
            break

    if answer.lower() in '1 новая игра':
        answer = 'new'

    elif answer.lower() in '2 загрузить персонажа':
        answer = 'load'

    elif answer.lower() in '3 выйти':
        answer = 'exit'

    return answer

def character_name() -> str:
    '''
    Запрашивает у игрока имя персонажа.
    :return: str: имя персонажа.
    '''
    os.system('cls')

    gui_headers.header('Имя вашего персонажа?')

    char_name = input(f'{gr_color}> {end_color}')

    return char_name

def char_exists() -> str:
    '''
    Запрос действий у игрока в случае, если персонаж с таким именем уже существует.
    Варианты "вернуться" и "перезаписать персонажа"
    :return: str: rewrite, back
    '''
    try_count = 0

    while True:
        os.system('cls')

        gui_headers.header('Персонаж с таким именем уже существует')

        print(f'{bl_color}[1]{end_color} {gr_color}Перезаписать персонажа{end_color}')
        print(f'{bl_color}[2]{end_color} {gr_color}Вернуться в главное меню{end_color}')

        print(line)

        if try_count == 0:
            answer = input(f'{gr_color}> {end_color}')
        else:
            answer = input(f'{bl_color}(введите команду или ее номер) {gr_color}> {end_color}')

        if (answer != '1' and answer != '2'
               and answer.lower() != 'перезаписать'
               and answer.lower() != 'перезаписать персонажа'
               and answer.lower() != 'вернуться'
               and answer.lower() != 'вернуться к выбору'):

            try_count += 1
            continue

        else:
            break

    if answer.lower() in '1 перезаписать персонажа':
        answer = 'rewrite'
    else:
        answer = 'back'

    return answer

def continue_button(header_text) -> None:
    '''
    Вывод в консоль сообщения, после которого игрок вернется в исходное положение.
    Для этого игрок должен подтвердить возврат.
    :param header_text: текст сообщения
    :return: None
    '''
    try_count = 0

    while True:
        os.system('cls')

        gui_headers.header(header_text)

        print(f'{bl_color}[1]{end_color} {gr_color}Продолжить{end_color}')

        print(line)

        if try_count == 0:
            answer = input(f'{gr_color}> {end_color}')
        else:
            answer = input(f'{bl_color}(введите команду или ее номер) {gr_color}> {end_color}')

        if answer not in '1 продолжить':

            try_count += 1

            continue

        else:
            break

def input_roleplay_genesis() -> str:
    try_count = 0

    while True:
        os.system('cls')

        gui_headers.header('Определите Ваше происхождение:')

        print(f'{bl_color}[1]{end_color} {gr_color}Человек{end_color}')
        print(f'{bl_color}[2]{end_color} {gr_color}Гуль{end_color}')
        print(f'{bl_color}[3]{end_color} {gr_color}Супермутант{end_color}')

        print(line)

        if try_count == 0:
            genesis = input(f'{gr_color}> {end_color}')
        else:
            genesis = input(f'{bl_color}(введите команду или ее номер){gr_color}> {end_color}')

        if (genesis != '1' and genesis != '2' and genesis != '3'
               and genesis.lower() != 'человек'
               and genesis.lower() != 'гуль'
               and genesis.lower() != 'супермутант'
               and genesis.lower() != 'мутант'):

            try_count += 1

            continue

        else:
            break

    if genesis.lower() in '1 человек':
        genesis = 'Человек'
    elif genesis.lower() in '2 гуль':
        genesis = 'Гуль'
    else:
        genesis = 'Супермутант'

    return genesis

def genesis_info(genesis):
    if genesis == 'Человек':
        os.system('cls')

        gui_headers.header('Человек:')

        print(f'{gr_color}')
        print('Обычные люди, потомки тех, кто пережил ядерный апокалипсис.')
        print('Однако являющиеся слегка мутированными, ввиду того, что')
        print('проживают на загрязненной радиацией пустоши.')
        print()
        print(f'* Харизма {bl_color}+5%')
        print(f'{gr_color}')
        print('Профессии на выбор:')
        print('--------------------')
        print('*Караванщик: Навыки переговоров делают его незаменимым для')
        print('выживания во время походов между поселениями.')
        print()
        print('*Рейдер: Хладнокровность делает его грозным противником для')
        print('всех, кто осмеливается бросить ему вызов.')

    elif genesis == 'Гуль':
        print(f'{gr_color}')
        print('Подвергшиеся воздействию радиации и ВРЭ люди. Они отличаются')
        print('деформированными чертами лица ввиду слезающей с них кожи.')
        print('Обладают увеличенной продолжительностью жизни. Многие люди')
        print('воспринимают гулей враждебно.')
        print()
        print(f'{gr_color}* Харизма {bl_color}-15%')
        print(f'{gr_color}* {bl_color}Сопротивление радиации{gr_color}')
        print()
        print('Профессии на выбор:')
        print('--------------------')
        print('*Караванщик: Навыки торговли делают его незаменимым для')
        print('выживания во время походов между поселениями.')
        print(f'Перк: {bl_color}Торговец{end_color}')
        print()
        print('*Изыскатель: Способность находить ценные вещи среди кучи')
        print('мусора способствуют его выживанию в этом опасном мире.')
        print(f'Перк: {bl_color}Изыскатель{end_color}')

    elif genesis == 'Супермутант':
        print(f'{gr_color}')
        print('Подвергшиеся воздействию ВРЭ люди. Данный вирус вызвал у них')
        print('радикальный рост мускулатуры и выносливости, однако их внешний')
        print('вид стал сильно отличаться от человеческого. У значительной')
        print('части супермутантов снизился уровень интеллекта.')
        print()
        print(f'{gr_color}* {bl_color}Осутствие харизмы{end_color} на начальном этапе')
        print(f'{gr_color}* {bl_color}Сопротивление радиации{gr_color}')
        print(f'{gr_color}* {bl_color}Здоровье +20%{gr_color}')
        print()
        print('Профессии на выбор:')
        print('--------------------')
        print('*Тень: Бывшие члены элитного подразделения Создателя. Еще')
        print('более сильны и выносливы. Однако страдают от шизофрении.')
        print(f'Перк: {bl_color}Элита{end_color}')
        print()
        print('*Странник: способность адаптироваться к любым условиям')
        print('позволяет ему выживать в самых экстремальных ситуациях.')
        print(f'Перк: {bl_color}Адаптивность{end_color}')


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

def print_event(text: str):
    print(rf'{gr_color}{text}{end_color}')

def input_choice(choice_text_1, choice_text_2, choice_text_3=None):
    print(f'''{bl_color}[1]{end_color} {gr_color}{choice_text_1}{end_color}
{bl_color}[2]{end_color} {gr_color}{choice_text_2}{end_color}''')
    if choice_text_3 != None:
        print(f'[3] {choice_text_3}')
    choice = input(f'{gr_color}>> {end_color}')

    while True:
        if choice == '3' and choice_text_3 == None:
            choice = input(f'{gr_color}Введите команду или ее номер: {end_color}')
            continue

        while (choice != '1' and choice != '2' and choice != '3'
               and choice.lower() != f'{choice_text_1}'.lower()
               and choice.lower() != f'{choice_text_2}'.lower()
               and choice.lower() != f'{choice_text_3}'.lower()):

            choice = input(f'{gr_color}Введите команду или ее номер: {end_color}')

        if choice.lower() in f'1 {choice_text_1}'.lower():
            choice = '1'
        elif choice.lower() in f'2 {choice_text_2}'.lower():
            choice = '2'
        elif choice.lower() in f'3 {choice_text_3}'.lower():
            choice = '3'

        return choice

def print_enemy_info(current_enemy_data: dict):
    print(f'''{gr_color}Имя: {current_enemy_data['name']}
Тип: {current_enemy_data['type']}
Описание: {current_enemy_data['description']}{end_color}''')
    button_continue()

def input_player_attack():
    print('[1] Атака')
    input(f'>> ')

def print_enemy_attack(pl_hp):
    print('Вас атаковали.')
    print(f'Ваше здоровье теперь равно: {pl_hp}')

def print_dodged_by_charisma():
    print('Вам удалось избежать сражения благодаря харизме.')

def input_loot_for_win_by_charisma(item_name):
    print(f'От противника вам достался предмет {item_name}, вы хотите себе его оставить?')
    print('[1] Да')
    print('[2] Нет')
    answer = input('>> ')

    while (answer != '1' and answer != '2' and
           answer.lower() != 'да' and
           answer.lower() != 'нет'):
        answer = input(f'{gr_color}Введите Ваш ответ: {end_color}')

    if answer.lower() in '1 да':
        answer = 'yes'
    elif answer.lower() in f'2 нет':
        answer = 'no'

    return answer

def input_item_for_use(player_data):
    player_inventory = player_data['inventory']
    print(player_inventory)
    print('Введите название предмета для его использования (либо "вернуться"): ')
    item_name = input('>> ')

    while item_name not in player_inventory and item_name.lower() != 'вернуться':
        item_name = input(f'{gr_color}Введите название предмета: {end_color}')

    if item_name.lower() == 'вернуться':
        item_name = 'back'

    return item_name

def input_loot_choice(enemy_data):
    print('Введите название предмета, который Вы хотите взять: ')
    print(f'[1] {enemy_data['loot'][0]}')
    print(f'[2] {enemy_data['loot'][1]}')
    print(f'[3] Ничего не брать')
    item_name = input('>> ')

    while (item_name != '1' and item_name != '2' and item_name != '3' and
           item_name.lower() != enemy_data['loot'][0].lower() and
           item_name.lower() != enemy_data['loot'][1].lower() and
           item_name.lower() != 'ничего не брать' and item_name.lower() != 'ничего'):
        item_name = input(f'{gr_color}Введите название предмета: {end_color}')

    if item_name.lower() in '3 ничего не брать':
        return None
    elif item_name.lower() in f'1 {enemy_data['loot'][0]}'.lower():
        item_name = enemy_data['loot'][0]
    elif item_name.lower() in f'2 {enemy_data['loot'][1]}'.lower():
        item_name = enemy_data['loot'][1]

    return item_name

def input_menu_choice():
    print('[1] Продолжить путь')
    print('[2] Использовать предмет')
    print('[3] Выйти (прогресс комнаты не сохраняется)')
    menu_choice = input('>> ')

    while (menu_choice != '1' and menu_choice != '2' and menu_choice != '3' and
           menu_choice.lower() != 'продолжить путь' and
           menu_choice.lower() != 'использовать предмет' and
           menu_choice.lower() != 'выйти'):
        menu_choice = input(f'{gr_color}Введите Ваш выбор: {end_color}')

    if menu_choice.lower() in '1 продолжить путь':
        return 'go'
    elif menu_choice.lower() in '2 использовать предмет':
        return 'use_item'
    else:
        return 'exit'

def input_death_menu_choice():
    print('[1] Начать прохождение снова')
    print('[2] Вернуться в главное меню')
    print('[3] Выйти')
    menu_choice = input('>> ')

    while (menu_choice != '1' and menu_choice != '2' and menu_choice != '3' and
           menu_choice.lower() != 'начать прохождение снова' and
           menu_choice.lower() != 'вернуться в главное меню' and
           menu_choice.lower() != 'вернуться в меню' and
           menu_choice.lower() != 'выйти'):

        menu_choice = input(f'{gr_color}Введите Ваш выбор: {end_color}')

    if menu_choice.lower() in '1 начать прохождение снова':
        return 'again'
    elif menu_choice.lower() in '2 вернуться в главное меню':
        return 'to_main_menu'
    elif menu_choice.lower() in '3 выйти':
        return 'exit'