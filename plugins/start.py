import asyncio
from time import time
from datetime import datetime
from modules.config import BOT_USERNAME
from modules.helpers.filters import command
from modules.helpers.command import commandpro
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)
    
   

@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/6e45ac5a575c28e248572.jpg",
        caption=f"""**━━━━━━━━━━━━━━━━━
ʜᴇʟʟᴏ, ɪ ᴀᴍ sᴜᴘᴇʀ ғᴀsᴛ ᴀɴᴅ ɴᴇxᴛ ɢᴇɴᴇʀᴀᴛɪᴏɴ ᴠᴄ ᴘʟᴀʏᴇʀ
ʙᴏᴛ ᴀɴᴅ ɴᴏ ʟᴀɢ ɪssᴜᴇ ᴡɪᴛʜ ʙᴇsᴛ sᴏᴜɴᴅ ǫᴜᴀʟɪᴛʏ ғᴏʀ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘs
ɪғ ʏᴏᴜ ʜᴀᴠᴇ ᴀɴʏ ǫᴜᴇsᴛɪᴏɴs ᴛʜᴇɴ
ᴅᴍ ᴛᴏ ᴍʏ ᴏᴡɴᴇʀ [sᴜᴍɪᴛ ʏᴀᴅᴀᴠ](https://t.me/Mr_DiSasTer_XD)...
━━━━━━━━━━━━━━━━━━━**""",
    reply_markup=InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
            InlineKeyboardButton("👥 sᴜᴘᴘᴏʀᴛ", url="https://t.me/TechQuardSupport"),
            InlineKeyboardButton("📣 ᴜᴘᴅᴀᴛᴇs", url="https://t.me/TechQuard")
        ],
        [
            InlineKeyboardButton("🧰 ᴄᴏᴍᴍᴀɴᴅs", url="https://telegra.ph/%F0%9D%99%B2%E1%B4%8F%E1%B4%8D%E1%B4%8D%E1%B4%80%C9%B4%E1%B4%85s-04-06"),
            InlineKeyboardButton("⚕️ ᴍᴏʀᴇ ɪɴғᴏ", callback_data="moreinfo")
        ]
   
     ]
  ),
)
    
    
@Client.on_message(commandpro(["/start", "/alive", "/repo"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/6e45ac5a575c28e248572.jpg",
        caption=f"""ʏᴏᴜ ᴋɴᴏᴡ ɪ ᴀᴍ ғᴀsᴛ ᴍᴜsɪᴄ ʙᴏᴛ ᴀɴᴅ ɴᴏ ʟᴀɢ ɪssᴜᴇ ᴡɪᴛʜ ʙᴇsᴛ sᴏᴜɴᴅ ǫᴜᴀʟɪᴛʏ ғᴏʀ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘs. """,
        reply_markup=InlineKeyboardMarkup(
             [
            [
                InlineKeyboardButton(text="👥 ꜱᴜᴘᴘᴏʀᴛ", url=f"https://t.me/TechQuardSupport"),
                InlineKeyboardButton(text="📣 ᴄʜᴀɴɴᴇʟ", url=f"https://t.me/TechQuard"),
            ]
        ]
     ),
  ) 

@Client.on_message(command(["ping"]) & ~filters.edited)
async def ping_pong(client: Client, message: Message):
    start = time()
    sumit = await message.reply_photo(
    photo=f"DARK_IMG",
        caption=" ᴩɪɴɢɪɴɢ...",
    delta_ping = time() - start
    await sumit.edit_text(
    f"ᴘ ᴏ ɴ ɢ ! \n" f"`{delta_ping * 1000:.3f} ᴍs`")

