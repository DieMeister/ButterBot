This is a multipurpose DiscordBot created to suit my personal preferences but possible to use on any server.
You need to add a `tokens.py` file which includes the bot token and import the python packages `discord.py` and `colorama` in order to run this bot by yourself. Also keep in mind to change `log_guild_id` and `log_channel_id` in `database.json` `bot: {log: {}}`
The following is a small documentation.
# Log Information Dictionaries (LIDs)
Log Information Dictionaries are always structured in 3 segments (terminal, embed, file), the places a log is saved if possible.
LIDs give the general structure of the logs having all variable values set to `null`; actual values are provided by a separate dictionary providing only the values and not necessarily the structure of the logs.
Below is the biggest possible version of a LID providing every possible value and its location.
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
                "inline": "bool",
                "value": "str",
                "name": "str"
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
        "amount": "int"
    }
}
```
The dictionary below represents a dictionary providing the actual values, showing its structure and which values can be changed.
```json
{
    "guild_id": null,
    "embed": {
        "description": "str",
        "fields": {
            "name": "value"
        }
    },
    "file": {}
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
        "timestamp": null
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
Variable Information is provided 
# Static Database Extensions
Static parts of the database are loaded separately for easier changes while the bot is running. Before they are loaded for the first time they are marked as `null` in the database.