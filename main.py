import telebot
import os
from dotenv import load_dotenv
from telebot import types
#import webbrowser

load_dotenv()  
BOT_TOKEN = os.getenv("BOT_TOKEN")  
bot = telebot.TeleBot(BOT_TOKEN)

#@bot.message_handler(commands = ['site', 'website'])
#def site(message):
#    webbrowser.open('')

@bot.message_handler(content_types = ['photo'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Перейти на сайт', url = 'https://ya.ru/')
    markup.row(btn1)
    btn2 = types.InlineKeyboardButton('Удалить фото', callback_data = 'delete')
    btn3 = types.InlineKeyboardButton('Изменить текст', callback_data = 'edit')
    markup.row(btn2,btn3) # можно делать add markup.add(types.InlineKeyboardButton('Изменить текст', callback_data = 'edit')) 
                    # но есть проблема что тогда кнопки будут друг под другом
    bot.reply_to(message,"Очень красивое фото", reply_markup = markup)

@bot.message_handler(commands=['start', 'main'])
def main(message):
    bot.send_message(message.chat.id, 'Яночка я тебя люблю!!!!') ## первый пункт указываю айди чата

@bot.message_handler(commands=['hello'])
def main(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}')

@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, '<b>Help<b> information', parse_mode ='html') 

@bot.message_handler()
def info(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}') # тоже самое что и send_message только будет ответом на предыдущее сообщение

@bot.callback_query_handler(func = lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, )
bot.polling(non_stop=True)

#bot.infinity_polling() - тоже самое что polling