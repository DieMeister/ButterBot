import discord
from discord.ext import commands

import os
from datetime import datetime, UTC
from colorama import Fore
from typing import TYPE_CHECKING, Optional, Union

import tokens
import internal

if TYPE_CHECKING:
    from discord.channel import VoiceChannel, StageChannel, ForumChannel, TextChannel, CategoryChannel


class ButterBot(commands.Bot):
    def get_guild_channel(self, guild_id: int, channel_id: int) -> "Optional[Union[VoiceChannel, StageChannel, ForumChannel, TextChannel, CategoryChannel]]":
        guild = self.get_guild(guild_id)
        if guild is not None:
            channel = guild.get_channel(channel_id)
            return channel
        return None

    async def log(self, log_type: str, variable_info: dict) -> None:
        # setting colors for each importance
        colors = {
            "debug": Fore.BLUE,
            "info": Fore.LIGHTWHITE_EX,
            "warning": Fore.LIGHTYELLOW_EX,
            "critical": Fore.RED
        }
        # creating a timestamp and the needed string formats of it
        timestamp = datetime.now(UTC)
        timestamp_date = timestamp.strftime("%Y-%m-%d")
        timestamp_str_short = timestamp.strftime("%Y-%m-%d %H:%M:%S")
        timestamp_str_long = timestamp.strftime("%Y-%m-%dT%H:%M:%S.%f+00:00")

        # updating the log count and log id
        internal.database["bot"]["log"]["log_count"] += 1
        log_id = internal.database["bot"]["log"]["log_count"]

        # gets the static data for the log entries
        static_info = internal.database["static"]["log_entries"][log_type]

        # provides the guild id if possible
        if "guild_id" in variable_info:
            static_info["guild_id"] = variable_info["guild_id"]

        # prints the log message to terminal
        print(f"{colors[static_info['importance']]}[{timestamp_str_short}] [{static_info['importance']:8}] [{log_id:8}] {static_info['terminal']['message']}{Fore.RESET}")

        # sends an embed to a discord channel
        if static_info["guild_id"] is None:
            log_guild_id = internal.database["bot"]["log"]["log_guild_id"]
            log_channel_id = internal.database["bot"]["log"]["log_channel_id"]
        else:
            log_guild_id = static_info["guild_id"]
            log_channel_id = internal.get_data(static_info["guild_id"], internal.database["guilds"], "guild_id")["log_channel_id"]
        channel = self.get_guild_channel(log_guild_id, log_channel_id)
        if channel is not None:
            if "description" in variable_info["embed"]:
                static_info["embed"]["description"] = variable_info["embed"]["description"]
            if "fields" in variable_info["embed"]:
                for i in variable_info["embed"]["fields"]:
                    for j in static_info["embed"]["fields"]:
                        if i == j["name"]:
                            j["value"] = variable_info["embed"]["fields"][i]
            static_info["embed"]["author"]["name"] = self.user.name
            static_info["embed"]["author"]["icon_url"] = self.user.display_avatar.url
            static_info["embed"]["color"] = 0xfa9b34
            static_info["embed"]["timestamp"] = timestamp_str_long
            await channel.send(embed=discord.Embed.from_dict(static_info["embed"]))
        else: print(f"{colors['warning']}[{datetime.now(UTC).strftime('%Y-%m-%d %H:%M:%S')}] [warning ] [{log_id:8}] couldn't find channel to send LogEmbed")

        # saves log to file
        for i in variable_info["file"]:
            static_info["file"][i] = variable_info["file"][i]
        static_info["file"]["log_id"] = log_id
        static_info["file"]["timestamp"] = timestamp_str_short
        try:
            log_file = internal.load_data(f"logs/{timestamp_date}.json")
        except FileNotFoundError:
            log_file = {
                "bot": [],
                "guilds": []
            }
        if static_info["guild_id"] is None:
            log_file["bot"].append(static_info["file"])
        else:
            guild_logs = internal.get_data(static_info["guild_id"], log_file["guilds"], "guild_id")
            if guild_logs is None:
                log_file["guilds"].append({
                    "guild_id": static_info["guild_id"],
                    "log_entries": [static_info["file"]]
                })
            else:
                guild_logs["log_entries"].append(static_info["file"])
        internal.save_data(log_file, f"logs/{timestamp_date}.json")

    async def setup_hook(self: commands.Bot) -> None:
        # loads database
        internal.database = internal.load_data("database.json")
        for file in os.listdir("database_extensions/static_extensions"):
            internal.database["static"][file[:-5]] = internal.load_data(f"database_extensions/static_extensions/{file}")
        await bot.log("setup_hook.load_database", {"embed":{},"file":{}})

        for file in os.listdir("./cogs"):
            if file.endswith(".py"):
                await self.load_extension(f"cogs.{file[:-3]}")
        await bot.log("setup_hook.load_bot_extensions", {
            "embed": {
                "description":f"{len(bot.cogs)} Cogs loaded"
            },
            "file": {
                "amount": len(bot.cogs)
            }
        })


intents = discord.Intents.all()
bot = ButterBot(command_prefix="!bb!", intents=intents, help_command=None)

bot.run(tokens.butter_test)
