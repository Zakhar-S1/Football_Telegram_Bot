import os
import machine
from telebot import TeleBot, types
from config import token, dictionary
from functions_bot import info_player

bot = TeleBot(token)

def install_inline_buttons(message, iterator, tx, add_tx):

    user_markup = types.InlineKeyboardMarkup()

    for btn in iterator:
        user_markup.add(types.InlineKeyboardButton(text = btn, callback_data = add_tx + btn))

    bot.send_message(message.chat.id, text = tx, reply_markup = user_markup)

def photo_processing(message):

    photo = str(message.photo[-1].file_id) + '.jpg'

    info = bot.get_file(photo[:-4])
    downloaded = bot.download_file(info.file_path)

    with open(photo, 'wb') as new_file:
        new_file.write(downloaded)

    img = open(photo, 'rb')
    data_network = machine.recognize_teacher(img)

    os.rename(f"/Users/user/Desktop/telegram-env/telegram-bot/{photo}",
          f"/Users/user/Desktop/telegram-env/telegram-bot/Football_Faces{photo}")

    print(data_network[1])
    print(data_network[0])

    if data_network[0] == 0 or data_network[1] < 25:
        msg = 'Совпадений не найдено'
    else:
        for key, value in dictionary.items():
             if value == data_network[0]:
                 msg = 'Мне кажется, что это ' + ''.join(key)

                 bot.send_message(message.chat.id, msg)
                 bot.send_message(message.chat.id,info_player(value))
