import gui_support

# для очищения консоли
import os

import winsound

# для корректной работы цветов в консоли
import ctypes
kernel32 = ctypes.windll.kernel32
kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)

gr_color = '\033[0;32m'
bl_color = '\033[0;34m'
red_color = '\033[0;31m'
yl_color = '\033[0;33m'
ppl_color = '\033[0;35m'
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

        gui_support.main_menu_header_ascii()
        gui_support.header('Главное меню')
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

            play_sound('error')
            continue
        else:
            break

    if answer.lower() in '1 новая игра':
        answer = 'new'

    elif answer.lower() in '2 загрузить персонажа':
        answer = 'load'

    elif answer.lower() in '3 выйти':
        answer = 'exit'

    play_sound('menu_click')
    return answer

def character_name() -> str:
    '''
    Запрашивает у игрока имя персонажа.
    :return: str: имя персонажа
    '''

    try_count = 0

    while True:

        os.system('cls')

        gui_support.header('Имя вашего персонажа?')

        if try_count == 0:
            char_name = input(f'{gr_color}> {end_color}')
        else:
            char_name = input(f'{bl_color}(имя персонажа не может быть пустым){gr_color} > {end_color}')

        if char_name == '':
            try_count += 1

            play_sound('error')
            continue

        play_sound('menu_click_2')
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

        gui_support.header('Персонаж с таким именем уже существует')

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

            play_sound('error')
            continue

        else:

            play_sound('menu_click')
            break

    if answer.lower() in '1 перезаписать персонажа':
        answer = 'rewrite'
    else:
        answer = 'back'

    return answer

def back_button(header_text) -> None:
    '''
    Вывод в консоль сообщения, после которого игрок вернется в исходное положение.
    Для этого игрок должен подтвердить возврат.
    :param header_text: текст сообщения
    :return: None
    '''

    try_count = 0

    while True:
        os.system('cls')

        gui_support.header(header_text)

        print(f'{bl_color}[1]{end_color} {gr_color}Вернуться{end_color}')

        print(line)

        if try_count == 0:
            answer = input(f'{gr_color}> {end_color}')
        else:
            answer = input(f'{bl_color}(введите команду или ее номер) {gr_color}> {end_color}')

        if answer not in '1 вернуться':

            try_count += 1

            play_sound('error')
            continue

        else:
            play_sound('menu_click_2')
            break

def input_roleplay_genesis() -> str:
    '''
    Запрашивает у игрока на выбор "происхождение" персонажа.
    :return: str (происхождение)
    '''

    try_count = 0

    while True:
        os.system('cls')

        gui_support.header('Ваше происхождение?')

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

            play_sound('error')
            continue

        else:

            play_sound('menu_click')

            if genesis == '1' or genesis.lower == 'человек':
                answer = genesis_info('Человек')
                if answer == 'yes':
                    return 'Человек'
                else:
                    continue

            elif genesis == '2' or genesis.lower() == 'гуль':
                answer = genesis_info('Гуль')
                if answer == 'yes':
                    return 'Гуль'
                else:
                    continue

            else:
                answer = genesis_info('Супермутант')
                if answer == 'yes':
                    return 'Супермутант'
                else:
                    continue

def genesis_info(genesis: str) -> str:
    '''
    Выводит в консоль инфо о происхождении которое выбрал игрок, после чего игрок подтверждает свой выбор.
    В ином случае он возвращается к выбору происхождения.
    :param genesis: str: происхождение
    :return: str: "yes" или "no"
    '''

    if genesis == 'Человек':
        os.system('cls')

        gui_support.header('Человек:')

        print(f'{gr_color}Обычные люди, потомки тех, кто пережил ядерный апокалипсис.')
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
        print()

    elif genesis == 'Гуль':
        os.system('cls')

        gui_support.header('Гуль')

        print(f'{gr_color} Гули - подвергшиеся воздействию радиации и ВРЭ люди. Они отличаются')
        print('деформированными чертами лица ввиду слезающей с них кожи. Обладают')
        print('увеличенной продолжительностью жизни.')
        print('Многие люди воспринимают гулей враждебно.')
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
        print(f'{gr_color}*Старатель: Меткость и опыт выживания в одиночку')
        print('способствуют его выживанию в этом опасном мире.')
        print(f'Перк: {bl_color}Стрелок{end_color}')
        print()

    elif genesis == 'Супермутант':
        os.system('cls')

        gui_support.header('Супермутант')

        print(f'{gr_color}Супермутанты - подвергшиеся воздействию ВРЭ люди. Данный вирус вызвал')
        print('у них радикальный рост мускулатуры и выносливости, однако их внешний')
        print('вид стал сильно отличаться от человеческого. У значительной')
        print('части супермутантов снизился уровень интеллекта.')
        print()
        print(f'{gr_color}* {bl_color}Осутствие харизмы{end_color} {gr_color}на начальном этапе')
        print(f'* {bl_color}Сопротивление радиации{gr_color}')
        print(f'{gr_color}* {bl_color}Здоровье +20%{gr_color}')
        print()
        print('Профессии на выбор:')
        print('--------------------')
        print('*Тень: Бывшие члены элитного подразделения Создателя. Еще')
        print('более сильны и выносливы. Однако страдают от шизофрении.')
        print(f'Перк: {bl_color}Элита{end_color}')
        print()
        print(f'{gr_color}*Странник: опыт службы в армии Создателя позволяет')
        print('ему выживать в самых экстремальных ситуациях.')
        print(f'Перк: {bl_color}Солдат{end_color}')
        print()

    print(f'{gr_color}Вы выбираете данное происхождение?{end_color} {bl_color}(да/нет){end_color}')

    print(line)

    while True:
        answer = input(f'{gr_color}> {end_color}')

        if answer.lower() != 'да' and answer.lower() != 'нет':

            play_sound('error')
            continue

        else:
            break

    if answer.lower() in 'да':
        answer = 'yes'
    else:
        answer = 'no'

    play_sound('menu_click')
    return answer

