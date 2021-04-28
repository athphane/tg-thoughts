from pyrogram.types import Message

from tgthoughtsbot.database.users import UserDB
from tgthoughtsbot.tgthoughtsbot import TgThoughtsBot
from tgthoughtsbot.utils import custom_filters


@TgThoughtsBot.on_message(custom_filters.command("users"))
async def users_count(bot: TgThoughtsBot, message: Message):
    users = UserDB().all_users().count()
    await message.reply(f"{TgThoughtsBot.__name__} has {users} users.")
