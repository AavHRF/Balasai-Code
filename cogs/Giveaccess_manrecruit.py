import discord
from bs4 import BeautifulSoup as b
from discord.ext import commands
import requests
import json


class giveaccess(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def giveaccess_recruit(self, ctx, guildid):
        with open("moderator.json", "r") as f:
            data = json.load(f)
            print(data)
            print(ctx.author.id)
        if str(ctx.author.id) in list(data):
            with open("recruitaccess.json", "r") as file:
                data = json.load(file)
                data.append(guildid)
            with open("recruitaccess.json", "w") as file:
                json.dump(data, file)
                await ctx.channel.send("gave access to guild")


def setup(bot):
    bot.add_cog(giveaccess(bot))