def input_roleplay_role(genesis: str) -> str:
    '''
    Запрашивает у игрока профессию/роль персонажа.
    :param genesis: происхождение
    :return: профессия/роль
    '''

    try_count = 0

    while True:
        os.system('cls')

        gui_support.header('Ваша роль?')

        if genesis == 'Человек':
            print(f'{bl_color}[1]{end_color} {gr_color}Караванщик{end_color}')
            print(f'{bl_color}[2]{end_color} {gr_color}Рейдер (мародер, налетчик){end_color}')

            print(line)

            if try_count == 0:
                role = input(f'{gr_color}> {end_color}')
            else:
                role = input(f'{bl_color}(введите команду или ее номер){gr_color}> {end_color}')

            if (role != '1' and role != '2'
                    and role.lower() != 'караванщик'
                    and role.lower() != 'рейдер'
                    and role.lower() != 'мародер'
                    and role.lower() != 'налетчик'):

                try_count += 1

                play_sound('error')
                continue

            else:
                play_sound('menu_click')

                if role == '1' or role.lower() == 'караванщик':
                    answer = role_info('Человек', 'Караванщик')
                    if answer == 'yes':
                        return 'Караванщик'
                    else:

                        continue

                elif (role in '2' or role.lower() == 'рейдер'
                      or role.lower() == 'налетчик'
                      or role.lower() == 'мародер'):
                    answer = role_info('Человек', 'Рейдер')
                    if answer == 'yes':
                        return 'Рейдер'
                    else:

                        continue

        elif genesis == 'Гуль':
            print(f'{bl_color}[1]{end_color} {gr_color}Караванщик{end_color}')
            print(f'{bl_color}[2]{end_color} {gr_color}Старатель{end_color}')

            print(line)

            if try_count == 0:
                role = input(f'{gr_color}> {end_color}')
            else:
                role = input(f'{bl_color}(введите команду или ее номер){gr_color}> {end_color}')

            if (role != '1' and role != '2'
                    and role.lower() != 'караванщик'
                    and role.lower() != 'старатель'):

                try_count += 1

                play_sound('error')
                continue

            else:

                play_sound('menu_click')
                if role == '1' or role.lower() == 'караванщик':
                    answer = role_info('Гуль', 'Караванщик')
                    if answer == 'yes':
                        return 'Караванщик'

                    else:
                        continue

                elif role == '2' or role.lower() == 'старатель':
                    answer = role_info('Гуль', 'Старатель')
                    if answer == 'yes':
                        return 'Старатель'

                    else:
                        continue

        elif genesis == 'Супермутант':
            print(f'{bl_color}[1]{end_color} {gr_color}Тень{end_color}')
            print(f'{bl_color}[2]{end_color} {gr_color}Странник{end_color}')

            print(line)

            if try_count == 0:
                role = input(f'{gr_color}> {end_color}')
            else:
                role = input(f'{bl_color}(введите команду или ее номер){gr_color}> {end_color}')

            if (role != '1' and role != '2'
                    and role.lower() != 'тень'
                    and role.lower() != 'странник'):

                try_count += 1

                play_sound('error')
                continue

            else:

                play_sound('menu_click')
                if role == '1' or role.lower() == 'тень':
                    answer = role_info('Супермутант', 'Тень')
                    if answer == 'yes':
                        return 'Тень'

                    else:
                        continue

                elif role in '2' or role.lower() == 'Странник':
                    answer = role_info('Супермутант', 'Странник')
                    if answer == 'yes':
                        return 'Странник'

                    else:
                        continue

