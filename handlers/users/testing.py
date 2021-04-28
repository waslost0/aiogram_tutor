from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp
from aiogram import types
from states import Test


@dp.message_handler(Command('test'))
async def enter_test(message: types.Message):
    await message.answer('Testing started\n'
                         'Question 1\n\n'
                         'qwfgqowyuigbquywg?')
    await Test.Q1.set()


@dp.message_handler(state=Test.Q1)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer1=answer)
    await message.answer('Question 2 \n\n'
                         'iquhwiquwohfg?')
    await Test.next()


@dp.message_handler(state=Test.Q2)
async def answer_q2(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer1 = data.get('answer1')
    answer2 = message.text
    await message.answer('Thx')
    await message.answer(f'Answer 1: {answer1}')
    await message.answer(f'Answer 2: {answer2}')
    await state.finish()
    # await state.reset_state()
    # await state.reset_state(with_data=False)
