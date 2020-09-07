import random
import asyncio

import discord
from discord.ext import commands

import secret as secret_cfg
import config as cfg


async def change_presence():
    # Waits until bot is loaded
    await bot.wait_until_ready()
    while not bot.is_closed():
        # Change presence every 60 seconds
        await bot.change_presence(
            activity=discord.Activity(type=discord.ActivityType.watching, name=random.choice(cfg.presence)))
        await asyncio.sleep(60)


class DiscordBot(commands.Bot):
    def __init__(self):
        super(DiscordBot, self).__init__(command_prefix=cfg.bot_info["prefix"])
        self.owner_id = secret_cfg.bot_info["owner"]
        self.token = secret_cfg.bot_info["token"]

        # Load all cogs
        for extension in cfg.cogs:
            try:
                self.load_extension(extension)
                print('Loaded module {}'.format(extension))
            except Exception as e:
                print('Failed to load module {}\n{}: {}'.format(extension, type(e).__name__, e))
        print('------')

    # Print bot info and set presence
    async def on_ready(self):
        print('Logged in as:')
        print('Username: ' + self.user.name)
        print('ID: ' + str(self.user.id))
        print('------')

    # Check if message is from bot
    async def on_message(self, message):
        if message.author.bot:
            return
        await self.process_commands(message)

    async def close(self):
        await super().close()

    def run(self):
        super().run(self.token, reconnect=True)


if __name__ == '__main__':
    bot = DiscordBot()
    # Create background task for presence
    bot.loop.create_task(change_presence())
    bot.run()
