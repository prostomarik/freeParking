import telebot
# from telebot import apihelper
import hack_config
import json
import traceback
import hack_user_database
import hack_dvor_database
import requests
import time
import cv2

bot = telebot.TeleBot(hack_config.TOKEN)

hack_dvor_database.create_table_users()
hack_dvor_database.create_new_camera(1, "ulica pushkina dom kolotushkina", {'lol': 'kek'})
hack_user_database.create_table_users()


def showImage(good, bad):  # список по 4 координаты свободных и занятых мест, формат : [x1, y1, x2, y2]
    image = cv2.imread('bot.jpg')

    for tmp in good:
        image = cv2.rectangle(image, (tmp[0], tmp[1]), (tmp[2], tmp[3]), (0, 255, 0), 2)
    for tmp in bad:
        image = cv2.rectangle(image, (tmp[0], tmp[1]), (tmp[2], tmp[3]), (0, 0, 255), 2)
    # cv2.imshow('a', image)
    #
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    return image


def update(link):
    r = requests.get(link).text
    return r

def load_exchange(URL):
    return requests.get(URL).text

URL0 = 'http://8851ee31.ngrok.io/0'
URL1 = 'http://8851ee31.ngrok.io/1'

@bot.message_handler(commands=['start'])
def start_command(message):
    hack_user_database.create_table_users()
    hack_user_database.create_new_user(message.from_user.id)
    print("--"+str( hack_user_database.getinfo(message.from_user.id)))
    bot.send_message(
        message.chat.id,
        'Greetings! I can show you free space for parking.\n' +
        'To get this information use /getinfo.\n' +
        'To get help press /help.'
    )


@bot.message_handler(commands=['getinfo'])
def exchange_command(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton('where is camera', callback_data='one'),
        telebot.types.InlineKeyboardButton('update and photo', callback_data='new')
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton('add camera', callback_data='add_camera'),
        telebot.types.InlineKeyboardButton('count free spaces', callback_data='count')
    )
    bot.send_message(
        message.chat.id,
        'Click on the currency of choice:',
        reply_markup=keyboard
    )


@bot.callback_query_handler(func=lambda call: True)
def iq_callback(query):
    data = query.data
    if data.startswith('one'): # 1
        give_one_info(query)
    if data.startswith('new'): # 2
        new_info(query)
    if data.startswith('add_camera'): # 3
        add_camera(query)
    if data.startswith('count'): # 4
        count(query)


def count(query): # 4.1
    bot.answer_callback_query(query.id)
    user_id = query.from_user.id
    print(hack_user_database.getinfo(user_id),user_id)
    ask_user_for_chosing2(query.message, user_id)


def ask_user_for_chosing2(message,user_id): # 4.2
    bot.send_chat_action(message.chat.id, 'typing')
    ids = hack_user_database.getinfo(user_id)
    msg = bot.reply_to(message, 'choose camera id from:\n'+str(ids))
    bot.register_next_step_handler(msg, update_and_send_count)


def update_and_send_count(message): # 4.3
    x = message.text.split('\n')
    print(x)
    if len(x) == 1 and is_number(x[0]): # correct input?
        if hack_user_database.getinfo(message.from_user.id) != None:
            bad = json.loads(load_exchange(URL0))["bisy_places"]
            time.sleep(5)
            good = json.loads(load_exchange(URL1))["free_places"]
            rez=[bad, good]
            print(rez)
            hack_dvor_database.update_latest(x[0], rez)
            #bot.send_message(message.chat.id, 'some information about dvor'+str(x[0]) + str(hack_dvor_database.getinfo(x[0])[0]))
            bot.send_message(message.chat.id, len(rez[1]))
        else:
           msg = bot.reply_to(message, 'no such camera id \n try another one')
           bot.register_next_step_handler(msg, update_and_send_info_one_dvor)
    else:
        bot.send_chat_action(message.chat.id, 'typing')
        msg = bot.reply_to(message, 'incorrect input \n you shoud write smth like this:')
        bot.send_message(message.chat.id, '123')
        bot.register_next_step_handler(msg, update_and_send_info_one_dvor)


def new_info(query): # 2.1
    bot.answer_callback_query(query.id)
    user_id = query.from_user.id
    print(hack_user_database.getinfo(user_id),user_id)
    ask_user_for_chosing(query.message, user_id)


def ask_user_for_chosing(message,user_id): # 2.2
    bot.send_chat_action(message.chat.id, 'typing')
    ids = hack_user_database.getinfo(user_id)
    msg = bot.reply_to(message, 'choose camera id from:\n'+str(ids))
    bot.register_next_step_handler(msg, update_and_send_info_one_dvor)


