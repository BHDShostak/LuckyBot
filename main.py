import telebot
import random
from telebot import types

import config

bot = telebot.TeleBot(config.token())

@bot.message_handler(commands=['start','help'])
def start(message):
    mess = f'Hallo, do you wand a random number from 0 to 100 <b>{message.from_user.first_name}</b> ?'
    bot.send_message(message.chat.id,mess, parse_mode='html')

markup = types.ReplyKeyboardMarkup(row_width=2)
itembtn1 = types.KeyboardButton('yes')
itembtn2 = types.KeyboardButton('no')
markup.add(itembtn1, itembtn2)
tb.send_message(chat_id, "Choose one word:", reply_markup=markup)

@bot.message_handler()
def user_text(message):
    if message.text == "yes":
        rnumb = random.randint(0,100)
        bot.send_message(message.chat.id,rnumb, parse_mode='html')
        bot.send_message(message.chat.id, f'Thanks for trying your luck! <b>{message.from_user.first_name}</b>',
                         parse_mode='html')
    else:
        bot.send_message(message.chat.id,f'Unfortunately you can not use your success <b>{message.from_user.first_name}</b> !', parse_mode='html')
        bot.send_message(message.chat.id, f'If you want you can re-enter your luck with command - /start , thanks!',
                         parse_mode='html')

bot.polling(none_stop=True)