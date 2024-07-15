from telegram import Update
from telegram.ext import ContextTypes
from config import UNKNOWN_TEXT

async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_markdown(text=UNKNOWN_TEXT)