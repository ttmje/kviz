# Бот телеграмм
import asyncio
import general
import keyboards as kb
from db import Database
import config
import logging
from aiogram import Bot, Dispatcher, executor, types

# инициализируем соединение с БД
db = Database()

# Задаем уровень логов
logging.basicConfig(level=logging.INFO)

# Инициализируем бота
bot = Bot(token=config.API_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)

# Обработка команды /start
@dp.message_handler(commands=["start"])
async def start_bot(message: types.Message):
    await bot.send_message(message.chat.id,
                           f"Привет! \nЭто БОТ-помошник Квизлет."
                           f"\nСейчас в моей базе уже {''.join(map(str,db.get_count()))} слов!")
    await message.reply('Начинаем изучать слова?', reply_markup=kb.inline_kb1)


# Обработка команды /help
@dp.message_handler(commands=["help"])
async def start_bot(message: types.Message):
    await bot.send_message(message.chat.id, f"Привет! \nЭто БОТ-помошник Квизлет.")

# Обработка команды /help
@dp.message_handler(commands=["add_word"])
async def start_bot(message: types.Message):
    await bot.send_message(message.chat.id, 'Введите слово: ')
    word = message.text
    await bot.send_message(message.chat.id, 'Введите перевод: ')
    #db.add_word(word,translate) #работает


# запускеаем лонг поллинг
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)