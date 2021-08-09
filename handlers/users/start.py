import states
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery


from keyboards.inline.callback_dates import choice_callback
from keyboards.inline.choice_keyboards import choice

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f'Привіт, {message.from_user.full_name} !\n'
                         '\n'
                         'Це бот-помічник KOZZA lingerie.\n'
                         'Він допоможе тобі правильно визначити свої розміри та підібрати найулюбленішу білизну саме для тебе ♥')
    await message.answer(text="Давай разом визначимо твій розмір білизни ?",
                         reply_markup=choice)

    
    