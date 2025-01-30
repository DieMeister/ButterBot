import discord
from discord.ext import commands

import os

import tokens


class ButterBot(commands.Bot):
    async def setup_hook(self: commands.Bot) -> None:
        for file in os.listdir("./cogs"):
            await self.load_extension(f"cogs.{file[:-3]}")


intents = discord.Intents.all()
bot = ButterBot(command_prefix="!bb!", intents=intents, help_command=None)

bot.run(tokens.butter_test)