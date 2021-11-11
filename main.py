import logging
import asyncio
from aiogram import Bot, Dispatcher, executor, types, utils
from aiogram.types import ParseMode
from config import URL, TOKET

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKET, parse_mode=ParseMode.HTML)
dp = Dispatcher(bot)

@dp.message_handler(commands='list')
async def send_list(message: types.Message):
    message_text = 'Строка поиска {}'.format('line search')
    await message.answer(text=message_text)


@dp.message_handler(commands='search')
async def send_search(message: types.Message):
    message_text = 'Слова поиса {}'.format('Words search!!')
    await message.answer(text=message_text)


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(text=message.text)

async def scheduled(wait_for, parser):
    while True:
        await asyncio.sleep(wait_for)
        print('Parse')
        pass

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(scheduled(10, None))
    executor.start_polling(dp, skip_updates=True)
