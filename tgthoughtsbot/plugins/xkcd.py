from pyrogram.types import Message
from tgthoughtsbot.tgthoughtsbot import TgThoughtsBot
from tgthoughtsbot.utils import custom_filters
from tgthoughtsbot.utils.aiohttp_helper import AioHttp


@TgThoughtsBot.on_message(custom_filters.command("xkcd"))
async def xkcd_image(bot: TgThoughtsBot, message: Message):
    xkcd = await AioHttp.get_json("https://xkcd.com/info.0.json")
    text = xkcd['title'] + "\n\n" + xkcd['alt']
    await message.reply_photo(xkcd['img'], caption=text)
