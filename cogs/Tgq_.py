import discord
from bs4 import BeautifulSoup
from discord.ext import commands
import requests
import json


class tgq(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def tgq(self, ctx):
        with open("generalaccess.json", "r") as f:
            data = json.load(f)
            print(data)
            print(ctx.guild.id)
        if str(ctx.guild.id) in list(data):
            headers = {"User-Agent": "forcosts"}
            c = requests.get(
                "https://www.nationstates.net/cgi-bin/api.cgi?q=tgqueue",
                headers=headers,
            ).text
            sou = BeautifulSoup(c, "xml")
            ma = sou.find("MANUAL").text
            ms = sou.find("MASS").text
            API = sou.find("API").text
            embed = discord.Embed(
                title="Tgq",
                description="no of telegrams currently queued",
                color=0x00FF00,
            )
            embed.add_field(name="Manual", value=ma, inline=True)
            embed.add_field(name="API", value=API, inline=True)
            embed.add_field(name="Stamps", value=ms, inline=True)
            embed.set_footer(
                text="contact @balasai#2438 for problems, new commands and suggestions "
            )
            await ctx.send(embed=embed)
        else:
            await ctx.channel.send(
                "Your server is not autorised to use this contact balasai to get access this is only to make sure that no one will Misuse bot"
            )


def setup(bot):
    bot.add_cog(tgq(bot))
