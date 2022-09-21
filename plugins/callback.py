from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from modules.config import BOT_USERNAME

HELP_TEXT = """
ʜᴇʟʟᴏ [{}](tg://user?id={})
ɪ ᴀᴍ sᴜᴘᴇʀ ғᴀsᴛ ɴᴇxᴛ ɢᴇɴᴇʀᴀᴛɪᴏɴ ᴠᴄ ᴘʟᴀʏᴇʀ ʙᴏᴛ ᴀɴᴅ ɴᴏ ʟᴀɢ ɪssᴜᴇ ᴡɪᴛʜ ʙᴇsᴛ sᴏᴜɴᴅ ǫᴜᴀʟɪᴛʏ ғᴏʀ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘs
ɪғ ʏᴏᴜ ʜᴀᴠᴇ ᴀɴʏ ǫᴜᴇsᴛɪᴏɴs ᴛʜᴇɴ
ᴅᴍ ᴛᴏ ᴍʏ ᴏᴡɴᴇʀ [sᴜᴍɪᴛ ʏᴀᴅᴀᴠ](https://t.me/Mr_DiSasTer_XD)...
━━━━━━━━━━━━━━━━━━━**"""


@Client.on_callback_query(filters.regex("home"))
async def home(_, query: CallbackQuery):
    await query.edit_message_text(f"{HELP_TEXT}".format(query.message.chat.first_name, query.message.chat.id),
    reply_markup=InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
            InlineKeyboardButton("🍄 sᴜᴘᴘᴏʀᴛ", url="https://t.me/TechQuardSupport"),
            InlineKeyboardButton("📣 ᴜᴘᴅᴀᴛᴇs", url="https://t.me/TechQuard")
        ],
        [
            InlineKeyboardButton("🧰 ᴄᴏᴍᴍᴀɴᴅs", url="https://telegra.ph/%F0%9D%99%B2%E1%B4%8F%E1%B4%8D%E1%B4%8D%E1%B4%80%C9%B4%E1%B4%85s-04-06"),
            InlineKeyboardButton("⚕️ ᴍᴏʀᴇ ɪɴғᴏ", callback_data="moreinfo")
        ]
   
     ]
  ),
)






@Client.on_callback_query(filters.regex("moreinfo"))
async def others(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""ʜᴇʏᴀ [{query.message.chat.first_name}](tg://user?id={query.message.chat.id})

ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ɢɪᴠᴇɴ ʙᴇʟᴏᴡ ᴛᴏ ᴋɴᴏᴡ ᴍᴏʀᴇ ᴀʙᴏᴜᴛ ᴍᴇ :""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🗯️ ꜱᴜᴘᴘᴏʀᴛ", url=f"https://t.me/TechQuardSupport"),
                    InlineKeyboardButton(
                        "🌐 ᴜᴘᴅᴀᴛᴇꜱ", url=f"https://t.me/TechQuard")
                ],
                [
                    InlineKeyboardButton(
                        "🍄 ᴍᴀɪɴᴛᴀɪɴᴇʀ", url="https://t.me/Mr_Disaster_Xd"),
                    InlineKeyboardButton(
                        "🍀 ᴏᴛʜᴇʀ ɪɴғᴏ", callback_data="repoinfo")
                ],
                [
                    InlineKeyboardButton("◁", callback_data="home")
                ]
           ]
        ),
    )



@Client.on_callback_query(filters.regex("cls"))
async def reinfo(_, query: CallbackQuery):
    try:
        await query.message.delete()
        await query.message.reply_to_message.delete()
    except Exception:
        pass


@Client.on_callback_query(filters.regex("repoinfo"))
async def repoinfo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""ʜᴇʀᴇ ᴀʙᴏᴜᴛ ᴛʜᴇ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ : 
ᴀɴᴅ ʙᴏᴛ ʟɪsᴛs ᴀɴᴅ ᴘʟᴇᴀsᴇ ᴊᴏɪɴ ᴏᴜʀ ᴍᴀɪɴ ᴄʜᴀɴɴᴇʟ ᴏʀ ʏᴏᴜᴛᴜʙᴇ ᴄʜᴀɴɴᴇʟ.
ᴛʜɪs ʀᴇᴘᴏ ɪs ᴏɴʟʏ ᴍᴀᴅᴇ ғᴏʀ ᴅᴇᴘʟᴏʏɪɴɢ ᴀ ᴘᴏᴡᴇʀғᴜʟ ᴍᴜsɪᴄ ʙᴏᴛ ᴏɴ ʜᴇʀᴏᴋᴜ ᴡɪᴛʜᴏᴜᴛ ғᴀᴄɪɴɢ ʜᴇʀᴏᴋᴜ ᴀᴄᴄᴏᴜɴᴛ ʙᴀɴɴɪɴɢ ᴘʀᴏʙᴇʟᴍ.

""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔗 ɢɪᴛʜᴜʙ", url=f"https://github.com/Sumit9969/DarkxMusic"),
                    InlineKeyboardButton(
                        "💌 ʏᴏᴜᴛᴜʙᴇ", url=f"https://youtube.com/channel/UCtI7hbY-BD7wvuIzoSU0cEw")
                ],
                [
                    InlineKeyboardButton(
                        "👾 ʙᴏᴛ ʟɪsᴛs", url="https://t.me/TechQuardBot"),
                    InlineKeyboardButton(
                        "🤤 ᴘᴏʀɴ ʜᴜʙ", url="http://t.me/TheNudesHubBot")
                ],
                [
                    InlineKeyboardButton("◁", callback_data="moreinfo")
                ]
           ]
        ),
     )
    
        
