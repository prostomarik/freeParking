import telebot
# from telebot import apihelper
import hack_config
import json
import traceback
import pprint


bot = telebot.TeleBot(hack_config.TOKEN)


@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(
        message.chat.id,
        'Greetings! I can show you free space for parking.\n' +
        'To get this information use /getinfo.\n' +
        'To get help press /help.'
    )


bot.polling(none_stop=True)
