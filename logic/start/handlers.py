from telegram.ext import CommandHandler, MessageHandler, filters

from logic.start.callbacks import start, cancel


start_handler = CommandHandler('start', start)
cancel_handler = CommandHandler('cancel', cancel)
