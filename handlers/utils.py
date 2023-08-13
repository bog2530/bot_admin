import os

from aiogram.fsm.state import State, StatesGroup


class Storage(StatesGroup):
    """Хранилище для отправки текста"""
    id_or_all = State()
    text = State()
    confirmation = State()


async def check_user_admin(tg_id):
    return tg_id == int(os.getenv('USER_ADMIN'))


async def check_user(tg_id):
    if tg_id == 'ВСЕМ':
        return True
    return False
