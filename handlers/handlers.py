import os

from aiogram import types, Router, F, html
from aiogram.fsm.context import FSMContext


from .utils import Storage, check_user
from menu.menu import (
    all_menu,
    other_menu,
    main_menu,
    my_menu,
)

form_router = Router()


async def cancellation_message(message, state):
    await state.clear()
    await message.answer(
        "Оправка отменена",
        reply_markup=my_menu,
    )


# @form_router.message(Command("w"))
@form_router.message(F.text == '📨 Отправить сообщение')
async def message_ls(message: types.Message, state: FSMContext):
    await message.answer(
        'Введите ID получателя или слово ВСЕМ или вернитесь в главное меню',
        reply_markup=all_menu,
    )
    await state.set_state(Storage.id_or_all)


# @form_router.message('Главное меню')
# @form_router.message(F.text.casefold() == 'Главное меню 🔙')
# # @form_router.message(F.text.casefold() == 'Главное меню 🔙')
# async def to_menu(message: types.Message, state: FSMContext):
#     await state.clear()
#     await message.answer(
#         "Оправка отменена",
#         reply_markup=my_menu,
#     )


@form_router.message(Storage.id_or_all)
async def input_mesage(message: types.Message, state: FSMContext):
    if message.text == 'Главное меню 🔙':
        await cancellation_message(message, state)
    elif await check_user(message.text) is False:
        await message.answer(
            'Пользователь не найден. Отправка отменена',
            reply_markup=my_menu,
        )
        await state.clear()
    else:
        await state.update_data(id_or_all=message.text)
        await state.set_state(Storage.text)
        await message.answer(
            'Введите сообщение или вернитесь в главное меню!',
            reply_markup=main_menu
        )


@form_router.message(Storage.text)
async def input_confirmation(message: types.Message, state: FSMContext):
    if message.text == 'Главное меню 🔙':
        await cancellation_message(message, state)
    else:
        await state.update_data(text=message.text)
        await state.set_state(Storage.confirmation)
        await message.answer(
            'Подтвердите отправку',
            reply_markup=other_menu
        )


@form_router.message(Storage.confirmation)
async def message_sending(message: types.Message, state: FSMContext):
    if message.text == 'n//Главное меню 🔙':
        await cancellation_message(message, state)
    elif message.text == 'Y':
        data = await state.update_data(confirmation=message.text)
        await state.clear()
        await sending(message=message, data=data)


async def sending(message: types.Message, data):
    text = f'''
    id = {html.quote(data['id_or_all'])}
    text ={html.quote(data['text'])}
    '''
    await message.answer(text=text, reply_markup=my_menu)



