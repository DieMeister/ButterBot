This is a multipurpose DiscordBot created to suit my personal preferences but possible to use on any server.
You need to add a `tokens.py` file which includes the bot token and import the python packages `discord.py` and `colorama` in order to run this bot by yourself. Also keep in mind to change `log_guild_id` and `log_channel_id` in `database.json` `bot: {log: {}}`

The following is a small documentation.
# Log Information Dictionaries (LIDs)
Log Information Dictionaries are always structured in 3 segments (terminal, embed, file), the places a log is saved if possible.
LIDs give the general structure of the logs having all variable values set to `null`; actual values are provided by a separate dictionary providing only the values and not necessarily the structure of the logs.

Below is a LID providing its structure as well as the basic embed layout for commands and every possible value for file logs
```json
{
    "importance": ["debug", "info", "warning", "critical"],
    "guild_id": "int",
    "terminal": {
        "message": "str"
    },
    "embed": {
        "author": {
            "name": "str",
            "icon_url": "str"
        },
        "title": "str",
        "description": "str",
        "color": "int",
        "fields": [
            {
                    "name": "Command",
                    "value": "\u200B",
                    "inline": false
                },
                {
                    "name": "CommandName",
                    "value": "str",
                    "inline": true
                },
                {
                    "name": "CommandType",
                    "value": ["Developer"],
                    "inline": true
                },
                {
                    "name": "**__executed in/by__**",
                    "value": "\u200B",
                    "inline": false
                },
                {
                    "name": "Guild",
                    "value": "`{ctx.guild.name}`\n`{ctx.guild.id}`",
                    "inline": true
                },
                {
                    "name": "Channel",
                    "value": "`{ctx.channel.name}`\n`{ctx.channel.id}`",
                    "inline": true
                },
                {
                    "name": "User",
                    "value": "`{ctx.author.name}`\n`{ctx.author.id}`",
                    "inline": true
                }
        ],
        "timestamp": "str",
        "footer": {
            "text": ["main"]
        },
        "type": "rich"
    },
    "file": {
        "log_id": "int",
        "timestamp": "str",
        "description": "str",
        "amount": "int",
        "command_name": "str",
        "command_type": ["developer"],
        "execution_guild_id": "int",
        "execution_channel_id": "int",
        "execution_user_id": "int"
    }
}
```
The minimal requirements for each are:

LID
```json
{
    "importance": null,
    "guild_id":  null,
    "terminal": {
        "message": null
    },
    "embed": {
        "author": {
            "name": null,
            "icon_url": null
        },
        "title": null,
        "color": null,
        "timestamp": null,
        "footer": {
            "text": null
        },
        "type": "rich"
    },
    "file": {
        "log_id": null,
        "timestamp": null,
        "description": null
    }
}
```
variables
```json
{
    "embed": {},
    "file": {}
}
``` 
# Static Database Extensions
Static parts of the database are loaded separately for easier changes while the bot is running. Before they are loaded for the first time they are marked as `null` in the database.