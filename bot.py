import os

from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dotenv import load_dotenv

from handlers.menu import start_command

load_dotenv()

bot = Bot(token=os.getenv('SECRET_KEY'))
storage = MemoryStorage()

if __name__ == "__main__":
    dp = Dispatcher(bot, storage=storage)
    dp.register_message_handler(start_command, commands=['start'])
    executor.start_polling(dp, skip_updates=True)
