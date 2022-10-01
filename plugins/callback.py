import asyncio
from pyrogram import filters
from pyrogram.types import Message
from pyrogram import Client
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from modules.config import BOT_USERNAME
from pyrogram.errors import MessageNotModified

HOME_TEXT = """
ʜᴇʟʟᴏ [{}](tg://user?id={})
ɪ ᴀᴍ sᴜᴘᴇʀ ғᴀsᴛ ɴᴇxᴛ ɢᴇɴᴇʀᴀᴛɪᴏɴ ᴠᴄ ᴘʟᴀʏᴇʀ ʙᴏᴛ ᴀɴᴅ ɴᴏ ʟᴀɢ ɪssᴜᴇ ᴡɪᴛʜ ʙᴇsᴛ sᴏᴜɴᴅ ǫᴜᴀʟɪᴛʏ ғᴏʀ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘs
ɪғ ʏᴏᴜ ʜᴀᴠᴇ ᴀɴʏ ǫᴜᴇsᴛɪᴏɴs ᴛʜᴇɴ
ᴅᴍ ᴛᴏ ᴍʏ ᴏᴡɴᴇʀ [sᴜᴍɪᴛ ʏᴀᴅᴀᴠ](https://t.me/Mr_DiSasTer_XD)...
━━━━━━━━━━━━━━━━━━━**"""

SUDO_CMD = """
🌾 **sᴜᴅᴏ ᴄᴏᴍᴍᴀɴᴅs :**
๏ /gcast : ʙʀᴏᴀᴅᴄᴀsᴛ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ sᴇʀᴠᴇᴅ ᴄʜᴀᴛs ᴏғ ᴛʜᴇ ʙᴏᴛ.
๏ /eval or /sh : ʀᴜɴs ᴛʜᴇ ɢɪᴠᴇɴ ᴄᴏᴅᴇ ᴏɴ ᴛʜᴇ ʙᴏᴛ's ᴛᴇʀᴍɪɴᴀʟ.
๏ /rmw : ᴄʟᴇᴀʀs ᴀʟʟ ᴛʜᴇ ᴄᴀᴄʜᴇ ᴩʜᴏᴛᴏs ᴏɴ ᴛʜᴇ ʙᴏᴛ's sᴇʀᴠᴇʀ.
๏ /rmp : ᴄʟᴇᴀʀs ᴛʜᴇ ʀᴀᴡ ғɪʟᴇs ᴏғ ᴛʜᴇ ʙᴏᴛ.
๏ /rmd : ᴄʟᴇᴀʀs ᴛʜᴇ ᴅᴏᴡɴʟᴏᴀᴅᴇᴅ ғɪʟᴇs ᴏɴ ᴛʜᴇ ʙᴏᴛ's sᴇʀᴠᴇʀ.""",

"""





#USERS_CMD = """



MORE_TEXT = """
ʜᴇʀᴇ ᴀʙᴏᴜᴛ ᴛʜᴇ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ : 
ᴀɴᴅ ʙᴏᴛ ʟɪsᴛs ᴀɴᴅ ᴘʟᴇᴀsᴇ ᴊᴏɪɴ ᴏᴜʀ ᴍᴀɪɴ ᴄʜᴀɴɴᴇʟ ᴏʀ ʏᴏᴜᴛᴜʙᴇ ᴄʜᴀɴɴᴇʟ.
ᴛʜɪs ʀᴇᴘᴏ ɪs ᴏɴʟʏ ᴍᴀᴅᴇ ғᴏʀ ᴅᴇᴘʟᴏʏɪɴɢ ᴀ ᴘᴏᴡᴇʀғᴜʟ ᴍᴜsɪᴄ ʙᴏᴛ ᴏɴ ʜᴇʀᴏᴋᴜ ᴡɪᴛʜᴏᴜᴛ ғᴀᴄɪɴɢ ʜᴇʀᴏᴋᴜ ᴀᴄᴄᴏᴜɴᴛ ʙᴀɴɴɪɴɢ ᴘʀᴏʙᴇʟᴍ.

"""