def update_and_send_info_one_dvor(message): # 2.3
    x = message.text.split('\n')
    print(x)
    # print(message)
    if len(x) == 1 and is_number(x[0]): # correct input?
        if hack_user_database.getinfo(message.from_user.id) != None:
            # bad = update('http://7f4f2621.ngrok.io/0')
            # time.sleep(5)
            # good = update('http://7f4f2621.ngrok.io/0')
            bad = json.loads(load_exchange(URL0))["bisy_places"]
            time.sleep(5)
            good = json.loads(load_exchange(URL1))["free_places"]
            rez=[bad, good]
            print(rez)
            hack_dvor_database.update_latest(x[0], rez)
            #bot.send_message(message.chat.id, 'some information about dvor'+str(x[0]) + str(hack_dvor_database.getinfo(x[0])[0]))
            myimage = showImage(good, bad)
            cv2.imwrite("map.jpg", myimage)
            foto = open('./map.jpg', 'rb')
            bot.send_photo(message.chat.id, foto)
        else:
           msg = bot.reply_to(message, 'no such camera id \n try another one')
           bot.register_next_step_handler(msg, update_and_send_info_one_dvor)
    else:
        bot.send_chat_action(message.chat.id, 'typing')
        msg = bot.reply_to(message, 'incorrect input \n you shoud write smth like this:')
        bot.send_message(message.chat.id, '123')
        bot.register_next_step_handler(msg, update_and_send_info_one_dvor)


def add_camera(query): # 3.1
    bot.answer_callback_query(query.id)
    user_id = query.from_user.id
    print(hack_user_database.getinfo(user_id))
    ask_user_to_choose_camera(query.message)


def ask_user_to_choose_camera(message): # 3.2
    bot.send_chat_action(message.chat.id, 'typing')
    ids = hack_dvor_database.allids()
    msg = bot.reply_to(message, 'choose one camera from:\n'+str(ids))
    bot.register_next_step_handler(msg, get_answer_choose_camera)


def get_answer_choose_camera(message): # 3.3
    x = message.text.split('\n')
    print(x)
    # print(message)
    if x[0] != 'No':
        if len(x) == 1 and is_number(x[0]): # correct input?
            if not hack_dvor_database.is_id_in_table(x[0]):
                hack_user_database.create_new_dvor_for_user(message.from_user.id,x[0])
                bot.send_message(message.chat.id, 'added')
            else:
               msg = bot.reply_to(message, 'this camera id is already existed \n try another one or write No')
               bot.register_next_step_handler(msg, get_answer_choose_camera)
        else:
            bot.send_chat_action(message.chat.id, 'typing')
            msg = bot.reply_to(message, 'incorrect input \n you shoud write smth like this:')
            bot.send_message(message.chat.id, '123')
            bot.register_next_step_handler(msg, get_answer_choose_camera)


def give_one_info(query): # 1.1
    bot.answer_callback_query(query.id)
    user_id = query.from_user.id
    print(hack_user_database.getinfo(user_id),user_id)
    ask_user_for_dvor_id(query.message, user_id)


def ask_user_for_dvor_id(message,user_id): # 1.2
    bot.send_chat_action(message.chat.id, 'typing')
    ids = hack_user_database.getinfo(user_id)
    msg = bot.reply_to(message, 'choose camera id from:\n'+str(ids))
    bot.register_next_step_handler(msg, send_info_one_dvor)


def send_info_one_dvor(message): # 1.3
    x = message.text.split('\n')
    print(x)
    # print(message)
    if len(x) == 1 and is_number(x[0]): # correct input?
        if hack_user_database.getinfo(message.from_user.id) != None:
            bot.send_message(message.chat.id, 'some information about space near house '+str(x[0]) + '\n' + str(hack_dvor_database.getinfo(x[0])[0]))
        else:
           msg = bot.reply_to(message, 'no such camera id \n try another one')
           bot.register_next_step_handler(msg, send_info_one_dvor)
    else:
        bot.send_chat_action(message.chat.id, 'typing')
        msg = bot.reply_to(message, 'incorrect input \n you shoud write smth like this:')
        bot.send_message(message.chat.id, '123')
        bot.register_next_step_handler(msg, send_info_one_dvor)



def is_number(str):
    try:
        float(str)
        return True
    except ValueError:
        return False



bot.polling(none_stop=True)
