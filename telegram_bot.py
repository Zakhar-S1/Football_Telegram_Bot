import config
import telebot
import requests
from controller_bot import menu_mess_controller, group_mess_controller
from functions_bot import registration, return_user, update_state, table_CL, table_PL, table_PD, matches_today, add_history, return_history
from keyboard_bot import menu, menu_group
import processing

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id,"Hello, I'm FOOTBALLCHIK",reply_markup = menu())
    registration(message)

@bot.message_handler(content_types=['text'])
def send_message(message):
    bot_st = return_user(message)
    if bot_st['state'] == 'menu':
        menu_mess_controller(message)
    elif bot_st['state'] == 'menu_group':
        group_mess_controller(message)

@bot.message_handler(content_types=['photo'])
def send_photo(message):

    processing.photo_processing(message)

if __name__ == "__main__":
	bot.polling()
