import telebot
from config import API, password, programmist
from data_base import cur, conn
from button import *
from insert_data_base import *

bot = telebot.TeleBot(API)
global to_whom


@bot.message_handler(commands=['start'])
def hi(message):
    global user_name
    user_name = message.from_user.first_name

    bot.send_message(message.chat.id, 'Здравствуйте, ' + user_name + '! Давайте знакомиться! Скажите, кто Вы:', reply_markup=button_start())

def return_to_who_are_you():
    bot.send_message(id, 'Скажите, кто Вы:', reply_markup=button_start())


@bot.message_handler(content_types=['text'])
def who_are_you(message):
    global id
    id = message.chat.id


    if message.text == 'Ученик':
        student()

    if message.text == 'Гость':
        guest()

    if message.text == 'Родитель':
        parent()

    if message.text == 'Учитель':
        mess = bot.send_message(id, 'Пожалуйста, введите пароль:', reply_markup=button_return())
        bot.register_next_step_handler(mess, parols)


    if message.text == 'Подписаться на рассылку':
        markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Получить последнюю новость')
        markup1.add(btn1)
        try:
            cur.execute("UPDATE user set reply = ? where userid = ?", ('on', id))
            conn.commit()
            bot.send_message(id, 'Вы успешно подписались на рассылку', reply_markup=button_reply_off())
        except:
            bot.send_message(id, 'Вы уже подписаны на рассылку или возникла ошибка')

    if message.text == 'Отписаться от рассылки':
        try:
            cur.execute("UPDATE user set reply = ? where userid = ?", ('off', id))
            conn.commit()
            bot.send_message(id, ' Вы успешно отписались от рассылки', reply_markup=button_reply_off())
        except:
            bot.send_message(id, 'Возникла ошибка при отписке')


    if message.text == 'Назад' :
        main_window()

    if message.text == 'Отправить новость' and id == teacher_id:
        to_whom_send_news()


    if message.text == 'Ученикам' and id == teacher_id:
        mess = bot.send_message(id, 'Ученикам какого класса вы хотите написать? Пожалуйста, пишите номер и букву класса слитно')
        bot.register_next_step_handler(mess, clas)


    if message.text == 'Родителям' and id == teacher_id:
        mess = bot.send_message(id, 'Родителям учеников какого класса вы хотите написать? Пожалуйста, пишите номер и букву класса слитно')
        bot.register_next_step_handler(mess, clas_p)

    if message.text == 'Гостям школы' and id == teacher_id:
        to_whom = ('Гостям школы', 'none')
        send_news(to_whom)

    if message.text == 'Учителям' and id == teacher_id:
        to_whom =('Учителям', 'none')
        send_news(to_whom)


def student():
    bot.send_message(id, 'Добро пожаловать!')
    mes = bot.send_message(id, 'Пожалуйста, скажи: в каком ты классе. Например, <<5А>>')
    bot.register_next_step_handler(mes, class_st)

def guest():
    bot.send_message(id, 'Добро пожаловать в самую лучшую школу на свете!', reply_markup=button_reply_on())
    user = (id, 'guest', 'off', user_name, 'none')
    insert_base(user)

def parent():
    bot.send_message(id, 'Добро пожаловать!')
    mes = bot.send_message(id, 'Пожалуйста, скажите: в каком классе обучается Ваш ребёнок. Например, <<5А>>')
    bot.register_next_step_handler(mes, class_st)


def class_st(message):
    class_student = message.text
    user = (id, 'student', 'off', user_name, class_student)
    insert_base(user)


def class_parent(message):
    class_student = message.text
    user = (id, 'parent', 'off', user_name, class_student)
    insert_base(user)

def insert_base(user):
    cur.execute("INSERT OR IGNORE INTO user(userid, status, reply, user_name, clas) VALUES(?, ?, ?, ?, ?);", user)
    conn.commit()
    bot.send_message(id, 'Спасибо! Желаете ли Вы подписаться на рассылку?', reply_markup=button_reply_on())

def main_window():
    bot.send_message(id, 'Выберите действие:', reply_markup=button_reply_on())


def parols(message):

        if message.text == password and message.text != 'Назад':
            bot.send_message(message.chat.id, 'Поздравляю! Вы успешно вошли в аккаунт')
            administrator()
        elif message.text == 'Назад':
            return_to_who_are_you()
        else:
            bot.send_message(id, 'Пароль неверный. Повторите попытку')
            mess = bot.send_message(message.chat.id, 'Пожалуйста, введите пароль:')
            bot.register_next_step_handler(mess, parols)



def administrator():
    global teacher_id
    teacher_id = id
    bot.send_message(id, 'Выберете действие:', reply_markup=button_admin_start())
    user = (id, 'teacher', 'off', user_name, 'none')


def to_whom_send_news():
    bot.send_message(id, 'Выберете, кому Вы хотите отправить новость:', reply_markup=who_reply())

def clas(message):
    classer = message.text
    to_whom = ('student', classer)
    send_news(to_whom)

def clas_p(message):
    classer = message.text
    to_whom = ('parent', classer)
    send_news(to_whom)


def send_news(to_whom):
    reply_message = bot.send_message(id, 'Пожалуйста, напишите новость одним сообщением')
    bot.register_next_step_handler(reply_message, reply, to_whom)



def reply(message, to_whom):
    sqlite_select_query = """SELECT userid, status, user_name, reply, clas from user """
    cur.execute(sqlite_select_query)
    data = cur.fetchall()
    conn.commit()
    news = message.text
    for replys in data:
        if replys[3] == 'on':
            if to_whom[0] == replys[1] and to_whom[1] == replys[4]:
                print(news)
                bot.send_message(replys[0], f'Здравствуйте, {replys[2]}. Доступна новая новость')
                bot.send_message(replys[0], news)

@bot.message_handler(commands=['stop'])
def stop_bot():
    bot.send_message(id, hi())

bot.infinity_polling()

