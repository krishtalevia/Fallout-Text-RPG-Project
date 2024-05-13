import gui_headers
import os

gr_color = '\033[0;32m'
bl_color = '\033[0;34m'
red_color = '\033[0;31m'
yl_color = '\033[0;33m'
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

        gui_headers.header(header_text)

        print(f'{bl_color}[1]{end_color} {gr_color}Вернуться{end_color}')

        print(line)

        if try_count == 0:
            answer = input(f'{gr_color}> {end_color}')
        else:
            answer = input(f'{bl_color}(введите команду или ее номер) {gr_color}> {end_color}')

        if answer not in '1 вернуться':

            try_count += 1

            continue

        else:
            break

def input_roleplay_genesis() -> str:
    try_count = 0

    while True:
        os.system('cls')

        gui_headers.header('Ваше происхождение?')

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

        gui_headers.header('Человек:')

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

        gui_headers.header('Гуль')

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
        print(f'{gr_color}*Изыскатель: Способность находить ценные вещи среди кучи')
        print('мусора способствуют его выживанию в этом опасном мире.')
        print(f'Перк: {bl_color}Изыскатель{end_color}')
        print()

    elif genesis == 'Супермутант':
        os.system('cls')

        gui_headers.header('Супермутант')

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
        print(f'{gr_color}*Странник: способность адаптироваться к любым условиям')
        print('позволяет ему выживать в самых экстремальных ситуациях.')
        print(f'Перк: {bl_color}Адаптивность{end_color}')
        print()

    print(f'{gr_color}Вы выбираете данное происхождение?{end_color} {bl_color}(да/нет){end_color}')

    print(line)

    while True:
        answer = input(f'{gr_color}> {end_color}')

        if answer.lower() != 'да' and answer.lower() != 'нет':
            continue

        else:
            break

    if answer.lower() in 'да':
        answer = 'yes'
    else:
        answer = 'no'

    return answer

def input_roleplay_role(genesis: str) -> str:
    try_count = 0

    while True:
        os.system('cls')

        gui_headers.header('Ваша профессия?')

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

                continue

            else:

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

                continue

            else:

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

                continue

            else:

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

def role_info(genesis, role) -> str:
    if genesis == 'Человек' and role == 'Караванщик':
        os.system('cls')

        gui_headers.header('Караванщик:')

        print(f'{gr_color}Зарабатывает на жизнь, перевозя редкие ресурсы и товары')
        print('между поселениями.')
        print()
        print(f'Перк "Переговорщик": Харизма {bl_color}+10%{end_color}')

    elif role == 'Рейдер':
        os.system('cls')

        gui_headers.header('Гуль')

        print(f'{gr_color}Зарабатывает на жизнь грабя неосторожных путешественников')
        print('и терроризируя поселения.')
        print()
        print(f'Перк "Адреналин": {bl_color}+15{end_color}{gr_color} к доп. урону, если здоровье падает ниже 25')

    elif role == 'Караванщик':
        os.system('cls')

        gui_headers.header('Караванщик')

        print(f'{gr_color}Зарабатывает на жизнь, перевозя редкие ресурсы и товары')
        print('между поселениями.')
        print()
        print(f'Перк "Торговец": Харизма {bl_color}+20%{end_color}{gr_color}')

    elif role == 'Старатель':
        os.system('cls')

        gui_headers.header('Старатель')

        print(f'{gr_color}Старатели зарабатывают себе на жизнь находя в заброшенных')
        print('местах ценные вещи, для последующей их продажи.')
        print()
        print(f'Перк "Изыскатель": {bl_color}30%{end_color}{gr_color} найти дополнительный предмет')

    elif role == 'Тень':
        os.system('cls')

        gui_headers.header('Тень')

        print(f'{gr_color}После смерти Создателя, наиболее мирные из Теней стали зарабатывать')
        print('работая наемниками, обладая особыми навыками и экипировкой.')
        print()
        print(f'Перк "Элита": {bl_color}+15{end_color}{gr_color} брони')

    elif role == 'Странник':
        os.system('cls')

        gui_headers.header('Странник')

        print(f'{gr_color}После смерти Создателя, многие Супермутанты растворились в пустоши,')
        print('находя в различной деятельности, где нужна сила и выносливость.')
        print()
        print(f'Перк "Адаптивность": {bl_color}30%{end_color}{gr_color} сопротивления к отнимающим здоровье')
        print('предметам или ловушкам')

    print(f'{gr_color}Вы выбираете данную профессию?{end_color} {bl_color}(да/нет){end_color}')

    print(line)

    while True:
        answer = input(f'{gr_color}> {end_color}')

        if answer.lower() != 'да' and answer.lower() != 'нет':
            continue

        else:
            break

    if answer.lower() in 'да':
        answer = 'yes'
    else:
        answer = 'no'

    return answer

