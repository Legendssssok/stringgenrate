from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup

from LegendSS.Data import Data


# Help Message
@Client.on_message(filters.private & filters.incoming & filters.command("help"))
async def _help(bot, msg):
    await bot.send_message(
        msg.chat.id,
        "**Help related on how to use me...**\n" + Data.HELP,
        reply_markup=InlineKeyboardMarkup(Data.home_buttons),
    )
