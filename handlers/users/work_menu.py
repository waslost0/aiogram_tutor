from aiogram import types
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import ReplyKeyboardRemove

from keyboards.default import menu
from loader import dp


@dp.message_handler(Command('menu'))
async def show_menu(message: types.Message):
    await message.answer("Please select item from menu", reply_markup=menu)


@dp.message_handler(text='Coca')
async def get_coca(message: types.Message):
    await message.answer('You selected Coca.\nI`m calling police')


@dp.message_handler(Text(equals=['Coca', 'Cola']))
async def get_food(message: types.Message):
    await message.answer(f'You selected: {message.text}', reply_markup=ReplyKeyboardRemove())
