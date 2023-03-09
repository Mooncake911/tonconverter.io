import asyncio
from aiogram import Bot, Dispatcher, executor

BOT_TOKEN = '6205743629:AAE9Ua6tRqC_O21S731o-8vov8AwlQ86s4w'

loop = asyncio.new_event_loop()
bot = Bot(BOT_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot, loop)

if __name__ == '__main__':
    from handlers import dp
    executor.start_polling(dp)
