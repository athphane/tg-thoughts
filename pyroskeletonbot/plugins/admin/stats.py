from pyrogram.types import Message

from pyroskeletonbot.database.users import UserDB
from pyroskeletonbot.pyroskeletonbot import PyroSkeletonBot
from pyroskeletonbot.utils import custom_filters


@PyroSkeletonBot.on_message(custom_filters.command("users"))
async def users_count(bot: PyroSkeletonBot, message: Message):
    users = UserDB().all_users().count()
    await message.reply(f"{PyroSkeletonBot.__name__} has {users} users.")
