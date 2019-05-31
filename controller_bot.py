import telebot
import config
from keyboard_bot import menu, menu_group
from functions_bot import registration, return_user, update_state, table_CL, table_PL, table_PD, matches_today, add_history, return_history, info_player
import time

GROUPS = "Input group [A-H]"

bot = telebot.TeleBot(config.token)

def menu_mess_controller(message):

    if message.text == 'Table CL':
        add_history(message,[time.time(),'Table CL'])
        bot.send_message(message.chat.id,GROUPS,reply_markup = menu_group())
        update_state(message,"menu_group")
    elif message.text == 'Table PL':
        add_history(message,[time.time(),'Table PL'])
        answer = table_PL()
        for i in range(len(answer)):
            bot.send_message(message.chat.id,answer[i])
    elif message.text == 'Table PD':
        add_history(message,[time.time(),'Table PD'])
        answer = table_PD()
        for i in range(len(answer)):
            bot.send_message(message.chat.id,answer[i])
    elif message.text == 'Matches':
        add_history(message,[time.time(),'Matches'])
        answer = matches_today()
        for i in range(len(answer)):
            bot.send_message(message.chat.id,answer[i])
    elif message.text == 'History':
        add_history(message,[time.time(),'History'])
        bot.send_message(message.chat.id,return_history(message))

def group_mess_controller(message):

    if message.text == 'Back✖️':
        add_history(message,[time.time(),'Back'])
        bot.send_message(message.chat.id,"Отмена✖️",reply_markup = menu())
        update_state(message,"menu")
    else:
        bot.send_message(message.chat.id,"✅")
        answer = table_CL(message)
        for i in range(len(answer)):
            bot.send_message(message.chat.id,answer[i])