def role_info(genesis: str, role: str) -> str:
    '''
    Выводит в консоль информацию о роли, после чего запрашивает согласен ли игрок на выбор этой роли.
    :param genesis: str (происхождение)
    :param role: str (роль)
    :return: str (да или нет)
    '''
    if genesis == 'Человек' and role == 'Караванщик':
        os.system('cls')

        gui_support.header('Караванщик:')

        print(f'{gr_color}Зарабатывает на жизнь, перевозя редкие ресурсы и товары')
        print('между поселениями.')
        print()
        print(f'Перк "Переговорщик": Харизма {bl_color}+10%{end_color}\n')

    elif role == 'Рейдер':
        os.system('cls')

        gui_support.header('Гуль')

        print(f'{gr_color}Зарабатывает на жизнь грабя неосторожных путешественников')
        print('и терроризируя поселения.')
        print()
        print(f'Перк "Адреналин": {bl_color}+15{end_color}{gr_color} к доп. урону, если здоровье падает ниже 25\n')

    elif role == 'Караванщик':
        os.system('cls')

        gui_support.header('Караванщик')

        print(f'{gr_color}Зарабатывает на жизнь, перевозя редкие ресурсы и товары')
        print('между поселениями.')
        print()
        print(f'Перк "Торговец": Харизма {bl_color}+20%{end_color}{gr_color}\n')

    elif role == 'Старатель':
        os.system('cls')

        gui_support.header('Старатель')

        print(f'{gr_color}Старатели зарабатывают себе на жизнь находя в заброшенных')
        print('местах ценные вещи, для последующей их продажи.')
        print()
        print(f'Перк "Стрелок": {bl_color}+20%{end_color}{gr_color} к меткости\n')

    elif role == 'Тень':
        os.system('cls')

        gui_support.header('Тень')

        print(f'{gr_color}После смерти Создателя, наиболее мирные из Теней стали зарабатывать')
        print('работая наемниками, обладая особыми навыками и экипировкой.')
        print()
        print(f'Перк "Элита": {bl_color}+15{end_color}{gr_color} брони\n')

    elif role == 'Странник':
        os.system('cls')

        gui_support.header('Странник')

        print(f'{gr_color}После смерти Создателя, многие Супермутанты растворились в пустоши,')
        print('находя в различной деятельности, где нужна сила и выносливость.')
        print()
        print(f'Перк "Солдат": {bl_color}+10%{end_color}{gr_color} к меткости\n')

    print(f'{gr_color}Вы выбираете данную профессию?{end_color} {bl_color}(да/нет){end_color}')

    print(line)

    while True:
        answer = input(f'{gr_color}> {end_color}')

        if answer.lower() != 'да' and answer.lower() != 'нет':

            play_sound('error')
            continue

        else:

            play_sound('menu_click')
            break

    if answer.lower() in 'да':
        answer = 'yes'
    else:
        answer = 'no'

    return answer

def print_start_game_exposition(char_name: str, perk: str, role: str) -> None:
    '''
    Выводит в консоль начальную экспозицию в зависимости от перка персонажа.
    :param char_name: str (имя персонажа)
    :param perk: str (перк)
    :param role: str (роль)
    :return:
    '''

    os.system('cls')

    gui_support.header('Описание')

    intro = (f'{gr_color}В суровом мире пустоши, оставшемся после ядерной катастрофы, Вы - {char_name}, \n'
             f'{role.lower()}, который нашел прибежище в баре города Хаб.\n'
             f'\n'
             f'Среди развалин былой цивилизации Вы зарабатываете на жизнь')

    if perk == 'Переговорщик' or perk == 'Торговец':
        print(f'{intro} перевозя \n'
              f'ресурсы и товары между поселениями.')

    elif perk == 'Адреналин':
        print(f'{intro} грабя \n'
              f'неосторожных путешественников и терроризируя поселения.')

    elif perk == 'Торговец':
        print(f'{intro}перевозя \n'
              f'редкие ресурсы и товары между поселениями.')

    elif perk == 'Стрелок':
        print(f'{intro} добывая \n'
              f'ценные ресурсы из облученной земли в одиночку.')

    elif perk == 'Элита':
        print(f'{intro} подрабатывая \n'
              f'наемником, используя свою силу и выносливость.')

    elif perk == 'Солдат':
        print(f'{intro} благодаря \n'
              f'своей меткости и выносливости.')

def continue_button() -> None:
    '''
    Кнопка "продолжить"
    :return:
    '''

    print(line)
    input(f'{gr_color}[Нажмите ENTER] > {end_color}')
    play_sound('menu_click_2')

def print_char_not_exist() -> None:
    '''
    Сообщение о том, что указанного персонажа не существует.
    :return:
    '''

    os.system('cls')

    gui_support.header('Ошибка')

    print(f'{gr_color}Персонажа с таким именем не существует')
    print(line)
    input(f'{gr_color}[Нажмите ENTER] > {end_color}')
    play_sound('menu_click_2')

def input_stats_or_go() -> str:
    '''
    Выбор просмотра статистики или перейти к выбору подземелья.
    :return: str (выбор да или нет)
    '''
    try_count = 0

    while True:
        os.system('cls')

        gui_support.header('Подготовка')

        print(f'{gr_color}Вам предстоит отправиться в дальний путь, с целью выполнить\n'
              f'свое предназначение. Будь то перевозка товаров между поселениями,\n'
              f'поиск редких ресурсов или борьба с опасными врагами.\n')

        print(f'Отправляйтесь в путь, чтобы узнать, чего стоит ваша жизнь в этом безжалостном мире.{end_color}\n')

        print(f'{bl_color}[1]{end_color} {gr_color}Информация о персонаже{end_color}')
        print(f'{bl_color}[2]{end_color} {gr_color}Отправиться в путь{end_color}')
        print(line)

        if try_count == 0:
            answer = input(f'{gr_color}> {end_color}')
        else:
            answer = input(f'{bl_color}(введите команду или ее номер) {gr_color}> {end_color}')

        if (answer != '1' and answer != '2'
               and answer.lower() != 'информация'
               and answer.lower() != 'информация о персонаже'
               and answer.lower() != 'отправиться'
               and answer.lower() != 'отправиться в путь'):

            try_count = 1

            play_sound('error')
            continue

        else:

            play_sound('menu_click_2')
            break

    if answer.lower() in '1 информация о персонаже':
        answer = 'stats'
    else:
        answer = 'go'

    return answer

