import asyncio
from telegram.ext import Application, Updater

async def finalize(app: Application):
    await app.updater.stop()
    await app.stop()
    await app.shutdown()
    await app.post_shutdown()
    

async def run_polling(app: Application):
    try:
        await app.initialize()
        await app.post_init()
        await app.updater.start_polling()
        await app.start() 
    finally:
        await finalize(app)
    

    
    
    