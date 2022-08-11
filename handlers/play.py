import os
from os import path
from pyrogram import Client, filters
from pyrogram.types import Message, Voice, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram.errors import UserAlreadyParticipant
from callsmusic import callsmusic, queues
from callsmusic.callsmusic import client as USER
from helpers.admins import get_administrators
import requests
import aiohttp
from youtube_search import YoutubeSearch
import converter
from downloaders import youtube
from config import DURATION_LIMIT, SUPPORT_GROUP
from helpers.filters import command
from helpers.decorators import errors
from helpers.errors import DurationLimitError
from helpers.gets import get_url, get_file_name
import aiofiles
import ffmpeg
from PIL import Image, ImageFont, ImageDraw
from pytgcalls import StreamType
from pytgcalls.types.input_stream import InputAudioStream
from pytgcalls.types.input_stream import InputStream


def transcode(filename):
    ffmpeg.input(filename).output("input.raw", format='s16le', acodec='pcm_s16le', ac=2, ar='48k').overwrite_output().run() 
    os.remove(filename)

# Convert seconds to mm:ss
def convert_seconds(seconds):
    seconds = seconds % (24 * 3600)
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return "%02d:%02d" % (minutes, seconds)


# Convert hh:mm:ss to seconds
def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60 ** i for i, x in enumerate(reversed(stringt.split(':'))))


# Change image size
def changeImageSize(maxWidth, maxHeight, image):
    widthRatio = maxWidth / image.size[0]
    heightRatio = maxHeight / image.size[1]
    newWidth = int(widthRatio * image.size[0])
    newHeight = int(heightRatio * image.size[1])
    newImage = image.resize((newWidth, newHeight))
    return newImage

async def generate_cover(requested_by, title, views, duration, thumbnail):
    async with aiohttp.ClientSession() as session:
        async with session.get(thumbnail) as resp:
            if resp.status == 200:
                f = await aiofiles.open("background.png", mode="wb")
                await f.write(await resp.read())
                await f.close()


    image1 = Image.open("./background.png")
    image2 = Image.open("etc/foreground.png")
    image3 = changeImageSize(1280, 720, image1)
    image4 = changeImageSize(1280, 720, image2)
    image5 = image3.convert("RGBA")
    image6 = image4.convert("RGBA")
    Image.alpha_composite(image5, image6).save("temp.png")
    img = Image.open("temp.png")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("etc/font.otf", 32)
     
    img.save("final.png")
    os.remove("temp.png")
    os.remove("background.png")



