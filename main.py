import telebot
from config import API, password, programmist
from data_base import conn, cur
from button import *


bot = telebot.TeleBot(API)

@bot.message_handler(commands=['start'])
def hi(message):
    global user_name
    user_name = message.from_user.first_name

    bot.send_message(message.chat.id, 'Привет, ' + user_name + '! Давайте знакомиться! Скажите, кто вы:', reply_markup=button_start())


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
        mess = bot.send_message(id, 'Пожалуйста, введите пароль:')
        bot.register_next_step_handler(mess, parols)


    if message.text == 'Подписаться на рассылку':
        markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Получить последнюю новость')
        markup1.add(btn1)
        try:
            cur.execute("UPDATE users5 set reply = ? where userid = ?", ('on', id))
            conn.commit()
            bot.send_message(id, 'Вы успешно подписались на рассылку', reply_markup=button_reply_off())
        except:
            bot.send_message(id, 'Вы уже подписаны на рассылку или возникла ошибка')

    if message.text == 'Отписаться от рассылки':
        try:
            cur.execute("UPDATE users5 set reply = ? where userid = ?", ('off', id))
            conn.commit()
            bot.send_message(id, ' Вы успешно отписались от рассылки', reply_markup=button_reply_off())
        except:
            bot.send_message(id, 'Возникла ошибка при отписке')


    if message.text == 'Получить последнюю новость':
        pass


    if message.text == 'Отправить новость' and id == teacher_id:
        reply_message = bot.send_message(id, 'Пожалуйста, напишите новость одним сообщением')
        bot.register_next_step_handler(reply_message, reply)



def student():
    bot.send_message(id, 'Добро пожаловать!', reply_markup=button_reply_on())
    mes = bot.send_message(id, 'Пожалуйста, скажи: в каком ты классе. Например, <<5А>>')
    bot.register_next_step_handler(mes, class_st)
    user = (id, 'student', 'off', user_name)

def guest():
    bot.send_message(id, 'Добро пожаловать в самую лучшую школу на свете!', reply_markup=button_reply_on())
    user = (id, 'guest', 'off', user_name, 'none')
    insert_base(user)

def parent():
    bot.send_message(id, 'Добро пожаловать!', reply_markup=button_reply_on())
    mes = bot.send_message(id, 'Пожалуйста, скажите: в каком классе обучается Ваш ребёнок. Например, <<5А>>')
    bot.register_next_step_handler(mes, class_st)
    user = (id, 'parent', 'off', user_name)

def class_st(message, user):
    class_student = message
    user = user + class_student
    print(user)





def parols(message):

        if message.text == password:
            bot.send_message(message.chat.id, 'Поздравляю! Вы успешно вошли в аккаунт')
            mess = bot.send_message(id, 'Пожалуйста, представьтесь')
            bot.register_next_step_handler(mess, name_teacher)
        else:
            bot.send_message(id, 'Пароль неверный. Повторите попытку')
            mess = bot.send_message(message.chat.id, 'Пожалуйста, введите пароль:')
            bot.register_next_step_handler(mess, parols)





def name_teacher(message):
    name_teach = message
    user = (id, name_teach)
    insert_base_teacher(user)





def insert_base_teacher(user):
    cur.execute("INSERT OR IGNORE INTO admin VALUES(?, ?);", user)
    conn.commit()
    administrator()

def insert_base(user):

    cur.execute("INSERT OR IGNORE INTO users5(userid, status, reply, user_name, class) VALUES(?, ?, ?, ?, ?);", user)
    conn.commit()





def administrator():
    global teacher_id
    teacher_id = id
    bot.send_message(id, 'Выберете действие:', reply_markup=button_admin_start())



def reply(message):
    sqlite_select_query = """SELECT userid, status, user_name, reply, class from users5 """
    cur.execute(sqlite_select_query)
    data = cur.fetchall()
    conn.commit()
    news = message.text
    for replys in data:
        print(replys)
        if replys[2] == 'on':
            bot.send_message(replys[0], f'Привет, {replys[1]}. Доступна новая новость')
            bot.send_message(replys[0], news)


@bot.message_handler(commands=['stop'])
def stop_bot():
    bot.send_message(id, hi())

bot.infinity_polling()

