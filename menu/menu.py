from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btn_my_menu = KeyboardButton(text='Главное меню 🔙')
main_menu = ReplyKeyboardMarkup(
    keyboard=[[
        btn_my_menu
    ]],
    resize_keyboard=True,
)

# __Главное меню__
btn_message_user = KeyboardButton(text='📨 Отправить сообщение')
my_menu = ReplyKeyboardMarkup(
    keyboard=[[
        btn_message_user,
    ]],
    resize_keyboard=True,
)

# __Меню модтверждения__
btn_message_yes = KeyboardButton(text='Y')
btn_message_no = KeyboardButton(text='n//Главное меню 🔙')
other_menu = ReplyKeyboardMarkup(
    keyboard=[[
        btn_message_yes,
        btn_message_no,
    ]],
    resize_keyboard=True,
)

# __Меню выбора пользователей__
btn_message_all = KeyboardButton(text='ВСЕМ')
all_menu = ReplyKeyboardMarkup(
    keyboard=[[
        btn_message_all,
        btn_my_menu,
    ]],
    resize_keyboard=True,
)




