from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

start_buttons = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Привет')],
    [KeyboardButton(text='Пока')]
], resize_keyboard=True)

task2_buttons = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Видео',url='https://vkvideo.ru/video-228285423_456239532')],
    [InlineKeyboardButton(text='Музыка',url='https://music.yandex.ru/home')],
    [InlineKeyboardButton(text='Новости',url='https://ria.ru/')]
])

show_more_button = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Показать больше',callback_data='show_more')]
])

option_buttons =['Опция 1','Опция 2']

def option_buttons():
    keyboard = InlineKeyboardBuilder()
    for button in option_buttons:
        keyboard.add(InlineKeyboardButton(text=button, callback_data='option:button)'))