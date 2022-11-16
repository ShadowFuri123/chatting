from telebot import types

def button_start():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Гость')
    btn2 = types.KeyboardButton('Ученик')
    btn3 = types.KeyboardButton('Учитель')
    btn4 = types.KeyboardButton('Родитель')

    markup.add(btn1, btn2, btn3, btn4)
    return markup


def button_main():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Подписаться на рассылку')
    btn2 = types.KeyboardButton('Узнать расписание')
    markup.add(btn1, btn2)
    return markup

def button_reply_off():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Отписаться от рассылки')
    markup.add(btn1)
    return markup


def button_admin_start():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Отправить новость')
    btn2 = types.KeyboardButton('Изменить расписание')
    markup.add(btn1, btn2)
    return markup

def button_return():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Назад')
    markup.add(btn1)
    return markup

def who_reply():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Гостям школы')
    btn2 = types.KeyboardButton('Ученикам')
    btn3 = types.KeyboardButton('Учителям')
    btn4 = types.KeyboardButton('Родителям')
    btn5 = types.KeyboardButton('Всем...')
    btn6 = types.KeyboardButton('Назад')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
    return markup

def who_all():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Гостям школы')
    btn2 = types.KeyboardButton('Ученикам')
    btn3 = types.KeyboardButton('Учителям')
    btn4 = types.KeyboardButton('Родителям')
    btn5 = types.KeyboardButton('Всем')
    btn6 = types.KeyboardButton('Назад')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
    return markup