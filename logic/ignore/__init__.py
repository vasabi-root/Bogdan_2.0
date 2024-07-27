import asyncio
from telegram import Bot, Update
import logging

async def clear_updates(bot: Bot):
    # unconfirmed get
    updates = await bot.get_updates()
    logging.info(f"Found {len(updates)} updates to be removed")
    
    if updates:
        update_ids = [update.update_id for update in updates]
        highest_update_id = max(update_ids)
        # confirmed get
        bot.get_updates(offset=highest_update_id + 1)
        logging.info("Updates cleared")