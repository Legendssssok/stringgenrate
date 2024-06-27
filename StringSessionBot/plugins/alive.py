from platform import python_version as y

#from pyrogram1 import __version__ as oldpyrover
from pyrogram import Client
from pyrogram import __version__ as pyrover
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup

from LegendSS.Data import Data


@Client.on_message(filters.private & filters.incoming & filters.command("alive"))
async def alivr(bot, msg):
    await bot.send_photo(
        msg.chat.id,
        photo="https://graph.org/file/c64df54687a3dcc00ab25.jpg",
        caption=f"""
┏•❅────✧❅✦❅✧────❅•┓
ㅤ★ **Python :** `{y()}`
ㅤ★ **Oldpyro :** `{oldpyrover}`
  ★ **Pyrogram :** `{pyrover}`
┗•❅────✧❅✦❅✧────❅•┛""",
        reply_markup=InlineKeyboardMarkup(Data.home_buttons),
    )