USERS_CMD = """ᴀᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅs ɪɴ ᴍᴜsɪᴄ ʙᴏᴛ :
๏ /play : sᴛᴀʀᴛs sᴛʀᴇᴀᴍɪɴɢ ᴛʜᴇ ʀᴇǫᴜᴇsᴛᴇᴅ ᴛʀᴀᴄᴋ ᴏɴ ᴠɪᴅᴇᴏᴄʜᴀᴛ.
๏ /pause : ᴩᴀᴜsᴇ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴩʟᴀʏɪɴɢ sᴛʀᴇᴀᴍ.
๏ /resume : ʀᴇsᴜᴍᴇ ᴛʜᴇ ᴩᴀᴜsᴇᴅ sᴛʀᴇᴀᴍ.
๏ /skip : sᴋɪᴩ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴩʟᴀʏɪɴɢ sᴛʀᴇᴀᴍ ᴀɴᴅ sᴛᴀʀᴛ sᴛʀᴇᴀᴍɪɴɢ ᴛʜᴇ ɴᴇxᴛ ᴛʀᴀᴄᴋ ɪɴ ǫᴜᴇᴜᴇ.
๏ /end : ᴄʟᴇᴀʀs ᴛʜᴇ ǫᴜᴇᴜᴇ ᴀɴᴅ ᴇɴᴅ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴩʟᴀʏɪɴɢ sᴛʀᴇᴀᴍ.
๏ /ping : sʜᴏᴡ ᴛʜᴇ ᴩɪɴɢ ᴀɴᴅ sʏsᴛᴇᴍ sᴛᴀᴛs ᴏғ ᴛʜᴇ ʙᴏᴛ.
๏ /join : ʀᴇǫᴜᴇsᴛ ᴛʜᴇ ᴀssɪsᴛᴀɴᴛ ᴛᴏ ᴊᴏɪɴ ʏᴏᴜʀ ᴄʜᴀᴛ.
๏ /id : sᴇɴᴅs ʏᴏᴜ ᴛʜᴇ ɪᴅ ᴏғ ᴛʜᴇ ᴜsᴇʀ ᴏʀ ʀᴇᴩʟɪᴇᴅ ғɪʟᴇ.
๏ /song : ᴅᴏᴡɴʟᴏᴀᴅs ᴛʜᴇ ʀᴇǫᴜᴇsᴛᴇᴅ sᴏɴɢ ᴀɴᴅ sᴇɴᴅ ɪᴛ ᴛᴏ ʏᴏᴜ.
๏ /search : sᴇᴀʀᴄᴇs ᴛʜᴇ ɢɪᴠᴇɴ ǫᴜᴇʀʏ ᴏɴ ʏᴏᴜᴛᴜʙᴇ ᴀɴᴅ sʜᴏᴡs ʏᴏᴜ ᴛʜᴇ ʀᴇsᴜʟᴛ.

"""

@Client.on_callback_query()
async def cb_handler(client: Client, query: CallbackQuery):
    if query.data=="home":
        buttons = [
        [
            InlineKeyboardButton("➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
            InlineKeyboardButton("🛟 sᴜᴘᴘᴏʀᴛ", url="https://t.me/TheSupportBots"),
            InlineKeyboardButton("🌾 ᴜᴘᴅᴀᴛᴇs", url="https://t.me/TechQuard")
        ],
        [
            InlineKeyboardButton("🧰 ᴄᴏᴍᴍᴀɴᴅs", callback_data="help_cmd"),
            InlineKeyboardButton("🎃 ᴍᴏʀᴇ ɪɴғᴏ", callback_data="more_info")
        ]
   
     ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                HOME_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass


    elif query.data=="help_cmd":
        get_me = await client.get_me()
        USERNAME = get_me.username
        buttons = [
                [
                    InlineKeyboardButton(
                        "🌾 sᴜᴅᴏ ᴄᴍᴅ ", callback_data="sudo_users"),
                    InlineKeyboardButton(
                        "🍃 ᴜsᴇʀs ᴄᴍᴅ", callback_data="users_cmd"),
                ],
                [
                    InlineKeyboardButton(
                        "🎓 ᴍᴀɪɴᴛᴀɪɴᴇʀ", url="https://t.me/Mr_Disaster_Xd"),
                    InlineKeyboardButton(
                        "🍀 ᴍᴏʀᴇ ɪɴғᴏ", callback_data="moreinfo")
                ],
                [
                    InlineKeyboardButton("⟲ ʙᴀᴄᴋ ⟳", callback_data="home")
                ]
           ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                HOME_TEXT.format(query.from_user.first_name, query.from_user.id),
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass



    elif query.data=="more_info":
        buttons =  [
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
                        "🎓 ᴅᴇᴠᴇʟᴏᴘᴇʀ", url="https://t.me/Mr_DiSasTer_XD")
                ],
                [
                    InlineKeyboardButton("⟲ ʙᴀᴄᴋ ⟳", callback_data="home")
                ]
           ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                MORE_TEXT.format(query.from_user.first_name, query.from_user.id),
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass  



    elif query.data=="users_cmd":
        buttons =  [              
                [
                    InlineKeyboardButton("⟲ ʙᴀᴄᴋ ⟳", callback_data="help_cmd")
                ]
           ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                USERS_CMD.format(query.from_user.first_name, query.from_user.id),
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass


    elif query.data=="sudo_users":
        buttons =  [              
                [
                    InlineKeyboardButton("⟲ ʙᴀᴄᴋ ⟳", callback_data="help_cmd")
                ]
           ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                SUDO_CMD.format(query.from_user.first_name, query.from_user.id),
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass 
 
   
 
