from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery
from aiogram import dispatcher


from keyboards.inline.callback_dates import choice_callback
from keyboards.inline.choice_keyboards import choice2
from keyboards.inline.choice_keyboards import insta_keyboard

from loader import dp


@dp.callback_query_handler(choice_callback.filter(your_choice='no'))
async def ask_choice(call: CallbackQuery, callback_data: dict):
    await call.message.answer(text='Чудово, обирай тоді свій розмір',
                              reply_markup=choice2)

@dp.callback_query_handler(choice_callback.filter(your_choice='75B'))
async def ask_choice(call: CallbackQuery, callback_data: dict):
    await call.message.answer(text='А ось деякі варінти, що можуть тобі підійти',
                              reply_markup=insta_keyboard)