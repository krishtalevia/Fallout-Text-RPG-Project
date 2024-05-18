gr_color = '\033[0;32m'
bl_color = '\033[0;34m'
end_color = '\033[0m'
import random

def main_menu_header_ascii() -> None:
    '''
    Шапка для главного меню.
    :return:
    '''
    print(rf"""
                {gr_color}     ______      ____  {bl_color}/{end_color}{gr_color}          __ 
                {gr_color}    / ____/___ _/ / /_{bl_color}//{end_color}{gr_color}   __  __/ /_
                {gr_color}   / /_  / __ `/ / / {bl_color}//{end_color}{gr_color}\ / / / / __/
                {gr_color}  / __/ / /_/ / / / {bl_color}/-/{end_color}{gr_color} / /_/ / /_  
                {gr_color} /_/    \____/_/_/\_{bl_color}//{end_color}{gr_color}_/\____/\__/  
                                    {bl_color}/{end_color}""")

def header(text: str) -> None:
    '''
    Заголовок для "слайдов".
    :param text: текст заголовка
    :return:
    '''
    print(f'{gr_color}|--------------------------------------------------------------------|')
    print(f'> {text}')
    print(f'|--------------------------------------------------------------------|{end_color}')

def get_death_text() -> None:
    '''
    В случае смерти игрока берется случайное описание его смерти.
    :return:
    '''
    dice = random.randint(1,5)

    if dice == 1:
        death_text = f'{gr_color}Ваш облучённый труп не заинтересовал даже стервятников.'
    elif dice == 2:
        death_text = f'{gr_color}Ваши кости отполировал ветер пустыни.'
    elif dice == 3:
        death_text = (f'{gr_color}Пустошь взяла своё.\n'
                      'Вы умирали долго, в страшных мучениях.\n'
                      'Ваше приключение закончено.')
    elif dice == 4:
        death_text = (f'{gr_color}Темнота загробного мира ожидает вас. Возможно, там вы найдёте покой,\n'
                      'который так и не нашли здесь…')
    elif dice == 5:
        death_text = (f'{gr_color}Пустошь берет своё. Ваша смерть была медленной и исключительно\n'
                      'болезненной. Ваше приключение завершилось.')

    return death_text

def combat_header_ascii() -> None:
    '''
    Шапка для "слайда" со сражением.
    :return:
    '''
    print(f'''{gr_color}
     ,______________________________________       
    |_________________,----------._ [____]  ""-,__  __....-----=====
                   (_(||||||||||||)___________/   ""                |
                      `----------' //////[ ))"-,                   |
                                           ""    `,  _,--....___    |
                                                   `/           """" {end_color}''')


    