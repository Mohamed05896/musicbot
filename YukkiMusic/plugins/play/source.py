import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from typing import Union
from pyrogram.types import InlineKeyboardButton

from config import GITHUB_REPO, SUPPORT_CHANNEL, SUPPORT_GROUP
from YukkiMusic import app
from config import BANNED_USERS, MUSIC_BOT_NAME

import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

BOT_USERNAME = getenv("BOT_USERNAME")

IMG_DEV1 = getenv("IMG_DEV1")

OWNER = getenv("OWNER")

OWNER_NAME = getenv("OWNER_NAME")

@app.on_message(
    command(["سورس ايطالي","سورس","السورس","يا سورس"])
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/09d895269ebd1fce23537.jpg",
        caption=f"""[⌁ 𝚆𝙴𝙻𝙲𝙾𝙼𝙴 𝙼𝚄𝚂𝙸𝙲 𝙵𝙰𝙸𝙳𝙴𝚁 🎸](https://t.me/VV_338)\n\n[⌁ 𝙳𝙴𝚅 𝙶𝚁𝙾𝚄𝙿 𝙵𝙰𝙸𝙳𝙴𝚁 🎸](https://t.me/FR_TW047)\n\n[⌁ 𝙳𝙴𝚅 𝚂𝙾𝚄𝚁𝙲𝙴 𝙵𝙰𝙸𝙳𝙴𝚁 🎸](https://t.me/FR_TW048)
— — — — — — — — —
𖥔 Dev User : @{OWNER}""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ՏøuƦcε 𝒇αιძεƦ", url=f"https://t.me/FR_TW048"), 
                ],[
                    InlineKeyboardButton(
                        "ՏøuƦcε 𝒇αιძεƦ", url=f"https://t.me/FR_TW048"),
                ],[
                    InlineKeyboardButton(
                        "أضغط لاضافه ألبوت لمجموعتك 𖣳", url=f"https://t.me/Ma_rly_bot?startgroup=true"),
                ],

            ]

        ),

    )
