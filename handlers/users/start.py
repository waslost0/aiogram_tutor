from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import User

from loader import dp
from utils.misc import rate_limit


@rate_limit(limit=10)
@dp.message_handler(CommandStart())
async def bot_start(message: types.Message, user: User):
    await message.answer(f'Q, {message.from_user.full_name}!\n'
                         f'User from middleware: {user.__dict__}')
