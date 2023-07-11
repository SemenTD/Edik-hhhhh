import asyncio  # Работа с асинхронностью

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command  # Фильтр для /start, /...
from aiogram.types import Message , ContentType  # Тип сообщения

from config import config  # Config

API_TOKEN = config.token

bot = Bot(token=API_TOKEN)
dp = Dispatcher()  # Менеджер бота


# dp.message - обработка сообщений
# Command(commands=['start'] Фильтр для сообщений, берём только /start
@dp.message(Command(commands=['start']))  # Берём только сообщения, являющиеся командой /start
async def start_command(message: Message):  # message - сообщение, которое прошло через фильтр
    await message.answer("Привет!")  # Отвечаем на полученное сообщени

# @dp.message(F.content_type == ContentType.PHOTO)
# async def echo_photo(message:Message):
#     await message.answer_photo(message.photo[0].file_id)
#
#
# @dp.message(F.content_type == ContentType.STICKER)
# async def echo_stiker (message:Message):
#     await message.answer_sticker(message.sticker.file_id)
#
# @dp.message(F.content_type == ContentType.VOICE)
# async def echo_voice (message:Message):
#     await message.answer_voice(message.voice.file_id)

@dp.message()
async def echo_all(message:Message):
    await message.send_copy(message.chat.id)

async def main():
    try:
        print('Bot Started')
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':  # Если мы запускаем конкретно этот файл.
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print('Bot stopped')
