from aiogram import types
from filters import IsPrivate
from loader import dp

from data.config import ADMINS_ID


@dp.message_handler(IsPrivate(), text='secret', user_id=ADMINS_ID)
async def admin_chat_secret(message: types.Message):
    await message.answer('This is secret message')
