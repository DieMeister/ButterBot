from discord.ext import commands

from typing import TYPE_CHECKING

import internal

if TYPE_CHECKING:
    from discord.ext.commands import Context
    from main import ButterBot


class Bot(commands.Cog):
    def __init__(self, bot: "ButterBot") -> None:
        self.bot = bot

    @commands.command()
    async def sync(self, ctx: "Context") -> None:
        if ctx.author.id in internal.database["static"]["developer"]:
            amount_synced = len(await self.bot.tree.sync())

            await self.bot.log("bot.commands.sync", {
                "embed": {
                    "fields": {
                        "Amount": amount_synced,
                        "Guild": f"`{ctx.guild.name}`\n`{ctx.guild.id}`",
                        "Channel": f"`{ctx.channel.name}`\n`{ctx.channel.id}`",
                        "User": f"`{ctx.author.name}`\n`{ctx.author.id}`"
                    }
                },
                "file": {
                    "amount": amount_synced,
                    "execution_guild_id": ctx.guild.id,
                    "execution_channel_id": ctx.channel.id,
                    "execution_user_id": ctx.author.id
                }
            })
            await ctx.send("Commands synced")


async def setup(bot: "ButterBot") -> None:
    await bot.add_cog(Bot(bot))