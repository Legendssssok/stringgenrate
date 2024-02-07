import asyncio
import importlib
from pyromod import listen
from pyrogram import Client, idle
from pyrogram.errors import FloodWait

from StringSessionBot.Config import API_HASH, API_ID, BOT_TOKEN
from StringSessionBot.database.token_users import add_tokenusers, get_tokenusers
from StringSessionBot.plugins import ALL_MODULES

from .logger import LOGS

add_tokenusers(BOT_TOKEN)

bot_token = get_tokenusers()
print(bot_token)


async def Start_Bot():
    for i in range(len(bot_token)):
        try:
            app = Client(
                "app",
                api_id=API_ID,
                api_hash=API_HASH,
                bot_token=bot_token[i],
                plugins=dict(root="StringSessionBot/plugins"),
            )
            await app.start()
        except FloodWait as e:
            LOGS.error(f"Bot Wants to Sleep For {e.value}")
            await asyncio.sleep(e.value + 5)
        except Exception as f:
            LOGS.error(f)
        for all_module in ALL_MODULES:
            importlib.import_module("StringSessionBot.plugins." + all_module)
            LOGS.info(f"➢ Successfully Imported : {all_module}")
        LOGS.info("==============================")
        LOGS.info("🔰Support Group🔰 : @LegendBot_OP")
        LOGS.info("⚜️Update Group⚜️  : @LegendBot_AI")
        LOGS.info("==============================")
        await idle()
