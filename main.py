from aiogram import Bot, Dispatcher, types
import asyncio
from aiogram.types.web_app_info import WebAppInfo
from aiogram.filters import Command  
from aiogram.utils.keyboard import InlineKeyboardBuilder
import os
from dotenv import load_dotenv
import sqlite3  

load_dotenv()  
BOT_TOKEN = os.getenv("BOT_TOKEN")  

#bot = telebot.TeleBot(BOT_TOKEN)
bot = Bot(BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))  
async def start(message:types.Message):
    button = types.KeyboardButton(
        text="Сделать заказ",
        web_app=WebAppInfo(url='index.html')
    )
    markup = types.ReplyKeyboardMarkup(
        keyboard=[[button]],
        resize_keyboard=True  # можно убрать, если не нужно автоизменение размера
    )
    await message.answer('Привет мой друг', reply_markup=markup)


async def main():
    await dp.start_polling(bot)  # чтобы работала постоянно

asyncio.run(main()) # запуск бота