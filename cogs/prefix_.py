import discord
from discord.ext import commands
import json


class Config(commands.Cog, name="Configuration"):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.__class__.__name__} Cog has been loaded\n-----")

    @commands.command()
    async def changeprefix(self, ctx, new_prefix):
        with open("./prefixes.json", "r") as f:
            prefixes = json.load(f)

            prefixes[str(ctx.guild.id)] = new_prefix

            with open("./prefixes.json", "w") as f:
                json.dump(prefixes, f, indent=4)


def setup(bot):
    bot.add_cog(Config(bot))
