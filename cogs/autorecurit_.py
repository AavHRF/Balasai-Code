import aiohttp, asyncio, json
import string
import discord
import re
import bs4
from bs4 import BeautifulSoup as b
from discord.ext import commands
from discord.ext import tasks
import requests
import lxml
import nationstates


class autorecruit(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def autorecruit(self, ctx, tgid, cilent, secretkey, nation, region):
        with open("autorecruitaccess.json", "r") as f:
            data = json.load(f)
            print(data)
            print(ctx.guild.id)
        if str(ctx.guild.id) in list(data):
            await ctx.message.delete()
            my_list = [1]

            @tasks.loop(seconds=180)
            async def my_loop():
                headers = {"User-Agent": f"nation"}
                happenings = requests.get(
                    f"https://www.nationstates.net/cgi-bin/api.cgi?q=happenings;filter=founding",
                    headers=headers,
                ).text
                a = b(happenings, "xml")
                c = a.find("TEXT").text
                c = c.replace("@@", " ")
                c = c.split()[0]
                r = requests.get(
                    f"https://www.nationstates.net/cgi-bin/api.cgi?nation={c}&q=tgcanrecruit&from={region}",
                    headers=headers,
                ).text
                d = b(r, "xml")
                e = d.find("TGCANRECRUIT").text
                f = int(e)
                if f == 1:
                    r = requests.get(
                        f"https://www.nationstates.net/cgi-bin/api.cgi?a=sendTG&client={cilent}&tgid={tgid}&key={secretkey}&to={c}",
                        headers=headers,
                    )
                    await ctx.message.channel.send(
                        "Requrit completed waiting for api limit to expire"
                    )
                else:
                    await ctx.message.channel.send(
                        "target unable to be requrited moving to next one"
                    )
                my_loop.start()

        else:
            await ctx.channel.send(
                "Your server is not autorised to use this contact balasai to get access this is only to make sure that no one will Misuse bot"
            )


def setup(bot):
    bot.add_cog(autorecruit(bot))
