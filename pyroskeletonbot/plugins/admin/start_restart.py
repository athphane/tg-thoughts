import asyncio

from pyrogram.types import Message

from pyroskeletonbot.pyroskeletonbot import PyroSkeletonBot
from pyroskeletonbot.utils import custom_filters


@PyroSkeletonBot.on_message(custom_filters.command("restart"))
@PyroSkeletonBot.admins_only
async def restart(bot: PyroSkeletonBot, message: Message):
    await message.reply(f"Restarting {PyroSkeletonBot}.")

    if 'p' in message.text and 'g' in message.text:
        asyncio.get_event_loop().create_task(bot.restart(git_update=True, pip=True))
    elif 'p' in message.text:
        asyncio.get_event_loop().create_task(bot.restart(pip=True))
    elif 'g' in message.text:
        asyncio.get_event_loop().create_task(bot.restart(git_update=True))
    else:
        asyncio.get_event_loop().create_task(bot.restart())
