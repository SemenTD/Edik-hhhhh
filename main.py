import asyncio
from aiogram import Bot, Dispatcher

from aiogram.filters import Command, Text
from aiogram.types import Message

from config import config

API_TOKEN = config.token

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Text(text='blue lock'))
async def easter_egg(message:Message):
    await message.answer("blue lock = №1 ")

@dp.message(Text(text='rust'))
async def easter_egg(message:Message):
    await message.answer("rust>game world")

@dp.message(Command(commands=["start"]))
async def start_command(message: Message):
    await message.answer("Привет!")


async def main():
    try:
        print("Bot Started")
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("Bot stopped")

@dp.message(Text(text='rust'))
async def easter_egg(message:Message):
    await message.answer("rust>game world")