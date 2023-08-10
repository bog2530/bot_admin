import os

from aiogram.fsm.state import State, StatesGroup


class Storage(StatesGroup):
    """Хранилище для отправки текста"""
    id_or_all = State()
    message = State()
    confirmation = State()


def check_user_admin(tg_id):
    admin = os.getenv('USER')
    return tg_id == admin
