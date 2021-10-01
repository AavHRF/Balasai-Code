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


class rmb(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def rmb(self, ctx, nation, region):
        with open("rmbaccess.json", "r") as f:
            data = json.load(f)
            print(data)
            print(ctx.guild.id)
        if str(ctx.guild.id) in list(data):
            my_list = [1]
            api = nationstates.Nationstates("petrixia")

            @tasks.loop(seconds=10)
            async def my_loop():
                headers = {"User-Agent": f"nation"}
                happenings = requests.get(
                    f"https://www.nationstates.net/cgi-bin/api.cgi?region={region}&q=messages;limit=1",
                    headers=headers,
                ).text
                ifs = re.search(r'<POST id="(?P<id>\d+)">', happenings).group("id")

                soup = BeautifulSoup(happenings, "xml")
                titles = soup.find("MESSAGE").text
                timestamp = soup.find("TIMESTAMP").text
                nat = soup.find("NATION").text
                nation = api.nation(nat)
                flag = nation.get_shards("flag")
                lik = soup.find("LIKES").text
                embed = discord.Embed(
                    title="RMB",
                    description="We will see rmb messages here ",
                    color=0x00FF00,
                )
                embed.set_thumbnail(url=flag["flag"])
                embed.add_field(
                    name="Nation",
                    value=(f"https://www.nationstates.net/nation={nat}"),
                    inline=True,
                )
                embed.add_field(name="Message", value=titles, inline=True)
                embed.add_field(name="Likes", value=lik, inline=True)
                embed.add_field(name="Region", value=region, inline=True)
                embed.add_field(
                    name="link to rmb",
                    value=(
                        f"https://www.nationstates.net/region={region}/page=display_region_rmb?postid={ifs}"
                    ),
                )
                embed.set_footer(
                    text="contact @balasai#2438 for any suggestions and custom edition"
                )
                if timestamp not in my_list:
                    await ctx.send(embed=embed)
                    my_list.append(timestamp)

            my_loop.start()
        else:
            await ctx.channel.send(
                "Your server is not autorised to use this contact balasai to get access this is only to make sure that no one will Misuse bot"
            )


def setup(bot):
    bot.add_cog(rmb(bot))
