from config import bot_token, ju_weather
import requests
from aiogram import types, Bot, Dispatcher
from aiogram.utils import executor

bot = Bot(token=bot_token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply('Привет! Введи название города')


@dp.message_handler()
async def get_weather(message: types.Message):
    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={ju_weather}&units=metric")
        data = r.json()
        # pprint(data)
        city = data['name']
        cur_temp = data['main']['temp']
        humid = data['main']['humidity']
        pres = data['main']['pressure'] * 0.75
        descript = data['weather'][0]['description']
        wind = data['wind']['speed']
        await message.reply(
            f"Погода в {city}:\nТемпература: {cur_temp}\nВлажность: {humid}\nДавление: {pres}\nОписание: {descript}\nВетер: {wind}")
        await message.reply()

    except Exception:
        pass


if __name__ == '__main__':
    executor.start_polling(dp)
