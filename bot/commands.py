import os
from script import Script
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(filters.command(["start"]) & filters.private)
async def event(bot, update):
    await update.reply_text(
        text=Script.START_TEXT.format(update.from_user.mention),
        disable_web_page_preview=True,
        reply_markup=Script.START_BUTTONS
    )
async def up(event):
    stt = dt.now()
    ed = dt.now()
    v = ts(int((ed - uptime).seconds) * 1000)
    ms = (ed - stt).microseconds / 1000
    p = f"Ping = {ms}ms"
    await event.reply(v + "\n" + p)
