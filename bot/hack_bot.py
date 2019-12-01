import telebot
# from telebot import apihelper
import hack_config
import json
import traceback
import pprint
import hack_user_database


bot = telebot.TeleBot(hack_config.TOKEN)


@bot.message_handler(commands=['start'])
def start_command(message):
    hack_user_database.create_table_users()
    hack_user_database.create_new_user(message.from_user.id)
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
        telebot.types.InlineKeyboardButton('one place', callback_data='one'),
        telebot.types.InlineKeyboardButton('all places', callback_data='all')
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
    if data.startswith('all'): # 2
        give_all_info(query)


def give_one_info(query): # 1.1
    bot.answer_callback_query(query.id)
    user_id = query.from_user.id
    print(hack_user_database.getinfo(user_id))
    ask_user_for_dvor_id(query.message)


def ask_user_for_dvor_id(message): # 1.2
    bot.send_chat_action(message.chat.id, 'typing')
    ids = hack_user_database.getinfo(message.from_user.id)
    msg = bot.reply_to(message, 'print dvor id from:\n'+str(ids))
    bot.register_next_step_handler(msg, send_info_one_dvor)


def send_info_one_dvor(message): # 1.3
    x = message.text.split('\n')
    print(x)
    # print(message)
    if len(x) == 1 and is_number(x[0]): # correct input?
        if hack_user_database.getinfo(message.from_user.id) != None:
            bot.send_message(message.chat.id, 'som infor about dvor'+str(x))
        else:
           msg = bot.reply_to(message, 'no such dvor id \n try another one')
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
