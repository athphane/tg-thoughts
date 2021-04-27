import time
import os
from pyroskeletonbot.utils import custom_filters
from pyroskeletonbot.pyroskeletonbot import PyroSkeletonBot
from pyrogram.types import Message


@PyroSkeletonBot.on_message(custom_filters.command('log'))
async def send_log_file(bot: PyroSkeletonBot, message: Message):
    if os.path.exists(f"logs/{PyroSkeletonBot.__name__.lower()}.log"):
        await message.reply_chat_action('upload_document')
        await message.reply_document(
            document=f"logs/{PyroSkeletonBot.__name__.lower()}.log",
            caption="This file was uploaded on:\n**{}**".format(time.ctime(time.time()))
        )
    else:
        await message.reply("Oddly enough, there is no log file. Try again?")



