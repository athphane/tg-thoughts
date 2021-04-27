from pyrogram.types import Message, InlineQuery

from pyroskeletonbot import PyroSkeletonBot
from pyroskeletonbot.database.users import UserDB
from pyroskeletonbot.utils import custom_filters


@PyroSkeletonBot.on_message(~custom_filters.group & custom_filters.private, group=-10)
async def creates_the_user(bot: PyroSkeletonBot, message: Message):
    user = UserDB().find_user(message.from_user)
    if user is None:
        UserDB().find_or_create(message.from_user)
        if message.from_user.last_name and message.from_user.username:
            full_message = (
                f"**A new user has started using {str(PyroSkeletonBot)}**\n"
                "UserID: __[{user_id}](tg://user?id={user_id})__\n"
                "First Name: __{first_name}__\n"
                "Last Name: __{last_name}__\n"
                "Username: @{username}"
            )

            await bot.send_log(
                full_message.format(
                    user_id=message.from_user.id,
                    first_name=message.from_user.first_name,
                    last_name=message.from_user.last_name,
                    username=message.from_user.username,
                )
            )

        elif message.from_user.username:
            username_message = (
                f"**A new user has started using {str(PyroSkeletonBot)}**\n"
                "UserID: __[{user_id}](tg://user?id={user_id})__\n"
                "First Name: __{first_name}__\n"
                "Username: @{username}"
            )

            await bot.send_log(
                username_message.format(
                    user_id=message.from_user.id,
                    first_name=message.from_user.first_name,
                    username=message.from_user.username,
                )
            )

        else:
            f_name_message = (
                f"**A new user has started using {str(PyroSkeletonBot)}**\n"
                "UserID: __[{user_id}](tg://user?id={user_id})__\n"
                "First Name: __{first_name}__"
            )

            await bot.send_log(
                f_name_message.format(
                    user_id=message.from_user.id,
                    first_name=message.from_user.first_name,
                )
            )
    else:
        UserDB().update_user(message.from_user)
    message.continue_propagation()


@PyroSkeletonBot.on_inline_query(group=9)
async def callback_user_updating(_, inline_query: InlineQuery):
    user = UserDB().find_user(inline_query.from_user)
    if user:
        UserDB().update_user(inline_query.from_user)