@Client.on_message(
    command(["play"])
    & filters.group
    & ~filters.edited
    & ~filters.forwarded
    & ~filters.via_bot
)
async def play(_, message: Message):
    global que
    global useer

    lel = await message.reply("🔎 **sᴇᴀʀᴄʜɪɴɢ..**")

    chumtiya = message.from_user.mention

    administrators = await get_administrators(message.chat)
    chid = message.chat.id

    try:
        user = await USER.get_me()
    except:
        user.first_name = "SumitYadav"
    usar = user
    wew = usar.id
    try:
        await _.get_chat_member(chid, wew)
    except:
        for administrator in administrators:
            if administrator == message.from_user.id:
                try:
                    invitelink = await _.export_chat_invite_link(chid)
                except:
                    await lel.edit(
                        "<b> » ᴀᴅᴅ ᴍᴇ ᴀs ᴀᴅᴍɪɴ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ғɪʀsᴛ.</b>")
                    return

                try:
                    await USER.join_chat(invitelink)
                    await USER.send_message(
                        message.chat.id, "**» ᴀssɪsᴛᴀɴᴛ ᴊᴏɪɴᴇᴅ ᴛʜɪs ɢʀᴏᴜᴘ ғᴏʀ ᴘʟᴀʏ ᴍᴜsɪᴄ.**")

                except UserAlreadyParticipant:
                    pass
                except Exception:
                    await lel.edit(
                        f"<b>» ғʟᴏᴏᴅ ᴡᴀɪᴛ ᴇʀʀᴏʀ </b>\nʜᴇʏ ᴀssɪsᴛᴀɴᴛ ᴜsᴇʀʙᴏᴛ ᴄᴏᴜʟᴅ ɴᴏᴛ ᴊᴏɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴅᴜᴇ ᴛᴏ ʜᴇᴀᴠʏ ᴊᴏɪɴ ʀᴇǫᴜᴇsᴛ. ᴍᴀᴋᴇ sᴜʀᴇ ᴜsᴇʀʙᴏᴛ ɪs ɴᴏᴛ ʙᴀɴɴᴇᴅ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ ʟᴀᴛᴇʀ ɪғ ʏᴏᴜ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ ᴛʜᴇɴ ᴄᴏɴᴛᴀᴄᴛ ɴʏ ᴏᴡɴᴇʀ [sᴜᴍɪᴛ ʏᴀᴅᴀᴠ](https://t.me/SIMPLE_MUNDAA)")
    try:
        await USER.get_chat(chid)
    except:
        await lel.edit(
            f"<i> » ʜᴇʏ {user.first_name}, ᴀssɪsᴛᴀɴᴛ ᴜsᴇʀʙᴏᴛ ɪs ɴᴏᴛ ɪɴ ᴛʜɪs ᴄʜᴀᴛ' ᴀsᴋ ᴀᴅᴍɪɴ ᴛᴏ sᴇɴᴅ /Play ᴄᴏᴍᴍᴀɴᴅs ғᴏʀ ғɪʀsᴛ ᴛɪᴍᴇ ᴛᴏ ᴀᴅᴅ ɪғ ʏᴏᴜ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ ᴛʜᴇɴ ᴄᴏɴᴛᴀᴄᴛ ɴʏ ᴏᴡɴᴇʀ [sᴜᴍɪᴛ ʏᴀᴅᴀᴠ](https://t.me/SIMPLE_MUNDAA)</i>")
        return
    
    audio = (
        (message.reply_to_message.audio or message.reply_to_message.voice)
        if message.reply_to_message
        else None
    )
    url = get_url(message)

    if audio:
        if round(audio.duration / 60) > DURATION_LIMIT:
            raise DurationLimitError(
                f"» sᴏɴɢ ʟᴏɴɢᴇʀ ᴛʜᴀɴ {DURATION_LIMIT} ᴍɪɴᴜᴛᴇ's ᴀʀᴇ ɴᴏᴛ ᴀʟʟᴏᴡᴇᴅ ᴛᴏ ᴘʟᴀʏ."
            )

        file_name = get_file_name(audio)
        title = file_name
        thumb_name = "https://te.legra.ph/file/0eca22cc7f98ed470b010.jpg"
        thumbnail = thumb_name
        duration = round(audio.duration / 60)
        views = "Locally added"

        keyboard = InlineKeyboardMarkup(
            [
                
               [
                    InlineKeyboardButton(
                            text="ᴜᴘᴅᴀᴛᴇs",
                            url=f"https://t.me/TechQuard"),
                            
                    InlineKeyboardButton(
                            text="sᴜᴘᴘᴏʀᴛ",
                            url=f"https://t.me/{SUPPORT_GROUP}")
               ],
               [ 
                     InlineKeyboardButton(
                            text="ᴄʟᴏsᴇ",
                            callback_data="close_play")
               ],
               
            ]
        )

        requested_by = message.from_user.first_name
        await generate_cover(requested_by, title, views, duration, thumbnail)
        file_path = await converter.convert(
            (await message.reply_to_message.download(file_name))
            if not path.isfile(path.join("downloads", file_name))
            else file_name
        )

    elif url:
        try:
            results = YoutubeSearch(url, max_results=1).to_dict()
            # print results
            title = results[0]["title"]
            thumbnail = results[0]["thumbnails"][0]
            thumb_name = f"thumb{title}.jpg"
            thumb = requests.get(thumbnail, allow_redirects=True)
            open(thumb_name, "wb").write(thumb.content)
            duration = results[0]["duration"]
            url_suffix = results[0]["url_suffix"]
            views = results[0]["views"]
            durl = url
            durl = durl.replace("youtube", "youtubepp")

            secmul, dur, dur_arr = 1, 0, duration.split(":")
            for i in range(len(dur_arr) - 1, -1, -1):
                dur += int(dur_arr[i]) * secmul
                secmul *= 60

            keyboard =  InlineKeyboardMarkup(
            [
                
               [
                    InlineKeyboardButton(
                            text="ᴜᴘᴅᴀᴛᴇs",
                            url=f"https://t.me/TechQuard"),
                            
                    InlineKeyboardButton(
                            text="sᴜᴘᴘᴏʀᴛ",
                            url=f"https://t.me/{SUPPORT_GROUP}")
               ],
               [ 
                     InlineKeyboardButton(
                            text="ᴄʟᴏsᴇ",
                            callback_data="close_play")
               ],
               
            ]
        )

        except Exception as e:
            title = "NaN"
            thumb_name = "https://te.legra.ph/file/0eca22cc7f98ed470b010.jpg"
            duration = "NaN"
            views = "NaN"
            keyboard =  InlineKeyboardMarkup(
            [
                
               [
                    InlineKeyboardButton(
                            text="ᴜᴘᴅᴀᴛᴇs",
                            url=f"https://t.me/TechQuard"),
                            
                    InlineKeyboardButton(
                            text="sᴜᴘᴘᴏʀᴛ",
                            url=f"https://t.me/{SUPPORT_GROUP}")
               ],
               [ 
                     InlineKeyboardButton(
                            text="ᴄʟᴏsᴇ",
                            callback_data="close_play")
               ],
               
            ]
        )

        if (dur / 60) > DURATION_LIMIT:
            await lel.edit(
                f"» sᴏɴɢ ʟᴏɴɢᴇʀ ᴛʜᴀɴ {DURATION_LIMIT} ᴍɪɴᴜᴛᴇ's ᴀʀᴇ ɴᴏᴛ ᴀʟʟᴏᴡᴇᴅ ᴛᴏ ᴘʟᴀʏ."
            )
            return
        requested_by = message.from_user.first_name
        await generate_cover(requested_by, title, views, duration, thumbnail)
        file_path = await converter.convert(youtube.download(url))
    else:
        if len(message.command) < 2:
            await m.reply_photo(
                     photo=f"https://te.legra.ph/file/b07e1debac241e6d9b30e.jpg",
                    caption="💌**ᴜsᴀɢᴇ: /play ɢɪᴠᴇ ᴀ ᴛɪᴛʟᴇ sᴏɴɢ ᴛᴏ ᴘʟᴀʏ ᴍᴜsɪᴄ**"
                    ,
                      reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("👥 sᴜᴘᴘᴏʀᴛ", url="https://t.me/TechQuardSupport"),
                            InlineKeyboardButton("📢 ᴜᴘᴅᴀᴛᴇs", url="https://t.me/TechQuard")
                        ]
                    ]
                )
            )
        await lel.edit("💓")
        query = message.text.split(None, 1)[1]
        # print(query)
        try:
            results = YoutubeSearch(query, max_results=1).to_dict()
            url = f"https://youtube.com{results[0]['url_suffix']}"
            # print results
            title = results[0]["title"]
            thumbnail = results[0]["thumbnails"][0]
            thumb_name = f"thumb{title}.jpg"
            thumb = requests.get(thumbnail, allow_redirects=True)
            open(thumb_name, "wb").write(thumb.content)
            duration = results[0]["duration"]
            url_suffix = results[0]["url_suffix"]
            views = results[0]["views"]
            durl = url
            durl = durl.replace("youtube", "youtubepp")

            secmul, dur, dur_arr = 1, 0, duration.split(":")
            for i in range(len(dur_arr) - 1, -1, -1):
                dur += int(dur_arr[i]) * secmul
                secmul *= 60

        except Exception as e:
            await lel.edit(
                "» ɴᴏᴛ ғᴏᴜɴᴅ, ᴛʀʏ sᴇᴀʀᴄʜɪɴɢ ᴡɪᴛʜ ᴛʜᴇ sᴏɴɢ ɴᴀᴍᴇ ."
            )
            print(str(e))
            return

        keyboard =  InlineKeyboardMarkup(
            [
                
               [
                    InlineKeyboardButton(
                            text="ᴜᴘᴅᴀᴛᴇs",
                            url=f"https://t.me/TechQuard"),
                            
                    InlineKeyboardButton(
                            text="sᴜᴘᴘᴏʀᴛ",
                            url=f"https://t.me/{SUPPORT_GROUP}")
               ],
               [ 
                     InlineKeyboardButton(
                            text="ᴄʟᴏsᴇ",
                            callback_data="close_play")
               ],
               
            ]
        )

        if (dur / 60) > DURATION_LIMIT:
            await lel.edit(
                f"» sᴏɴɢ ʟᴏɴɢᴇʀ ᴛʜᴀɴ {DURATION_LIMIT} ᴍɪɴᴜᴛᴇ's ᴀʀᴇ ɴᴏᴛ ᴀʟʟᴏᴡᴇᴅ ᴛᴏ ᴘʟᴀʏ."
            )
            return
        requested_by = message.from_user.first_name
        await generate_cover(requested_by, title, views, duration, thumbnail)
        file_path = await converter.convert(youtube.download(url))
    ACTV_CALLS = []
    chat_id = message.chat.id
    for x in callsmusic.pytgcalls.active_calls:
        ACTV_CALLS.append(int(x.chat_id))
    if int(chat_id) in ACTV_CALLS:
        position = await queues.put(chat_id, file=file_path)
        await message.reply_photo(
            photo="final.png",
            caption=f"**» ᴛʀᴀᴄᴋ ᴀᴅᴅᴇᴅ ᴛᴏ ǫᴜᴇᴜᴇ {position} **\n\n​🪗 **ɴᴀᴍᴇ :**{title}\n\n⏰ ** ᴅᴜʀᴀᴛɪᴏɴ :** `{duration}` **ᴍɪɴᴜᴛᴇs**\n🥁 ** ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ​ : **{chumtiya}",
            reply_markup=keyboard,
        )
    else:
        await callsmusic.pytgcalls.join_group_call(
                chat_id, 
                InputStream(
                    InputAudioStream(
                        file_path,
                    ),
                ),
                stream_type=StreamType().local_stream,
            )

        await message.reply_photo(
            photo="final.png",
            reply_markup=keyboard,
            caption=f"**─────────────────**\n**​🪗 ɴᴀᴍᴇ :** {title}\n**─────────────────**\n⏰ **ᴅᴜʀᴀᴛɪᴏɴ:** `{duration}` ᴍɪɴᴜᴛᴇs\n🥁 **ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ​:** {chumtiya}\n", )

    os.remove("final.png")
    return await lel.delete()

@Client.on_callback_query(filters.regex("close_play"))
async def in_close_play(_, query: CallbackQuery):
    await query.message.delete()
