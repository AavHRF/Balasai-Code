import discord
from discord.ext import commands
from discord import Intents, AllowedMentions
from typing import Optional
from traceback import print_exc
from aiohttp import ClientSession
import json
from bot_utils.Help_ import HelpCommand


def get_prefix(client, message):  ##first we define get_prefix
    with open(
        "prefixes.json", "r"
    ) as f:  ##we open and read the prefixes.json, assuming it's in the same file
        prefixes = json.load(f)  # load the json as prefixes
    try:
        return prefixes[
            str(message.guild.id)
        ]  # recieve the prefix for the guild id given
    except:
        return "sbs!"


class Bot(commands.Bot):
    """A subclass of `commands.Bot` with additional features."""

    def __init__(self, *args, **kwargs):
        intents = Intents.default()

        super().__init__(
            command_prefix=get_prefix,
            intents=intents,
            allowed_mentions=AllowedMentions(everyone=False, users=False, roles=False),
            help_command=HelpCommand(),
            case_insensitive=True,
            *args,
            **kwargs,
        )

        self.session: Optional[ClientSession] = None

    def load_cogs(self, *exts) -> None:
        """Load a set of extensions."""

        for ext in exts:
            try:
                self.load_extension(ext)
            except Exception as e:
                print_exc()

    async def login(self, *args, **kwargs) -> None:
        """Create the ClientSession before logging in."""

        self.session = ClientSession()

        await super().login(*args, **kwargs)

    async def on_ready(self):
        print("Bot Logged in.")
