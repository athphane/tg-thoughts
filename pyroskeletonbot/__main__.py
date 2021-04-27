import pyroskeletonbot
from pyroskeletonbot import PyroSkeletonBot, scheduler

if __name__ == '__main__':
    pyroskeletonbot.client = PyroSkeletonBot

    scheduler.start()

    PyroSkeletonBot.run()
