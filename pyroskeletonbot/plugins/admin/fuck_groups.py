from pyrogram.types import Message

from pyroskeletonbot.pyroskeletonbot import PyroSkeletonBot
from pyroskeletonbot.utils import custom_filters


@PyroSkeletonBot.on_message(custom_filters.group)
async def fuck_groups(_, message: Message):
    """
     Needed to plop this somewhere
    """
    message.stop_propagation()
