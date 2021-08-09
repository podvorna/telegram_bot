from aiogram.types import InlineKeyboardMarkup
from aiogram.types.inline_keyboard import InlineKeyboardButton

from keyboards.inline.callback_dates import choice_callback

choice = InlineKeyboardMarkup(row_width=2,
                              inline_keyboard=[
                                 [
                                     InlineKeyboardButton(
                                         text='Давай!',
                                         callback_data=choice_callback.new(your_choice='yes',
                                                                           quantity=1)),
                                     
                                     InlineKeyboardButton(
                                       text='Я вже все знаю😎',
                                       callback_data=choice_callback.new(your_choice='no',
                                                                           quantity=0))
                                 ]    
                                              ])

choice2 = InlineKeyboardMarkup(row_width=3,
                              inline_keyboard=[
                                 [
                                     InlineKeyboardButton(
                                         text='75B',
                                         callback_data=choice_callback.new(your_choice='75B',
                                                                           quantity=1)),
                                     
                                     InlineKeyboardButton(
                                       text='80B',
                                       callback_data=choice_callback.new(your_choice='80B',
                                                                           quantity=0)),
                                     InlineKeyboardButton(
                                       text='85B',
                                       callback_data=choice_callback.new(your_choice='85B',
                                                                           quantity=0))
                                 ]    
                                              ])

insta_keyboard = InlineKeyboardMarkup()
INSTA_LINK = 'https://www.instagram.com/p/CSEskonjSSc/'
insta_link = InlineKeyboardButton(text='Переглянути', url=INSTA_LINK)

insta_keyboard.insert(insta_link)