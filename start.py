import asyncio
import os

from aiogram import Bot, Dispatcher, types, Router
from dotenv import load_dotenv
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import CommandStart

from handlers.handlers import form_router
from handlers.utils import check_user_admin


load_dotenv()

router = Router()


@router.message(CommandStart())
async def start_command(message: types.Message):
    user = message.from_user.id

    if check_user_admin(user):
        text = 'Отказано в доступе'
        await message.answer(text)
    btn_bot = KeyboardButton(text="тест")
    markup = ReplyKeyboardMarkup(keyboard=[[btn_bot]], resize_keyboard=True)
    text = (
        f"Добро пожаловать в админ-бот"
    )
    await message.answer(text, reply_markup=markup)
# os.getenv('SECRET_KEY')


async def main():
    bot = Bot(token='1995305307:AAHW9dZISzV33_5BmlVepodlJVQjcjmGq0A')
    dp = Dispatcher()
    dp.include_router(router)
    dp.include_router(form_router)

    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
