import logging
from telegram.ext import ApplicationBuilder, CallbackQueryHandler

from logic.ignore import clear_updates
from logic.ignore.handlers import unknown_handler
from logic.start import run_polling
from logic.start.handlers import start_handler, cancel_handler
from logic.bullying.handlers import get_chance_handler, set_chance_handler, msg_handler
import asyncio

from config.keys import TOKEN

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

def main():
    application = ApplicationBuilder().token(TOKEN).build()
    # await clear_updates(application.bot)
    
    application.add_handler(start_handler)
    application.add_handler(cancel_handler)
    
    application.add_handler(get_chance_handler)
    application.add_handler(set_chance_handler)
    application.add_handler(msg_handler)
    
    application.add_handler(unknown_handler)
    application.run_polling(
        drop_pending_updates=True,
    )
    
    # await run_polling(application)

if __name__ == '__main__':
    # asyncio.run(main())
    main()
