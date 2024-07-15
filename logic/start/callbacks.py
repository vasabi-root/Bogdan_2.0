from telegram import (
    Update, ReplyKeyboardMarkup, 
    InlineKeyboardMarkup, InlineKeyboardButton
)
from telegram.ext import ContextTypes, ConversationHandler

from config import START_TEXT, CANCEL_TEXT, CACHE, CHANCE, DEFAULT_CACHE


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat = update.effective_chat
    CACHE.setdefault(chat.id, DEFAULT_CACHE)
    await update.message.reply_markdown(START_TEXT)


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    chat = update.effective_chat
    CACHE.setdefault(chat.id, DEFAULT_CACHE)
    CACHE[chat.id][CHANCE] = 0
    await update.message.reply_text(CANCEL_TEXT)
    return ConversationHandler.END
