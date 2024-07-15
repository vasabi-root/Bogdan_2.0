from telegram.ext import CommandHandler, filters, MessageHandler

from logic.ignore.callbacks import unknown

unknown_handler = MessageHandler(filters=filters.COMMAND, callback=unknown)
