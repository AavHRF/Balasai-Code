import discord
from bs4 import BeautifulSoup as b
from discord.ext import commands
import requests
import json


class nendo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def nendo(self, ctx, nation):
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
            r = requests.get(
                f"https://www.nationstates.net/cgi-bin/api.cgi?nation={nation}&q=region",
                headers=headers,
            ).text
            print("all nation sucessful")

            c = b(r, "xml")
            i = c.find("REGION").text
            region = i.replace("_", " ")

            s = requests.get(
                f"https://www.nationstates.net/cgi-bin/api.cgi?region={region}&q=nations",
                headers=headers,
            ).text

            e = b(s, "xml")
            f = e.find("NATIONS").text
            f = f.replace("_", " ")
            f = f.split(":")

            t = requests.get(
                f"https://www.nationstates.net/cgi-bin/api.cgi?nation={nation}&q=endorsements",
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
            print(g)

            j = len(list(g))
            v = list(g)
            v = ", ".join(v)
            await ctx.message.channel.send(
                f"People Endorsing {nation} are:({n})\n{ze}\n\nPeople not endorsing {nation} are:({j}){v}"
            )
        else:
            await ctx.message.channel.send(
                "Your server is not autorised to use this contact balasai to get access this is only to make sure that no one will Misuse bot "
            )


def setup(bot):
    bot.add_cog(nendo(bot))
