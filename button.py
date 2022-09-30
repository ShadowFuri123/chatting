from telebot import types

def button_start():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Гость')
    btn2 = types.KeyboardButton('Ученик')
    btn3 = types.KeyboardButton('Учитель')
    btn4 = types.KeyboardButton('Родитель')

    markup.add(btn1, btn2, btn3, btn4)
    return markup


def button_reply_on():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Подписаться на рассылку')
    markup.add(btn1)
    return markup

def button_reply_off():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Отписаться от рассылки')
    markup.add(btn1)
    return markup


def button_admin_start():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Отправить новость')
    markup.add(btn1)
    return markup