from db import Database
import keyboard
from aiogram import Bot, Dispatcher, executor, types
db = Database()
print(f'Привет, я помогу изучать тебе иностранные слова! \n'
      'Меню: \n'
      '[1] - Вывести весь справочник\n'
      '[2] - Включить режим ввода слов\n' 
      '[3] - Найти слово в базе\n'
      '[4] - Вывести определенное количество слов\n'
      '[5] - Вывести количество слов в базе\n'
      '[ESC] - Выйти'
      )

def menu_select():
    select = input()
    if select == '1':
        show_all()
    elif select == '2':
        add_word()
    elif select == '3':
        get_word()
    elif select == '4':
        get_limit_words()
    elif select == '5':
        get_count()
    else:
        if keyboard.is_pressed('esc'):
            exit()

def show_all():
    for item in db.show_all():
        print(' - '.join(map(str, item)))

def add_word():
    word = input('Введите слово:  ')
    translate = input('Введите перевод: ')
    if (not db.word_exists(word, translate)):
        db.add_word(word, translate)
        print(f'Вы ввели: {word}, перевод: {translate}. Значения добавлены в справочник. Нажмите [2] для повторного ввода')
    else:
        print('Такое слово уже есть в базе, попробуй другое! Нажмите [2] для повторного ввода')

def get_word():
    while True:
        get_word = input()
        if db.get_word(get_word) is None or get_word is not int:
            print('Такого слова в базе нет! Нажмите [3] для повторного ввода')
            break
        else:
            print('Резуьтат: ', ' - '.join(db.get_word(get_word)))


def get_limit_words():
    try:
        limit = input('Введите количество последних записей для вывода:  ')
        for item in db.get_last_words(limit):
            print(' - '.join(map(str, item)))
    except (Exception) as error:
        print('Видимо, что то пошло не так, попробуй указать другой лимит для вывода..\n', '[INFO] -', error)

def get_count():
        print('Всего слов в базе: ', ''.join(map(str, db.get_count())))

while True:
    menu_select()
