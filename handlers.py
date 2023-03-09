import logging
import time

from aiogram.types import Message, ContentType
from aiogram.types import PreCheckoutQuery, LabeledPrice
from aiogram.dispatcher.filters import Command

from main import bot, dp
from keyboards import keyboard
PAYMENTS_TOKEN = 0


@dp.message_handler(Command('start'))
async def start(message: Message):
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name
    logging.info(f'{user_id=} {user_full_name} {time.asctime()}')
    await bot.send_message(message.chat.id,
                           f'\tHellow {user_full_name}!, Ton Converter Bot can convert the following types of files: '
                           f'.docx,.pdf,.doc,.jpg,.jpeg,.gif,.png,.bmp,.svg,.tiff,.htm,.html,.docm,.dotx,.dot,.md,.rtf,'
                           f'.odt,.ott,.txt,.mobi,.mht,.mhtml,.xht,.xhtml,.chm,.zip,.rar,.7z,.tar,.tar.gz,.wps,.wpt\n\n'
                           f'\tHow to use?\n'
                           f'1. You can simply send the file to the bot in a message and choose the needed format.\n'
                           f'2. You can tab the menu button.\n',
                           reply_markup=keyboard)


@bot.message_handler(content_types=['photo', 'document'])
async def send_file(message):
    try:
        await bot.send_message(message.chat.id, bot.get_file_url(message.document.file_id))
    except AttributeError:
        try:
            await bot.send_message(message.chat.id, bot.get_file_url(message.photo[0].file_id))
        except AttributeError:
            await bot.send_message(message.chat.id, f'Format of your file is incorrect...', reply_markup=keyboard)
