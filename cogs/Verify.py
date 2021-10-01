import aiohttp, asyncio, json
import string
import discord
import re
import bs4
from bs4 import BeautifulSoup
from discord.ext import commands
from discord.ext import tasks
import requests
import lxml
import nationstates
import json


class verify(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def verify(self, ctx, nation):
        msg = await ctx.author.send("Verifying...")
        msg = await ctx.author.send(f"Please log in {nation} now")
        msg = await ctx.author.send(
            "This next step is how I   make sure that nation is yours. Please go to this page: https://www.nationstates.net/page=verify_login \n Copy the code from the verification page and send it to me"
        )

        def check(msg):
            Message.channel.me == client.user

        ans2 = await ctx.wait_for("message", check=check)
        headers = {"User-Agent": "Nation:talusbot,nsdiscordbot "}
        ver = requests.get(
            f"https://www.nationstates.net/cgi-bin/api.cgi?a=verify&nation={ans1.content}&checksum={ans2.content}",
            headers=headers,
        )
        x = ver.text
        data = {"user": ctx.author.id, "nation": f"nation"}
        if int(x) == 1:
            await ctx.channel.send(
                f"verified that {ctx.author.mention} owns the nation {ans1.content}"
            )
            with open("ver.json", "w") as ver:
                json.dump(data, ver)
        else:
            await ctx.channel.send(
                f"the nation seem to be exist in boneyard see https://www.nationstates.net/nation={nation}"
            )


def setup(bot):
    bot.add_cog(verify(bot))
