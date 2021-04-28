from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp


@dp.message_handler(Command('start'))
async def echo(message: types.Message):
    await message.answer('q')


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)
