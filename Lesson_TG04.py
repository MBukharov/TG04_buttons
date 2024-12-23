import asyncio
from aiogram import Bot, Dispatcher,F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from config import TOKEN_TG
from buttons import start_buttons, task2_buttons, show_more_button, option_button

bot = Bot(token=TOKEN_TG)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer('Нажми на нужную кнопку', reply_markup=start_buttons)

@dp.message(Command('help'))
async def start(message: Message):
    await message.answer('Доступные команды:\n/start\n/links\n/dynamic')

@dp.message(F.text == 'Привет')
async def hello(message: Message):
    await message.reply(f'Привет, {message.from_user.first_name}!')

@dp.message(F.text == 'Пока')
async def hello(message: Message):
    await message.reply(f'До свидания, {message.from_user.first_name}!')

@dp.message(Command('links'))
async def links(message: Message):
    await message.answer('Вот интересные ссылки',reply_markup=task2_buttons)

@dp.message(Command('dynamic'))
async def dynamic(message: Message):
    await message.answer('...',reply_markup=show_more_button)

@dp.callback_query(F.data == 'show_more')
async def show_more(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text('Выберите опцию', reply_markup=await option_button())

@dp.callback_query(F.data.startswith('option'))
async def option(callback: CallbackQuery):
    await callback.answer('')
    param = callback.data.split(':')[1]
    await callback.message.answer(param)


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())