def print_stats(stats: dict, char_name: str) -> None:
    '''
    Вывод в консоль информации о персонаже.
    :param stats: dict (данные персонажа)
    :param char_name: str (имя персонажа)
    :return:
    '''

    os.system('cls')

    gui_support.header('Информация о персонаже')

    print(f'{gr_color}Имя: {char_name}\t\t\t Происхождение: {stats['genesis']}')
    print(f'Здоровье: {stats['hp']}\t\t Перк: {stats['perk']}')
    print(f'Броня: {stats['armor']}\t\t Инвентарь: {stats['inventory'] if len(stats['inventory']) > 0 else 'пуст'}')
    print(f'Урон: {stats['damage']}\t\t Доп. урон: {stats['bdamage']}')
    print(f'Уровень радиации: {stats['rad_level']}\t\t Меткость: {stats['accuracy']}')

def input_choosing_road(roads_list: list) -> str:
    '''
    Выбор подземелья (пути) с предварительной информацией о нем.
    :param roads_list: (список подземелий)
    :return: str (название подземелья)
    '''

    try_count = 0

    while True:
        os.system('cls')

        gui_support.header('Выбор маршрута')

        print(f'{bl_color}[1]{end_color} {gr_color}{roads_list[0]}{end_color}')
        print(f'{bl_color}[2]{end_color} {gr_color}{roads_list[1]}{end_color}')
        print(f'{bl_color}[3]{end_color} {gr_color}{roads_list[2]}{end_color}')

        print(line)
        if try_count == 0:
            road = input(f'{gr_color}> {end_color}')
        else:
            road = input(f'{bl_color}(введите команду или ее номер){gr_color}>{end_color} ')

        if (road != '1' and road != '2' and road != '3'
               and road.lower() != f'{roads_list[0]}'.lower()
               and road.lower() != f'{roads_list[1]}'.lower()
               and road.lower() != f'{roads_list[2]}'.lower()):

            try_count = 1

            play_sound('error')
            continue
        else:
            play_sound('menu_click_2')

            if road == '1' or road.lower() == f'{roads_list[0]}'.lower():
                answer = road_info('Могильник')
                if answer == 'yes':
                    road = f'{roads_list[0]}'

                else:
                    continue

            elif road == '2' or road.lower() == f'{roads_list[1]}'.lower():
                answer = road_info('Некрополь')
                if answer == 'yes':
                    road = f'{roads_list[1]}'

                else:
                    continue

            else:
                answer = road_info('Свечение')
                if answer == 'yes':
                    road = f'{roads_list[2]}'

                else:
                    continue

            return road

def road_info(road_name: str) -> str:
    '''
    Вывод в консоль информации о выбранном пути с запросом на согласие.
    :param road_name: str (название пути)
    :return: str (да или нет)
    '''

    if road_name == 'Могильник':
        os.system('cls')

        gui_support.header('Могильник:')

        print(f'{gr_color}После начала ядерной войны подавляющее большинство\n'
              'населения Лос-Анджелеса погибло от радиации, голода,\n'
              'болезней и вследствие иных причин. Их кости десятилетия\n'
              'спустя остались лежать в зданиях и на улицах, придавая\n'
              'этому месту облик кладбища.\n')

        print('По направлению к этому месту предстоит ваш путь.\n')

        print(f'{gr_color}Сложность: {end_color}Легко')

    elif road_name == 'Некрополь':
        os.system('cls')

        gui_support.header('Некрополь:')

        print(f'{gr_color}Слава о ходячих мертвецах из Мёртвого города широко известна\n'
              'в Пустошах Калифорнии. Путешественники и торговцы стараются\n'
              'обходить город стороной.\n')

        print('По направлению к этому месту предстоит ваш путь.\n')

        print(f'{gr_color}Сложность: {yl_color}Средняя{end_color}')

    elif road_name == 'Свечение':
        os.system('cls')

        gui_support.header('Свечение:')

        print(f'{gr_color}Бывший исследовательский комплекс компании «Вест-Тек»\n'
              f'разрушенный прямым попаданием атомной бомбы. Уровень радиации\n'
              f'в развалинах был так высок, что они слабо светились по ночам,\n'
              f'и это место получило название «Свечение».\n')

        print('По направлению к этому месту предстоит ваш путь.\n')

        print(f'{gr_color}Сложность: {red_color}Высокая{end_color}')

    print(f'{gr_color}Вы выбираете данный путь?{end_color} {bl_color}(да/нет){end_color}')

    print(line)

    while True:
        answer = input(f'{gr_color}> {end_color}')

        if answer.lower() != 'да' and answer.lower() != 'нет':

            play_sound('error')
            continue

        else:

            play_sound('menu_click')
            break

    if answer.lower() in 'да':
        answer = 'yes'
    else:
        answer = 'no'

    return answer

