from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery
from aiogram import dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from keyboards.inline.callback_dates import choice_callback
from keyboards.inline.choice_keyboards import choice

from loader import dp


class Callback_answer_state(StatesGroup):
    waiting_for_size1 = State()
    waiting_for_size2 = State()



@dp.callback_query_handler(choice_callback.filter(your_choice='yes'))
async def ask_choice(call: CallbackQuery, callback_data: dict):
    await call.message.answer('Чудово, для цього тобі знадобиться лише сантиметрова стрічка та декілька хвилин.')
    await call.message.answer('Спочатку виміряй обхват під грудьми. Сантиметрова стрічка має бути розташована паралельно підлозі.')
    await call.message.answer('Напиши мені свої заміри, просто цифру.')
    
general_size=[]

@dp.message_handler(regexp=r"^(\d+)$")
async def make_size_1(message: types.Message):
    global general_size
    size1 = int(message.text)
    if  size1 >=68 and size1<=75: 
        general_size.append(size1)
        await message.answer('А тепер, виміряй обхват грудей. \n Та не забудь написати мені свої заміри і я обовязково визначу твій розмір бра.')
    await Callback_answer_state.waiting_for_size1.set()
        
@dp.message_handler(state='*')
async def make_size_2(message: types.Message):
    global general_size
    size2 = int(message.text)
    if  size2 >= 80 and size2 <= 86: 
        general_size.append(size2)
        await message.answer('Чудово, твій розиір-', general_size)
    await Callback_answer_state.next()
   

