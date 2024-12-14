from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_buttons = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Привет')],
    [KeyboardButton(text='Пока')]
], resize_keyboard=True)

task2_buttons = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Видео',url='https://vkvideo.ru/video-228285423_456239532')],
    [InlineKeyboardButton(text='Музыка',url='https://music.yandex.ru/home')],
    [InlineKeyboardButton(text='Новости',url='https://ria.ru/')]
])