def input_choice(choice_text_1: str, choice_text_2: str, choice_text_3=None) -> str:
    '''
    Выбор одного из указанного в событии варианта.
    :param choice_text_1: str (выбор в событии)
    :param choice_text_2: str (выбор в событии)
    :param choice_text_3: str (опциональный выбор в событии)
    :return: str (номер выбора)
    '''

    print(line)
    print(f'{bl_color}[1]{end_color} {gr_color}{choice_text_1}{end_color}')
    print(f'{bl_color}[2]{end_color} {gr_color}{choice_text_2}{end_color}')

    if choice_text_3 != None:
        print(f'{bl_color}[3]{end_color} {gr_color}{choice_text_3}{end_color}')

    choice = input(f'{gr_color}> {end_color}')

    while True:
        if choice == '3' and choice_text_3 == None:
            choice = input(f'{bl_color}(введите команду или ее номер) {gr_color}> {end_color}')

            play_sound('error')
            continue

        while (choice != '1' and choice != '2' and choice != '3'
               and choice.lower() != f'{choice_text_1}'.lower()
               and choice.lower() != f'{choice_text_2}'.lower()
               and choice.lower() != f'{choice_text_3}'.lower()):

            choice = input(f'{bl_color}(введите команду или ее номер) {gr_color}> {end_color}')

        if choice.lower() in f'1 {choice_text_1}'.lower():
            choice = '1'
        elif choice.lower() in f'2 {choice_text_2}'.lower():
            choice = '2'
        elif choice.lower() in f'3 {choice_text_3}'.lower():
            choice = '3'

        play_sound('menu_click')
        return choice

def print_trap_fail(effect: int, effect_parameter_name: str) -> None:
    '''
    Вывод в консоль сообщения о неудаче при решении "ловушки" и эффект на персонажа.
    :param effect: int (кол-во нанесенного эффекта)
    :param effect_parameter_name: (название параметра)
    :return:
    '''

    os.system('cls')

    gui_support.header('Неудача')

    play_sound('result')
    print(f'{gr_color}Вы получаете {yl_color}{effect}{gr_color} к параметру "{effect_parameter_name}"')

    continue_button()

def print_trap_success(is_succ_eff: str, win_eff: int, win_param_name: str) -> None:
    '''
    Вывод в консоль сообщения об успехе при решении "ловушки" и эффект на персонажа.
    :param is_succ_eff: str (есть ли эффект при успехе)
    :param win_eff: int (эффект в числе)
    :param win_param_name: str (название эффекта)
    :return:
    '''

    os.system('cls')

    gui_support.header('Успех')

    play_sound('result')
    print(f'{gr_color}Вы решили возникшую перед вами проблему.\n')

    if is_succ_eff == 'yes':
        print(f'Однако вы также получили {yl_color}{win_eff}{gr_color} к параметру "{win_param_name}"')

    continue_button()

def print_enemy_info(current_enemy_data: dict, event_text: str) -> None:
    '''
    Выводит в консоль текст события и информацию о противнике.
    :param current_enemy_data: dict (данные противника)
    :param event_text: str (текст события)
    :return:
    '''

    if current_enemy_data['loot'][0] == 'Обычные':
        category_color = end_color
    elif current_enemy_data['loot'][0] == 'Редкие':
        category_color = bl_color
    else:
        category_color = ppl_color

    os.system('cls')

    gui_support.header('Событие: Враг')

    print(f'{gr_color}{event_text}\n')

    print(f'Описание:')
    print('----------------')
    print(f'{gr_color}Имя: {current_enemy_data['name']}\t Тип: {current_enemy_data['type']}\n'
          f'Описание: {current_enemy_data['description']}\n'
          f'\n'
          f'Содержит предметы из категории:\n'
          f'{category_color}{current_enemy_data['loot'][0]}\t {gr_color}(наибольшая вероятность)\n'
          f'{end_color}{current_enemy_data['loot'][1]}\n'
          f'\n'
          f'{gr_color}С меньшим процентом могут выпасть предметы из других категорий.')

def print_treasure_info(event_text: str, item_data: dict, item_category: str, item_name: str) -> None:
    '''
    Выводит в консоль текст события и информацию о найденном предмете.
    :param event_text: str (текст события)
    :param item_data: dict (данные предмета)
    :param item_category: str (категория предмета)
    :param item_name: str (название предмета)
    :return:
    '''

    if item_category == 'Обычные' or item_category == 'Неизвестные':
        category_color = end_color
    elif item_category == 'Редкие':
        category_color = bl_color
    else:
        category_color = ppl_color

    os.system('cls')

    gui_support.header('Событие: Предмет')

    print(f'{gr_color}{event_text}\n')

    print(f'{gr_color}Название предмета: {yl_color}"{item_name}"{gr_color}')
    print(f'Категория: {category_color}{item_category}')
    print(f'{gr_color}Тип: {item_data['type']}')
    print(f'Эффект: {item_data['eff_description'] if item_category != 'Неизвестные' else 'Случайный'}')

    if item_data['add_eff_status'] == 'yes':
        print(f'Доп. эффект: {item_data['add_eff_description']}:')
    else:
        print(f'Доп. эффект: Нет')

def print_trap_info(event_text: str) -> None:
    '''
    Выводит в консоль текст события перед "ловушкой".
    :param event_text: str (текст события)
    :return:
    '''

    os.system('cls')

    gui_support.header('Событие: Задача')

    print(f'{gr_color}{event_text}\n')

    print(f'{gr_color}От вашего выбора зависит состояние вашего персонажа.{end_color}')

