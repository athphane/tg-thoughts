# PyroSkeletonBot
A Telegram Bot based on [Pyrogram](https://github.com/pyrogram/pyrogram)

This is a base skeleton that I use for my bot development process.

## Requirements
You're gonna need to get the following programs and services either installed on your server
or signed up for. You must do all. It is a cardinal sin if you don't.

* `virtualenv` installed so that the packages don't interfere with other system packages.

* [MongoDB](https://www.mongodb.com) on your server or a free server from 
[MongoDB Atlas](https://www.mongodb.com/cloud/atlas). (I recommend Atlas as I used it during
development with no issues.)

## Installing
```bash
git clone https://github.com/athphane/PyroSkeleton.git
cd PyroSkeleton
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
python -m pyroskeleton
```

## Developing
To add extra modules to the bot, simply add the code into [pyroskeletonbot/plugins](pyroskeletonbot/plugins). Each file
that is added to the 'plugins' directory should have the following code at a minimum.
```python
from pyrogram.types import Message
from pyroskeletonbot.utils import custom_filters

from pyroskeletonbot import PyroSkeletonBot

@PyroSkeletonBot.on_message(custom_filters.command('sample', ['.']))
async def module_name(bot: PyroSkeletonBot, message: Message):
    await message.edit("This is a sample module")
```

This example is only for Pyrogram on_message events. 
