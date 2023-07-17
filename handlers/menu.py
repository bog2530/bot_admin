from aiogram import types

from db.orm import check_admin


async def start_command(message: types.Message):

    orm.add_user(
        message.from_user.id,
        message.from_user.username,
    )
    user
    btn_bot = types.KeyboardButton("Гадать с помощью бота")

    btn_setting = types.KeyboardButton("Настройки")
    btn_individual = types.KeyboardButton("Заказать индивидуальное гадание")

    markup = types.reply_keyboard.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(btn_setting, btn_individual)
    markup.row(btn_bot)

    text = (
        f"Привет {message.from_user.first_name}, этот бот поможет тебе принять решение."
    )
    await message.answer(text, reply_markup=markup)