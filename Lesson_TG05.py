import asyncio
from aiogram import Bot, Dispatcher,F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from config import TOKEN_TG
import requests
from googletrans import Translator
from datetime import datetime

bot = Bot(token=TOKEN_TG)
dp = Dispatcher()

def get_dollar_price():
    url = 'https://www.cbr-xml-daily.ru/daily_json.js'
    response = requests.get(url)
    data = response.json()
    return data['Valute']['USD']['Value']

def get_day_info():
    url = "http://numbersapi.com/"
    date = datetime.now()
    date_str = date.strftime("%m/%d/")
    url = url + date_str + 'date'

    r = requests.get(url)

    translator = Translator()
    translated_text = translator.translate(r.text, dest="ru").text
    return translated_text

def get_dog_photo():
    url = 'https://random.dog/woof.json'
    response = requests.get(url)
    data = response.json()
    return data['url']

def get_joke():
    url = 'https://geek-jokes.sameerkumar.website/api?format=json'
    response = requests.get(url)
    data = response.json()
    translator = Translator()
    translated_text = translator.translate(data['joke'], dest="ru").text
    return  translated_text


def get_yesorno():
    url = 'https://yesno.wtf/api'
    response = requests.get(url)
    data = response.json()
    return data


@dp.message(CommandStart())
async def start(message: Message):
    await message.reply('Доступные команды:\n/dollar - курс доллара'
                        '\n/day - информация о сегодняшнем дне'
                        '\n/dog - фото собаки'
                        '\n/joke - получить шутку'
                        '\n/yes_or_no - бросить жребий (да или нет)')


@dp.message(Command('dollar'))
async def dollar(message: Message):
    await message.reply(f'Курс доллара: {get_dollar_price()} руб.')

@dp.message(Command('day'))
async def day(message: Message):
    await message.reply(f'{get_day_info()}')

@dp.message(Command('dog'))
async def dog(message: Message):
    await message.answer_photo(photo = get_dog_photo())

@dp.message(Command('joke'))
async def joke(message: Message):
    await message.reply(f'{get_joke()}')

@dp.message(Command('yes_or_no'))
async def yes_or_no(message: Message):
    data = get_yesorno()
    await message.answer_video(video = data['image'], caption = data['answer'].capitalize())


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())