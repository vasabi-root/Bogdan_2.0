import logging
from telegram import (
    Update, ReplyKeyboardMarkup, 
    InlineKeyboardMarkup, InlineKeyboardButton
)
from telegram.ext import ContextTypes, ConversationHandler
import random

from config import (
    GET_CHANCE_TEXT, SET_CHANCE_TEXT,
    CACHE, CHANCE, DEFAULT_CACHE
)

'''
TODO
плохо, что для каждого хэндлера надо проверять, есть ли вообще запись о пользователе в БД (на данный момент, в кэше)
т.е. надо переписать так, чтоб не было постоянного повтора строки CACHE.setdefault(chat.id, DEFAULT_CACHE)
в идеале, надо навесить эту строку на событие первого использования бота в чате (но это не обязательно /start)
Надо доки парсить
'''

async def get_chance(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat = update.effective_chat
    CACHE.setdefault(chat.id, DEFAULT_CACHE)
    await update.message.reply_text(GET_CHANCE_TEXT + f'{CACHE[chat.id][CHANCE]}%')

async def set_chance(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat = update.effective_chat
    CACHE.setdefault(chat.id, DEFAULT_CACHE)

    try:
        value = int(update.message.text.split('/chance')[1])
        CACHE[chat.id][CHANCE] = value
        logging.info(f'for chat.id: [{chat.id}] chance set {value}')
    except:
        pass
    await update.message.reply_text(SET_CHANCE_TEXT + f'{CACHE[chat.id][CHANCE]}%')


async def answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat = update.effective_chat
    CACHE.setdefault(chat.id, DEFAULT_CACHE)
    if random.randint(1, 100) <= CACHE[chat.id][CHANCE]:
        ans = gen_bullying(update.message.text)
        await update.message.reply_text(ans)

def gen_bullying(msg: str) -> str:
    '''
    TODO: работа с Gliff.app API 
    '''    
    return 'some bullying'