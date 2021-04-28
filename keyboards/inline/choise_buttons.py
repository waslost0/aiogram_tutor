from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_datas import buy_callback

choise = InlineKeyboardMarkup(row_width=2,
                              inline_keyboard=[
                                  [
                                      InlineKeyboardButton(
                                          text='Buy pear',
                                          callback_data=buy_callback.new(item_name='pear',
                                                                         quantity=2)
                                      ),
                                      InlineKeyboardButton(
                                          text='Buy apple',
                                          callback_data='buy:apple:5'
                                      ),
                                  ],
                                  [
                                      InlineKeyboardButton(
                                          text='Cancel',
                                          callback_data='cancel'
                                      )
                                  ]
                              ])

pear_keyboard = InlineKeyboardMarkup()
PEAR_LINK = 'https://google.com'
pear_link = InlineKeyboardMarkup(text='Buy here', url=PEAR_LINK)
pear_keyboard.insert(pear_link)
