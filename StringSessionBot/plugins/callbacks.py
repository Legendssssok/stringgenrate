from pyrogram import Client
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

from LegendSS.Data import Data
from LegendSS.generate import ERROR_MESSAGE, generate_session


@Client.on_callback_query()
async def _callbacks(bot: Client, callback_query: CallbackQuery):
    user = await bot.get_me()
    mention = user.mention
    query = callback_query.data.lower()
    if query.startswith("home"):
        if query == "home":
            chat_id = callback_query.from_user.id
            message_id = callback_query.message.id
            await bot.edit_message_text(
                chat_id=chat_id,
                message_id=message_id,
                text=Data.START.format(callback_query.from_user.mention, mention),
                reply_markup=InlineKeyboardMarkup(Data.buttons),
            )
    elif query == "about":
        chat_id = callback_query.from_user.id
        message_id = callback_query.message.id
        await bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text=Data.ABOUT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(Data.home_buttons),
        )
    elif query == "help":
        chat_id = callback_query.from_user.id
        message_id = callback_query.message.id
        await bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text="**Help related on how to use me...**\n" + Data.HELP,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(Data.home_buttons),
        )
    elif query == "generate":
        await callback_query.message.reply(
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
    elif query in ["pyrogramv1", "pyrogramv2", "telethon", "hellbot"]:
        await callback_query.answer()
        try:
            if query == "pyrogramv2":
                await generate_session(bot, callback_query.message)
            elif query == "pyrogramv1":
                await generate_session(bot, callback_query.message, old_pyro=True)
            elif query == "telethon":
                await generate_session(bot, callback_query.message, telethon=True)
            else:
                await generate_session(bot, callback_query.message, hellbot=True)
        except Exception as e:
            await callback_query.message.reply(ERROR_MESSAGE.format(str(e)))
