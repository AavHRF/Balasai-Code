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


class Region(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def region(self, ctx, *, region):
        with open("generalaccess.json", "r") as f:
            data = json.load(f)
            print(data)
            print(ctx.guild.id)
        if str(ctx.guild.id) in list(data):
            headers = {"User-Agent": "hevenda"}
            r = requests.get(
                f"https://www.nationstates.net/cgi-bin/api.cgi?region={region}&q=wabadges+name+power+numnations+founder+foundedtime+founded+flag+delegatevotes+delegateauth+delegate",
                headers=headers,
            ).text

            soup = BeautifulSoup(r, "xml")
            numnat = soup.find("NUMNATIONS").text
            p = soup.find("POWER").text
            name = soup.find("NAME").text
            fo = soup.find("FOUNDER").text
            ft = soup.find("FOUNDEDTIME").text
            fa = soup.find("FOUNDED").text
            fla = soup.find("FLAG").text
            dev = soup.find("DELEGATEVOTES").text
            dea = soup.find("DELEGATEAUTH").text
            de = soup.find("DELEGATE").text
            ra = requests.get(fla)
            file = open("rflag.png", "wb")
            file.write(ra.content)
            file.close()
            region = region.replace(" ", "_")
            color_thief = ColorThief("flag.png")
            dominant_color = color_thief.get_color(quality=1)
            print(dominant_color)
            ra = int(dominant_color[0])
            gb = int(dominant_color[1])
            bd = int(dominant_color[2])

            de = de.replace("_", " ")
            fo = fo.replace("_", " ")
            if fa == "0":
                f = "Antiquity (no records found pre-2010)"
            else:
                f = fa
            print(f)
            if fo == "0":
                fou = "founderless region"
            else:
                fou = fo
            print(fou)
            if "X" in dea:
                b = "executive delegate"
            else:
                b = "non executive delegate"
            if de == "0":
                deli = "no delegate elected"
            else:
                deli = de + " ( " + dev + " ) " + b
            embed = discord.Embed(color=discord.Color.from_rgb(ra, gb, bd))
            embed.set_author(
                name=name, url=f"https://www.nationstates.net/region={region}"
            )
            embed.set_thumbnail(url=fla)
            embed.add_field(name="Founder", value=fou, inline=True)
            embed.add_field(name="Population", value=numnat, inline=False)
            embed.add_field(name="Founded ", value=f, inline=True)
            embed.add_field(name="delegate", value=deli, inline=True)
            embed.add_field(name="Region power", value=p, inline=True)
            embed.set_footer(text="contact @balasai#2438 for more queries")
            await ctx.send(embed=embed)
        else:
            await ctx.send(
                "Your server is not autorised to use this contact balasai to get access this is only to make sure that no one will Misuse bot"
            )


def setup(bot):
    bot.add_cog(Region(bot))
