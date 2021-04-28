from pyrogram.types import Message

from tgthoughtsbot.tgthoughtsbot import TgThoughtsBot
from tgthoughtsbot.utils import custom_filters


@TgThoughtsBot.on_message(custom_filters.group)
async def fuck_groups(_, message: Message):
    """
     Needed to plop this somewhere
    """
    message.stop_propagation()