def print_start_game_exposition(char_name: str, perk: str, role: str) -> None:
    os.system('cls')

    gui_headers.header('Описание')

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

    elif perk == 'Изыскатель':
        print(f'{intro} добывая \n'
              f'ценные ресурсы из облученной земли.')

    elif perk == 'Элита':
        print(f'{intro} подрабатывая \n'
              f'наемником, используя свою силу и выносливость.')

    elif perk == 'Адаптивность':
        print(f'{intro} благодаря \n'
              f'своей силе и выносливости.')

def continue_button() -> None:
    print(line)
    input(f'{gr_color}[Нажмите ENTER] > {end_color}')

def input_stats_or_go():
    try_count = 0

    while True:
        os.system('cls')

        gui_headers.header('Подготовка')

        print(f'{gr_color}Вам предстоит отправиться в дальний путь, с целью выполнить\n'
              f'свои обязанности. Будь то перевозка товаров между поселениями,\n'
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

            continue

        else:
            break

    if answer.lower() in '1 информация о персонаже':
        answer = 'stats'
    else:
        answer = 'go'

    return answer

def print_stats(stats, char_name):
    os.system('cls')

    gui_headers.header('Информация о персонаже')

    print(f'{gr_color}Имя: {char_name}\t\t\t Происхождение: {stats['genesis']}')
    print(f'Здоровье: {stats['hp']}\t\t Перк: {stats['perk']}')
    print(f'Броня: {stats['armor']}\t\t Инвентарь: {stats['inventory'] if len(stats['inventory']) > 0 else 'пуст'}')
    print(f'Урон: {stats['damage']}\t\t Доп. урон: {stats['bdamage']}')
    print(f'Уровень радиации: {stats['rad_level']}')

def input_choosing_road(roads_list):
    try_count = 0

    while True:
        os.system('cls')

        gui_headers.header('Выбор маршрута')

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

            continue
        else:

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

def road_info(road_name):
    if road_name == 'Могильник':
        os.system('cls')

        gui_headers.header('Могильник:')

        print(f'{gr_color}После начала ядерной войны подавляющее большинство\n'
              'населения Лос-Анджелеса погибло от радиации, голода,\n'
              'болезней и вследствие иных причин. Их кости десятилетия\n'
              'спустя остались лежать в зданиях и на улицах, придавая\n'
              'этому месту облик кладбища.\n')

        print('По направлению к этому месту предстоит ваш путь.\n')

        print(f'{gr_color}Сложность: {end_color}Легко')

    elif road_name == 'Некрополь':
        os.system('cls')

        gui_headers.header('Некрополь:')

        print(f'{gr_color}Слава о ходячих мертвецах из Мёртвого города широко известна\n'
              'в Пустошах Калифорнии. Путешественники и торговцы стараются\n'
              'обходить город стороной.\n')

        print('По направлению к этому месту предстоит ваш путь.\n')

        print(f'{gr_color}Сложность: {yl_color}Средняя{end_color}')

    elif road_name == 'Свечение':
        os.system('cls')

        gui_headers.header('Свечение:')

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
            continue

        else:
            break

    if answer.lower() in 'да':
        answer = 'yes'
    else:
        answer = 'no'

    return answer

def input_choice(choice_text_1, choice_text_2, choice_text_3=None):

    print(line)
    print(f'{bl_color}[1]{end_color} {gr_color}{choice_text_1}{end_color}')
    print(f'{bl_color}[2]{end_color} {gr_color}{choice_text_2}{end_color}')

    if choice_text_3 != None:
        print(f'{bl_color}[3]{end_color} {gr_color}{choice_text_3}{end_color}')

    choice = input(f'{gr_color}> {end_color}')

    while True:
        if choice == '3' and choice_text_3 == None:
            choice = input(f'{bl_color}(введите команду или ее номер) {gr_color}> {end_color}')
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

        return choice

def print_enemy_info(current_enemy_data: dict, event_text):
    os.system('cls')

    gui_headers.header('Событие: Враг')

    print(f'{gr_color}{event_text}\n')

    print(f'Описание:')
    print('----------------')
    print(f'{gr_color}Имя: {current_enemy_data['name']}\t Тип: {current_enemy_data['type']}\n'
          f'Описание: {current_enemy_data['description']}{end_color}')

def print_treasure_info(event_text):
    os.system('cls')

    gui_headers.header('Событие: Предмет')

    print(f'{gr_color}{event_text}\n')

def print_state_of_combat(char_name, player_data, enemy_data):
    os.system('cls')

    gui_headers.header('Сражение')

    print()
    print(f'{gr_color}{char_name}\t\t\t\t\t{enemy_data['name']}')
    print('--------------------\t\t\t--------------------')
    print(f'Здоровье: {player_data['hp']}\t\t\t\tЗдоровье: {enemy_data['hp']}')
    print(f'Броня: {player_data['armor']}\t\t\t\tУрон: {enemy_data['damage']}')
    print(f'Урон: {player_data['damage']}\t\t\t\tРадиация: {enemy_data['is_rad']}')
    print(f'Доп. урон: {player_data['bdamage']}\t')
    print(f'Уровень рад.: {player_data['rad_level']}\t{end_color}')

def input_player_attack():
    print(line)
    input(f'{gr_color}[Для атаки нажмите ENTER] >{end_color}')

def print_enemy_attack():
    print(line)
    input(f'{gr_color}[Ход противника, нажмите ENTER] >{end_color}')

def print_item_taken(item_name):
    os.system('cls')

    gui_headers.header('Предмет подобран')

    print(f'{gr_color}Предмет {item_name} добавлен в инвентарь{end_color}')
    continue_button()

def print_dodged_by_charisma():
    os.system('cls')

    gui_headers.header('Успех')

    print(f'{gr_color}Вы прошли проверку на харизму и избежали сражения.')
    continue_button()

def input_loot_for_win_by_charisma(item_name):
    try_count = 0

    while True:
        os.system('cls')

        gui_headers.header('Вы избежали сражеия')

        print(f'{gr_color}От противника вам достался предмет {yl_color}{item_name}{gr_color},\n'
              f'вы хотите себе его оставить? {bl_color}(да/нет)\n')

        while True:
            answer = input(f'{gr_color}> {end_color}')

            if answer.lower() != 'да' and answer.lower() != 'нет':
                continue

            else:
                break

        if answer.lower() in 'да':
            answer = 'yes'
        else:
            answer = 'no'

        return answer

def failed_charisma():
    os.system('cls')

    gui_headers.header('Провал')

    print(f'{gr_color}Вы провалили проверку на харизму. Приготовтесь к сражению.')
    continue_button()

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

def input_loot_choice_for_win(enemy_data):
    try_count = 0

    while True:
        os.system('cls')

        gui_headers.header('Враг побежден')

        print(f'{gr_color}После убийства противника вы можете забрать его предметы.\n')

        print('Введите название предмета, который Вы хотите взять: ')
        print(f'{bl_color}[1]{end_color} {gr_color}{enemy_data['loot'][0]}')
        print(f'{bl_color}[2]{end_color} {gr_color}{enemy_data['loot'][1]}')
        print(f'{bl_color}[3]{end_color} {gr_color}Ничего не брать\n')

        print(line)

        if try_count == 0:
            item_name = input(f'{gr_color}> {end_color}')
        else:
            item_name = input(f'{bl_color}(введите название предмета или его номер){end_color} {gr_color}> ')

        if (item_name != '1' and item_name != '2' and item_name != '3' and
               item_name.lower() != enemy_data['loot'][0].lower() and
               item_name.lower() != enemy_data['loot'][1].lower() and
               item_name.lower() != 'ничего не брать' and item_name.lower() != 'ничего'):

           try_count += 1

           continue
        else:
            break


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