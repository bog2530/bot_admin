# import os
#
# from aiogram import Bot, Dispatcher, executor
# from aiogram.contrib.fsm_storage.memory import MemoryStorage
# from dotenv import load_dotenv
#
# from handlers.menu import start_command
#
# load_dotenv()
#
# bot = Bot(token=os.getenv('SECRET_KEY'))
# storage = MemoryStorage()


from aiohttp import web
from aiogram import Bot, Dispatcher, types, executor
import json

# Инициализация бота
bot = Bot(token='1995305307:AAF7CbNBr8PJJIWmS4EpwPTo_bcpXPEj9wk')
Bot.set_current(bot)
dp = Dispatcher(bot)

app = web.Application()

webhook_path = '/1995305307:AAF7CbNBr8PJJIWmS4EpwPTo_bcpXPEj9wk'


# async def set_webhook():
#     webhook_uri = f'https://5c41-78-37-182-180.ngrok.io{webhook_path}'
#     await bot.set_webhook(
#         webhook_uri # here we are telling our Telegram API to use the WEBHOOK
#     )
#
# async def on_startup(_):
#     await set_webhook()

# @dp.message_handler()
# async def echo(message: types.Message):
#     # old style:
#     await bot.send_message(message.chat.id, message.text)


# async def handle_webhook(request):
#     url = str(request.url)
#     index = url.rfind('/')
#     token = url[
#             index + 1:]  # this method is used because in some cases request object can't be correctly interpreted and match_info will return empty object
#     if token == '1995305307:AAF7CbNBr8PJJIWmS4EpwPTo_bcpXPEj9wk':
#         update = types.Update(**await request.json())  # we just parse our bytes into dictionary
#         await dp.process_update(update)  # this will just process update using the appropriate handler
#         return web.Response()  # construct the response object
#     else:
#         return web.Response(status=403)  # if our TOKEN is not authenticated


  # here we set router for process each webhook http request through our handler_


# Обработчик POST-запросов
# async def handle(request):
#     data = await request.json()
#     text = data.get('text')
#     chat_id = data.get('chat_id')
#     if text and chat_id:
#         await bot.send_message(chat_id=chat_id, text=text)
#         return web.Response(text='OK')
#     else:
#         return web.Response(text='Invalid request data')


# Запуск веб-приложения
# if __name__ == '__main__':
#
#
#     web.run_app(app, port=80)


# if __name__ == "__main__":
#     app.router.add_post('/1995305307:AAF7CbNBr8PJJIWmS4EpwPTo_bcpXPEj9wk', handle_webhook)
#     app.router.add_post('/endpoint', handle)
#     app.on_startup.append(on_startup)
#
#     web.run_app(
#         app,
#         host='0.0.0.0',
#         port=8080
#     )
#

# if __name__ == "__main__":
#     dp = Dispatcher(bot, storage=storage)
#     dp.register_message_handler(start_command, commands=['start'])
#     executor.start_polling(dp, skip_updates=True)


# ---------- hendlers -----------

# from aiogram import types
#
# from db.orm import check_user
#
#
# @dp.message_handler()
# async def start_command(message: types.Message):
#
#     user = message.from_user.id
#
#     if check_user(user):
#         text = 'Отказано в доступе'
#         await message.answer(text)
#     btn_bot = types.KeyboardButton("тест")
#     markup = types.reply_keyboard.ReplyKeyboardMarkup(resize_keyboard=True)
#     markup.row(btn_bot)
#
#     text = (
#         f"Добро пожаловать в админ-бот"
#     )
#     await message.answer(text, reply_markup=markup)
#
#
# async def message_ls(message: types.Message):
#     ...
#
#
# async def message_all(message: types.Message):
#     ...
