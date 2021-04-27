from pyrogram.types import Message
from pyroskeletonbot.pyroskeletonbot import PyroSkeletonBot
from pyroskeletonbot.utils import custom_filters
from pyroskeletonbot.utils.aiohttp_helper import AioHttp


@PyroSkeletonBot.on_message(custom_filters.command("xkcd"))
async def xkcd_image(bot: PyroSkeletonBot, message: Message):
    xkcd = await AioHttp.get_json("https://xkcd.com/info.0.json")
    text = xkcd['title'] + "\n\n" + xkcd['alt']
    await message.reply_photo(xkcd['img'], caption=text)
