from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.inline.menu import menu_start
from loader import dp







@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Assalomu aleykum botimizga xush kelibsiz!!!, {message.from_user.full_name}!",reply_markup=menu_start)

