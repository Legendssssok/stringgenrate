from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

@Client.on_message(filters.private & ~filters.forwarded & filters.command("generate"))
async def main(_, msg):
    await msg.reply(
        "Please choose the python library you want to generate string session for",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Pyrogram V1", callback_data="pyrogramv1"),
                    InlineKeyboardButton("Pyrogram V2", callback_data="pyrogramv2"),
                ],
                [
                    InlineKeyboardButton("Telethon", callback_data="telethon"),
                    InlineKeyboardButton("HellBot", callback_data="hellbot"),
                ],
            ]
        ),
    )
