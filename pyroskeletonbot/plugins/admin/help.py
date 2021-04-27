from pyrogram.types import Message

from pyroskeletonbot.pyroskeletonbot import PyroSkeletonBot
from pyroskeletonbot.utils import custom_filters


@PyroSkeletonBot.on_message(custom_filters.command("help"))
async def help_message(_, message: Message):
    await message.reply(
        "Here is some helpful information on how to use me! \n"
        "/help - Shows this message\n"
    )
