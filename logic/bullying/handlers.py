from telegram.ext import CommandHandler, MessageHandler, filters

from logic.bullying.callbacks import answer, set_chance, get_chance


msg_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), answer)
get_chance_handler = CommandHandler('chance', get_chance)
set_chance_handler = MessageHandler(filters.Regex('\/chance(\d{1,2}|100)$'), set_chance)
