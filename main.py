from aiogram import Bot, Dispatcher, types
import asyncio
from aiogram.filters import Command  
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
    #await bot.send_message(message.chat.id, 'Hello')
    await message.answer('Hello')

async def main():
    await dp.start_polling(bot)  # чтобы работала постоянно

asyncio.run(main()) # запуск бота