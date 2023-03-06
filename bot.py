import os
import logging
import time

from aiogram import Bot, Dispatcher, executor, types

TOKEN = os.getenv('TOKEN')

logging.basicConfig(level=logging.INFO, filename='bot_log.log', filemode='a',
                    format="%(asctime)s %(levelname)s %(message)s")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def answer_start_command(message: types.Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    logging.info(f'{user_name=}, {user_id=} sent message: {message.text}')
    await message.answer(f'Привет, {user_name}!')
    await message.answer(f'Братик или сестричка, я помогу тебе перевести ФИО на кирилице в латиницу!\nДавай свое ФИО!')

@dp.message_handler()
async def help_translit(message: types.Message):
    
    dict = {'А':'A', 'Б':'B', 'В':'V', 'Г':'G', 'Д':'D', 'Е':'E', 'Ё':'E', 'Ж':'ZH', 'З':'Z', 'И':'I', 'Й':'I', 'К':'K', 
            'Л':'L', 'М':'M', 'Н':'N', 'О':'O', 'П':'P', 'Р':'R', 'С':'S', 'Т':'T', 'У':'U', 'Ф':'F', 'Х':'KH', 'Ц':'TS',
            'Ч':'CH', 'Ш':'SH', 'Щ':'SHCH', 'Ъ':'IE', 'Ы':'Y', 'Ь' : '', 'Э':'E', 'Ю':'IU', 'Я':'IA'}
    
    translit_text_result = ''
    for char in message.text:
        if char.upper() in dict.keys():
            translit_text_result += dict[char.upper()]
        else:
            translit_text_result += char
    
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    logging.info(f'{user_name=}, {user_id=} sent message: {message.text} answer: {translit_text_result}')
    
    await message.reply(translit_text_result)

if __name__ == '__main__':
    executor.start_polling(dp)