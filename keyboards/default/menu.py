from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Coca')
        ],
        [
            KeyboardButton(text='Cola'),
            KeyboardButton(text='Coffee')
        ],
    ],
    resize_keyboard=True
)
