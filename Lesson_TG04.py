import asyncio
from aiogram import Bot, Dispatcher,F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from config import TOKEN_TG
from buttons import start_buttons, task2_buttons

bot = Bot(token=TOKEN_TG)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer('Нажми на нужную кнопку', reply_markup=start_buttons)

@dp.message(F.text == 'Привет')
async def hello(message: Message):
    await message.reply(f'Привет {message.from_user.first_name}!')

@dp.message(F.text == 'Пока')
async def hello(message: Message):
    await message.reply(f'До свидания {message.from_user.first_name}!')

@dp.message(Command('links'))
async def links(message: Message)
    await message.edit_text('Вот интересные ссылки',reply_markup=task2_buttons)


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())