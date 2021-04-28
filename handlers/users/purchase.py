from aiogram import types
from loguru import logger

from keyboards.inline.callback_datas import buy_callback
from keyboards.inline.choise_buttons import choise, pear_keyboard
from loader import dp, bot
from aiogram.dispatcher.filters import Command


@dp.message_handler(Command('items'))
async def show_items(message: types.Message):
    await message.answer(text='For sale we have 2 pieces: 5 apples an 2 pear.\n'
                              'If you want some, press button, if not Cancel',
                         reply_markup=choise)


@dp.callback_query_handler(buy_callback.filter(item_name='pear'))
async def buying_pear(call: types.CallbackQuery, callback_data: dict):
    # await bot.answer_callback_query(callback_query_id=call.id)
    await call.answer(cache_time=60)
    logger.info(f'callback_data = {call.data}')
    logger.info(f'callback_data dict = {call}')
    quantity = callback_data.get('quantity')
    await call.message.answer(f'You selected to buy pear. Pears count {quantity}. Thx',
                              reply_markup=pear_keyboard)


@dp.callback_query_handler(buy_callback.filter(item_name='apple'))
async def buying_apple(call: types.CallbackQuery, callback_data: dict):
    # await bot.answer_callback_query(callback_query_id=call.id)
    await call.answer(cache_time=60)
    logger.info(f'callback_data = {call.data}')
    logger.info(f'callback_data dict = {call}')
    quantity = callback_data.get('quantity')
    await call.message.answer(f'You selected to buy apple. Apples count {quantity}. Thx')


@dp.callback_query_handler(text="cancel")
async def cancel_buying(call: types.CallbackQuery):
    await call.answer("Canceled!", show_alert=True)

    await call.message.edit_reply_markup(reply_markup=None)

    # await bot.edit_message_reply_markup(chat_id=call.from_user.id,
    #                                     message_id=call.message.message_id,
    #                                     reply_markup=None)
