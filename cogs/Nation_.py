import colorthief
from colorthief import ColorThief
import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup
from discord import Color
import html
import aiohttp
import asyncio
import json


def human_format(num):
    magnitude = 0
    while abs(num) >= 1000:
        magnitude += 1
        num /= 1000.0
    # add more suffixes if you need them
    return "%.2f%s" % (num, ["", "K", " million", " billion", "T", "P"][magnitude])


class nation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def nation(self, ctx, *, nation):
        with open("generalaccess.json", "r") as f:
            data = json.load(f)
            print(data)
            print(ctx.guild.id)
        if str(ctx.guild.id) in list(data):
            headers = {"User-Agent": "indusse"}
            r = requests.get(
                f"https://www.nationstates.net/cgi-bin/api.cgi?nation={nation}&q=name+motto+leader+animal+name+fullname+category+region+currency+founded+foundedtime+lastactivity+wa+influence+population+flag+demonym2plural+capital",
                headers=headers,
            ).text
            s = BeautifulSoup(r, "xml")

            nation = nation.replace(" ", "_")
            currency = s.find("CURRENCY").text
            motto = s.find("MOTTO").text
            an = s.find("ANIMAL").text
            leader = s.find("LEADER").text
            f = s.find("FLAG").text
            n = s.find("NAME").text
            cap = s.find("CAPITAL").text
            na = s.find("FULLNAME").text
            c = s.find("CATEGORY").text
            wa = s.find("UNSTATUS").text
            reg = s.find("REGION").text
            po = int(s.find("POPULATION").text)
            print(po)
            denonym = s.find("DEMONYM2PLURAL").text
            pon = po * 1000000
            pop = human_format(pon)
            fund = s.find("FOUNDED").text
            la = s.find("LASTACTIVITY").text
            ra = requests.get(f)
            file = open("flag.png", "wb")
            file.write(ra.content)
            file.close()
            color_thief = ColorThief("flag.png")
            dominant_color = color_thief.get_color(quality=1)
            print(dominant_color)
            r = dominant_color[0]
            g = dominant_color[1]
            b = dominant_color[2]
            # palette = color_thief.get_palette(color_count=2 )

            inf = s.find("INFLUENCE").text
            m = html.unescape(motto)
            embed = discord.Embed(color=discord.Color.from_rgb(r, g, b))
            embed.set_author(name=na, url=f"https://www.nationstates.net/{nation}")
            embed.add_field(name="Capital", value=cap, inline=False)
            embed.add_field(name="LEADER", value=leader, inline=False)
            embed.add_field(name="Founded", value=fund, inline=False)

            embed.add_field(name="Currency", value=currency, inline=False)
            embed.add_field(name="Animal", value=an, inline=False)
            embed.add_field(name="Region", value=reg, inline=False)
            embed.add_field(name="Last Active", value=la, inline=False)
            embed.add_field(name="World Assembly", value=wa, inline=False)
            embed.add_field(name="Influence", value=inf, inline=False)
            embed.add_field(name="Population", value=pop, inline=False)
            embed.add_field(name="people called", value=denonym, inline=False)
            embed.add_field(name="Motto", value=m, inline=False)
            embed.set_footer(text="contact @balasai#2438 for more queries")
            embed.set_thumbnail(url=f)
            await ctx.send(embed=embed)
        else:
            await ctx.channel.send(
                "Your server is not autorised to use this contact balasai to get access this is only to make sure that no one will Misuse bot"
            )


def setup(bot):
    bot.add_cog(nation(bot))
