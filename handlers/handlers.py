import os

from aiogram import types, Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext


from .utils import Storage
form_router = Router()

# Отправить ЛС 📨


@form_router.message(F.text.casefold() == 'тест')
async def message_ls(message: types.Message, state: FSMContext):
    await message.answer(
        'Введите ID получателя или слово ВСЕМ или вернитесь в главное меню',
        # reply_markup=ReplyKeyboardRemove(),
    )
    await state.set_state(Storage.id_or_all)


# @form_router.message('Главное меню')
@form_router.message(F.text.casefold() == 'Главное меню 🔙')
async def to_menu(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer(
        "Cancelled.",
        # reply_markup=ReplyKeyboardRemove(),
    )


@form_router.message(Storage.id_or_all)
async def input_mesage(message: types.Message, state: FSMContext):
    await state.update_data(message=message.text)
    await state.set_state(Storage.message)
    await message.answer(
        'Введите сообщение или вернитесь в главное меню!',
        # reply_markup=ReplyKeyboardMarkup(...
        #     resize_keyboard=True,
        # ),
    )


@form_router.message(Storage.message)
async def input_confirmation(message: types.Message, state: FSMContext):
    await state.update_data(confirmation=message.text)
    await state.set_state(Storage.confirmation)
    await message.answer(
        'Подтвердите отправку',
        # reply_markup=ReplyKeyboardMarkup(...
        #     resize_keyboard=True,
        # ),
    )


async def end_message_ls(message: types.Message, data):
    text = data['text']
    await message.answer(text=text)

