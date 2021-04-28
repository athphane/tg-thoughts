import asyncio

from pyrogram.types import Message

from tgthoughtsbot.tgthoughtsbot import TgThoughtsBot
from tgthoughtsbot.utils import custom_filters


@TgThoughtsBot.on_message(custom_filters.command("restart"))
@TgThoughtsBot.admins_only
async def restart(bot: TgThoughtsBot, message: Message):
    await message.reply(f"Restarting {TgThoughtsBot}.")

    if 'p' in message.text and 'g' in message.text:
        asyncio.get_event_loop().create_task(bot.restart(git_update=True, pip=True))
    elif 'p' in message.text:
        asyncio.get_event_loop().create_task(bot.restart(pip=True))
    elif 'g' in message.text:
        asyncio.get_event_loop().create_task(bot.restart(git_update=True))
    else:
        asyncio.get_event_loop().create_task(bot.restart())
