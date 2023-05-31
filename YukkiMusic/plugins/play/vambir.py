import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)


@app.on_message(
     command(["مبرمج السورس","فايدر","المبرمج"])
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/09d895269ebd1fce23537.jpg",
caption=f"""✧ الزرار الاول -> قناه السورس \n✧ الزرار الثاني -> هو مبرمج السورس""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                InlineKeyboardButton(
                    "𓆩𝚂𝙾𝚄𝚁𝙲𝙴 𝙵𝙰𝙸𝙳𝙴𝚁𓆪", url=f"https://t.me/FR_TW048"
                ),
                ],
                [
                    InlineKeyboardButton(
                        "فا يـ د ر حـِْـٰــ۫͜ ــزًيــ۫͜ ـن 𓆩🖤🥀𓆪", url=f"https://t.me/VV_338"),
                ],
            ]
        ),
    )
    