def print_description_event_info(event_text: str, header_text: str) -> None:
    '''
    Выводит в консоль текст события "Описание"
    :param event_text: str (текст события)
    :param header_text: str (заголовок события)
    :return:
    '''

    os.system('cls')

    gui_support.header(f'Событие: {header_text}')

    print(f'{gr_color}{event_text}\n')

def print_branching_info(event_text):
    '''
    Выводит в консоль текст события перед "разветвлением".
    :param event_text: str (текст события)
    :return:
    '''

    os.system('cls')

    gui_support.header('Событие: Разветвление')

    print(f'{gr_color}{event_text}\n')

    print(f'{gr_color}Куда Вы направитесь дальше?{end_color}')

def print_state_of_combat(char_name: str, player_data: dict, enemy_data: dict) -> None:
    '''
    Выводит в консоль инфо о персонаже и противнике.
    :param char_name: str (имя персонажа)
    :param player_data: dict (данные персонажа)
    :param enemy_data: dict (имя противника)
    :return:
    '''

    os.system('cls')

    gui_support.combat_header_ascii()
    gui_support.header('Сражение')

    print()
    print(f'{gr_color}{char_name}\t\t\t\t\t{enemy_data['name']}')
    print('--------------------\t\t\t--------------------')
    print(f'Здоровье: {player_data['hp']}\t\t\t\tЗдоровье: {enemy_data['hp']}')
    print(f'Броня: {player_data['armor']}\t\t\t\tУрон: {enemy_data['damage']}')
    print(f'Урон: {player_data['damage']}\t\t\t\tРадиация: {enemy_data['is_rad']}')
    print(f'Доп. урон: {player_data['bdamage']}\t')
    print(f'Уровень рад.: {player_data['rad_level']}\t{end_color}')

def input_player_attack(player_data: dict, enemy_data: dict, hit_status: str, adrenaline_damage: int) -> None:
    '''
    Выводит в консоль кол-во нанесенного урона, если игрок попал, после того, как игрок подтвердит удар.
    :param player_data: dict (данные о персонаже)
    :param enemy_data: dict (данные о противнике)
    :param hit: str (статус попадания игрока)
    :param adrenaline_damage: int (дополнительный урон при условии, что здоровье ниже 25 и есть перк "Адреналин")
    :return:
    '''

    print(line)
    input(f'{gr_color}[Для атаки нажмите ENTER] > {end_color}')
    play_sound('menu_click')

    if hit_status == 'hit':
        print(f'{gr_color}Вы нанесли {yl_color}{player_data['damage'] + player_data['bdamage'] + adrenaline_damage}'
              f'{gr_color} урона противнику {enemy_data['name']}\n')

        play_sound('player_hit')

    else:
        print(f'{yl_color}Вы промахнулись\n')

        play_sound('miss')

    input(f'{gr_color}[Для продолжения нажмите ENTER] > {end_color}')
    play_sound('menu_click_2')


def input_enemy_attack(player_data: dict, enemy_data: dict, hit_status: str, rad_hit: int) -> None:
    '''
    Выводит информацию о том сколько противник нанес урона броне или здоровью игрока, если он попал, после того
    как игрок подтвердит начало хода.
    :param player_data: dict (данные о персонаже)
    :param enemy_data: dict (данные о противнике)
    :param hit_status: str (статус попадания противника)
    :param rad_hit: int (единицы радиации, которые добавляются персонажу с ударами противника)
    :return:
    '''

    print(line)
    input(f'{gr_color}[Ход противника, нажмите ENTER] > {end_color}')
    play_sound('menu_click')

    if hit_status == 'hit':

        if player_data['armor'] != 0:
            print(f'{gr_color}{enemy_data['name']} нанес {yl_color}{enemy_data['damage']} {gr_color}урона вашей броне\n')

        else:

            if rad_hit > 0:
                print(f'{gr_color}{enemy_data['name']} нанес Вам {yl_color}{enemy_data['damage']} {gr_color}урона '
                      f'({yl_color}+{rad_hit}{gr_color} к ур. радиации)\n')
            else:
                print(f'{gr_color}{enemy_data['name']} нанес Вам {yl_color}{enemy_data['damage']} {gr_color}урона\n')

        play_sound('enemy_hit')

    else:
        print(f'{yl_color}Противник промахнулся\n')

        play_sound('miss')

    input(f'{gr_color}[Для продолжения нажмите ENTER] > {end_color}')
    play_sound('menu_click_2')

def print_item_taken(item_name: str) -> None:
    '''
    Выводит в консоль сообщение о том, что персонаж поднял предмет и его название (предмета).
    :param item_name: str (название предмета)
    :return:
    '''

    os.system('cls')

    gui_support.header('Предмет подобран')

    play_sound('result')
    print(f'{gr_color}Предмет {yl_color}{item_name}{gr_color} добавлен в инвентарь{end_color}')
    continue_button()

def print_radiation_sickness() -> None:
    '''
    Выводит в консоль сообщение о том, что персонаж потерял здоровье вследствие выского уровня радиации.
    :return:
    '''

    os.system('cls')

    gui_support.header('Лучевая болезнь')

    play_sound('result')
    print(f'{gr_color}Вас вырвало, теперь вы чувствуете легкую усталость.')
    print(f'{red_color}-20{end_color} {gr_color}к параметру Здоровье.')
    continue_button()

