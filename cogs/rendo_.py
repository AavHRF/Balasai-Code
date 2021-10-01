import discord
from bs4 import BeautifulSoup as b
from discord.ext import commands
import requests
import json


class rendo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def rendo(self, ctx, *, region):
        with open("generalaccess.json", "r") as f:
            data = json.load(f)
            print(data)
            print(ctx.guild.id)
        if str(ctx.guild.id) in list(data):
            headers = {"User-Agent": "Balasai"}
            r = requests.get(
                "https://www.nationstates.net/cgi-bin/api.cgi?wa=1&q=members",
                headers=headers,
            ).text
            print("all wa sucessful")

            c = b(r, "xml")
            d = c.find("MEMBERS").text
            d = d.replace("_", " ")
            d = d.split(",")

            s = requests.get(
                f"https://www.nationstates.net/cgi-bin/api.cgi?region={region}&q=nations",
                headers=headers,
            ).text
            e = b(s, "xml")
            f = e.find("NATIONS").text
            f = f.replace("_", " ")
            f = f.split(":")
            t = requests.get(
                f"https://www.nationstates.net/cgi-bin/api.cgi?region={region}&q=delegate",
                headers=headers,
            ).text
            print("delegate sucessful")

            I = b(t, "xml")
            h = I.find("DELEGATE").text
            h = h.replace("_", " ")

            t = requests.get(
                f"https://www.nationstates.net/cgi-bin/api.cgi?nation={h}&q=endorsements",
                headers=headers,
            ).text
            u = b(t, "xml")

            print("deligate endorsements sucessful")
            z = u.find("ENDORSEMENTS").text
            z = z.replace("_", " ")
            z = z.split(",")
            n = len(z)
            ze = ", ".join(z)
            wa = set(f) & set(d)
            g = wa - set(z)
            j = len(list(g))
            v = list(g)
            v = ", ".join(v)
            await ctx.message.channel.send(
                f"People Endorsing Delegate are:({n})\n{ze}\n\nPeople not endorsing delegate are:({j}){v}"
            )
        else:
            await ctx.channel.send(
                "Your server is not autorised to use this contact balasai to get access this is only to make sure that no one will Misuse bot"
            )


def setup(bot):
    bot.add_cog(rendo(bot))
