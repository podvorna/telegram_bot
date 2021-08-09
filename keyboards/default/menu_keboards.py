from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Визначити розмір"),
        ],
        [
            KeyboardButton(text="Переглянути каталог товарів"),
            KeyboardButton(text="Наш інстаграм")
        ],
    ],
    resize_keyboard=True
)

