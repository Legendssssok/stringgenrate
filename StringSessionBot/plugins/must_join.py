from pyrogram import Client, filters
from StringSessionBot.Config import MUST_JOIN, AUTH_USERS
from pyrogram.types import Message
from pyrogram.errors import UserNotParticipant, ChatWriteForbidden, ChatAdminRequired
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channel(bot: Client, msg: Message):
    if not MUST_JOIN:  # Not compulsory
        return
    try:
        try:
            await bot.get_chat_member(MUST_JOIN, msg.from_user.id)
        except UserNotParticipant:
            if MUST_JOIN.isalpha():
                link = "https://t.me/" + MUST_JOIN
            else:
                chat_info = await bot.get_chat(MUST_JOIN)
                link = chat_info.invite_link
            try:
                await msg.reply_photo(
                    photo="https://graph.org/file/c64df54687a3dcc00ab25.jpg",
                    caption="You must join [this channel]({link}) to use me. After joining try again !",
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton("✨ Join Channel ✨", url=link)]
                    ])
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        await msg.reply_text(f"I'm not admin in the MUST_JOIN chat : {MUST_JOIN} !")
    if msg.from_user.id in AUTH_USERS:
        return
    else:
        await msg.reply_photo(
            photo="https://graph.org/file/c64df54687a3dcc00ab25.jpg",
            caption="**You are not authorised Member**\n\nYou Have to Buy Plan to Use Me\n➢ **Check Our Plan**\n• 1 Refill = 10 Rs\n• 10 Refill = 90 Rs\n\n**Click Below 👇 and Contact Owner**\n• Repo is also for sell Advanced Repo\n__Time Pass Go Away__", 
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("✨ Owner ✨", url="https://t.me/LegendBoy_OP")]
            ])
        )
        await msg.stop_propagation()
