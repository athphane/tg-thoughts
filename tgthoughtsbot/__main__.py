import tgthoughtsbot
from tgthoughtsbot import TgThoughtsBot, scheduler

if __name__ == '__main__':
    tgthoughtsbot.client = TgThoughtsBot

    scheduler.start()

    TgThoughtsBot.run()
