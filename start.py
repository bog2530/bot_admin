import asyncio
import os

from aiogram import Bot, Dispatcher, types, Router
from dotenv import load_dotenv
from aiogram.filters import CommandStart

from handlers.utils import check_user_admin
from menu.menu import my_menu
from handlers.handlers import form_router


load_dotenv()

router = Router()


@router.message(CommandStart())
async def start_command(message: types.Message):
    user = message.from_user.id
    if await check_user_admin(user):
        markup = my_menu
        await message.answer(
            'Добро пожаловать в админ-бот',
            reply_markup=markup,
        )
    else:
        await message.answer('Отказано в доступе')


async def main():
    bot = Bot(token=os.getenv('SECRET_KEY'))
    dp = Dispatcher()
    dp.include_router(form_router)
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
