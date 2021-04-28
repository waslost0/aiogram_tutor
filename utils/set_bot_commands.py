from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand("start", "Начало работы с ботом"),
        types.BotCommand("decode", "Decode string"),
        types.BotCommand("encode", "Encode string"),
        types.BotCommand("add", "Add user"),
    ])
