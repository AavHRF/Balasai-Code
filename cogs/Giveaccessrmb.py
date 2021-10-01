import discord
from bs4 import BeautifulSoup as b
from discord.ext import commands
import requests
import json


class rmbaccess(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def giveaccess_rmb(self, ctx, guildid):
        with open("moderator.json", "r") as f:
            data = json.load(f)
            print(data)
            print(ctx.author.id)
        if str(ctx.author.id) in list(data):
            with open("rmbaccess.json", "r") as file:
                data = json.load(file)
                data.append(guildid)
            with open("rmbaccess.json", "w") as file:
                json.dump(data, file)
                await ctx.channel.send("gave access to guild")


def setup(bot):
    bot.add_cog(rmbaccess(bot))