def print_dodged_by_charisma(dice: int, hostility: int) -> None:
    '''
    Выводит в консоль сообщение о том, что персонаж прошел проверку на харизму.
    :param dice: int (кол-во выпавшей харизмы)
    :param hostility: int (враждебность противника)
    :return:
    '''

    os.system('cls')

    gui_support.header('Успех')

    play_sound('result')
    print(f'{gr_color}Вы прошли проверку на харизму и избежали сражения.\n')
    print(f'{gr_color}Вы разыграли {yl_color}{dice}{gr_color} вашей харизмы против '
          f'{yl_color}{hostility} {gr_color}враждебности противника.')

    continue_button()

def input_loot_for_win_by_charisma(item_name: str) -> str:
    '''
    Принимает ответ от игрока, оставить ли себе предмет от противника.
    :param item_name: str (название предмета)
    :return: str (ответ да или нет)
    '''

    play_sound('result')

    while True:
        os.system('cls')

        gui_support.header('Вы избежали сражения')

        print(f'{gr_color}От противника вам достался случайный предмет {yl_color}{item_name}{gr_color}.\n'
              f'Вы хотите себе его оставить? {bl_color}(да/нет)')

        while True:
            print(line)
            answer = input(f'{gr_color}> {end_color}')

            if answer.lower() != 'да' and answer.lower() != 'нет':

                play_sound('error')
                continue

            else:

                play_sound('menu_click')
                break

        if answer.lower() in 'да':
            answer = 'yes'
        else:
            answer = 'no'

        return answer

def failed_charisma(dice: int, hostility: int) -> None:
    '''
    Выводит в консоль сообщщение о том, что игрок не прошел проверку на харизму.
    :param dice: int (кол-во выпавшей харизмы)
    :param hostility: int (враждебность противника)
    :return:
    '''

    os.system('cls')

    gui_support.header('Провал')

    play_sound('result')
    print(f'{gr_color}Вы провалили проверку на харизму. Приготовтесь к сражению.\n')
    print(f'{gr_color}Вы разыграли {yl_color}{dice}{gr_color} вашей харизмы против '
          f'{yl_color}{hostility} {gr_color}враждебности противника.')

    continue_button()

def input_item_for_use(player_data: dict) -> str:
    '''
    Принимает от игрока название предмета для использования.
    :param player_data: dict (данные персонажа)
    :return: str: название предмета или "вернуться"
    '''

    player_inventory = player_data['inventory']

    while True:
        item_name = input(f'{gr_color}Введите название предмета для его использования (либо "вернуться") > ')

        if item_name not in player_inventory and item_name.lower() != 'вернуться':

            play_sound('error')
            continue

        else:

            play_sound('menu_click')
            if item_name.lower() == 'вернуться':
                item_name = 'back'

            return item_name

def print_item_use_effect(item_name: str, effect: int,
                          item_data: dict, parameter_index=None) -> None:
    '''
    Выводит в консоль сообщение с эффектом от использованного предмета.
    :param item_name: str (название предмета)
    :param effect: int (эффект в числе)
    :param item_data: dict (данные о предмете)
    :param parameter_index: int (индекс параметра у предмета "капсула")
    :return:
    '''

    os.system('cls')

    gui_support.header('Вы использовали предмет')

    play_sound('stimpack')
    print(f'{gr_color}Название предмета: {item_name}\n'
          f'Тип: {item_data['type']}\n')

    if item_name != 'Капсула':
        print(f'{gr_color}Эффект: {item_data['eff_description']}')

        if item_data['add_eff_status'] == 'yes':
            print(f'{gr_color}Доп. эффект: {item_data['add_eff_description']}')

    else:
        print('У капсул эффект определяется случайно.')
        print(f'{gr_color}Эффект: {item_data['eff_parameter'][parameter_index]} {'+' if effect > 0 else ''}{effect}')

    continue_button()

    pass

def inventory_is_empty():
    '''
    Выводит в консоль сообщение о том, что инвентарь пуст.
    :return:
    '''

    play_sound('error')
    print(f'{gr_color}Ваш инвентарь пуст{end_color}')

def input_loot_choice_for_win(random_item_1: str, random_item_2:str) -> str:
    '''
    Принимает от игрока название или номер предмета который он хочет получить себе.
    :param random_item_1: str (название предмета)
    :param random_item_2: str (название предмета)
    :return: str (название предмета)
    '''

    try_count = 0
    play_sound('result')

    while True:
        os.system('cls')

        gui_support.header('Враг побежден')

        print(f'{gr_color}После убийства противника вы можете забрать его предмет.\n')
        print(f'{gr_color}Предметы определены случайно.\n')

        print('Введите название предмета, который Вы хотите взять: ')
        print(f'{bl_color}[1]{end_color} {yl_color}{random_item_1}')
        print(f'{bl_color}[2]{end_color} {yl_color}{random_item_2}')
        print(f'{bl_color}[3]{end_color} {gr_color}Ничего не брать')

        print(line)

        if try_count == 0:
            item_name = input(f'{gr_color}> {end_color}')
        else:
            item_name = input(f'{bl_color}(введите название предмета или его номер){end_color} {gr_color}> ')

        if (item_name != '1' and item_name != '2' and item_name != '3' and
               item_name.lower() != random_item_1.lower() and
               item_name.lower() != random_item_2.lower() and
               item_name.lower() != 'ничего не брать' and item_name.lower() != 'ничего'):

           try_count += 1

           play_sound('error')
           continue
        else:

            play_sound('menu_click')
            break


    if item_name.lower() in '3 ничего не брать':
        return None
    elif item_name.lower() in f'1 {random_item_1.lower()}'.lower():
        item_name = random_item_1
    elif item_name.lower() in f'2 {random_item_2.lower()}'.lower():
        item_name = random_item_2

    return item_name

def input_menu_choice(player_data: dict, char_name: str) -> str:
    '''
    Меню, принимающее от игрока ответ: продолжить/использовать предмет/выйти.
    :param player_data: dict (данные персонажа)
    :param char_name: str (имя персонажа)
    :return: str (ответ)
    '''

    try_count = 0

    if len(player_data['inventory']) == 0:
        inventory = 'пуст'
    else:
        inventory = ''

    while True:
        os.system('cls')

        gui_support.header('Вы продолжаете свой путь')

        print(f'{gr_color}{char_name}\t\t\t\t {yl_color}{player_data['road']}:{player_data['current_location'][0:-4]}')
        print(f'{gr_color}---------------')
        print(f'Происхождение: {player_data['genesis']}\t\t Перк: {player_data['perk']}')
        print(f'Здоровье: {player_data['hp']}\t\t\t Уровень радиации: {player_data['rad_level']}')
        print(f'Урон: {player_data['damage']}\t\t\t Доп. урон: {player_data['bdamage']}')
        print(f'Броня: {player_data['armor']}\t\t\t Харизма: {player_data['charisma']}')
        print(f'Меткость: {player_data['accuracy']}')
        print(f'Инвентарь: {yl_color}{inventory}', end='')

        for i in range(0, len(player_data['inventory']), 1):
            if i == 0:
                print(f'{player_data['inventory'][i]}', end='')
            else:
                print(f', {player_data['inventory'][i]}', end='')

        print()
        print()
        print(f'{bl_color}[1]{gr_color} Продолжить путь')
        print(f'{bl_color}[2]{gr_color} Использовать предмет')
        print(f'{bl_color}[3]{gr_color} Выйти (прогресс локации не сохранится)')
        print(f'{bl_color}[4]{gr_color} Сохранить статистику (в текстовом файле)')

        print(line)

        if try_count == 0:
            menu_choice = input('> ')
        else:
            menu_choice = input(f'{bl_color}(введите команду или ее номер) {gr_color}> ')

        if (menu_choice != '1' and menu_choice != '2' and menu_choice != '3' and menu_choice != '4' and
            menu_choice.lower() != 'продолжить путь' and
            menu_choice.lower() != 'использовать предмет' and
            menu_choice.lower() != 'выйти' and
            menu_choice.lower() != 'сохранить статистику'):

            try_count += 1

            play_sound('error')
            continue
        else:
            play_sound('menu_click')

            if menu_choice.lower() in '1 продолжить путь':
                return 'go'
            elif menu_choice.lower() in '2 использовать предмет':
                return 'use_item'
            elif menu_choice.lower() in '3 выйти':
                return 'exit'
            else:
                return 'save txt'

def print_stats_txt_saved():
    '''
    Сообщение о том, что статистика сохранена в txt файле.
    :return:
    '''

    play_sound('result')
    print(f'{gr_color}Статистика успешно сохранена в папке "characters".\n')

    input(f'[Нажмите ENTER] >{end_color}')
    play_sound('menu_click_2')

def input_death_menu_choice() -> str:
    '''
    Меню, возникающее у игрока после смерти персонажа. Принимает ответ: начать снова/вернуться/выйти.
    :return: str (ответ)
    '''

    try_count = 0
    death_text = gui_support.get_death_text()
    play_sound('death')

    while True:
        os.system('cls')

        gui_support.header('Вы погибли')

        print(death_text)
        print()

        print(f'{bl_color}[1]{gr_color} {gr_color}Начать прохождение снова')
        print(f'{bl_color}[1]{gr_color} {gr_color}Вернуться в главное меню')
        print(f'{bl_color}[1]{gr_color} {gr_color}Выйти')

        if try_count == 0:
            menu_choice = input(f'{gr_color}> ')
        else:
            menu_choice = input(f'{bl_color}(введите команду или ее номер) {gr_color}>')

        if (menu_choice != '1' and menu_choice != '2' and menu_choice != '3' and
               menu_choice.lower() != 'начать прохождение снова' and
               menu_choice.lower() != 'вернуться в главное меню' and
               menu_choice.lower() != 'вернуться в меню' and
               menu_choice.lower() != 'выйти'):

            try_count += 1

            play_sound('error')
            continue
        else:

            play_sound('menu_click_2')

            if menu_choice.lower() in '1 начать прохождение снова':
                return 'again'
            elif menu_choice.lower() in '2 вернуться в главное меню':
                return 'to_main_menu'
            elif menu_choice.lower() in '3 выйти':
                return 'exit'

def play_sound(sound_name: str) -> None:
    '''
    Проигрывание звука
    :param sound_name: str (название звука)
    :return:
    '''
    winsound.PlaySound(f'sounds/{sound_name}.wav', winsound.SND_ASYNC)
