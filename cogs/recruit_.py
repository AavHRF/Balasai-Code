import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup as b
import html
import asyncio
import xml.etree.ElementTree as ET
import json


class recruit(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def recruit(self, ctx, nation, tgid, region):
        with open("recruitaccess.json", "r") as f:
            data = json.load(f)
            print(data)
            print(ctx.guild.id)
        if str(ctx.guild.id) in list(data):
            message = ctx.message
            await message.delete()
            psmsg = await message.channel.send("ok")
            await psmsg.add_reaction("⏸")
            headers = {"User-Agent": "Nation:{},ns discord bot ".format(nation)}
            URL = "https://www.nationstates.net/cgi-bin/api.cgi"
            url_params = {"q": "newnations"}
            with requests.get(
                URL, headers=headers, params=url_params
            ) as res_newnations:
                root = ET.fromstring(res_newnations.text)
                element = root.find("NEWNATIONS")
                url_params = {"q": "tgcanrecruit", "from": f"{region}"}
            ctx = await self.bot.get_context(message)
            for new_nation in element.text.split(","):
                url_params["nation"] = new_nation.strip()
                await asyncio.sleep(10)
                while (await ctx.fetch_message(psmsg.id)).reactions[0].count > 1:
                    await asyncio.sleep(1)
                with requests.get(
                    URL, headers=headers, params=url_params
                ) as res_nation:
                    root = ET.fromstring(res_nation.text)
                    element = root.find("TGCANRECRUIT")

                    if element.text == "1":
                        embed = discord.Embed(
                            title="Recruit",
                            description="Welcome to recruitment from the bot now you can use the bot for recruiting. ",
                            color=discord.Color.blue(),
                        )
                        embed.add_field(
                            name="nation name", value=new_nation, inline=False
                        )
                        embed.add_field(name="can recruit", value="yes", inline=False)
                        if tgid.startswith("\n"):
                            tgid = tgid[1:]
                        embed.add_field(
                            name="Link to recruit",
                            value=f"[new_nation](https://www.nationstates.net/page=compose_telegram?tgto={new_nation}&message={tgid})",
                        )
                        embed.set_footer(
                            text="contact @balasai#2438 for problems and suggestions"
                        )
                        await message.channel.send(embed=embed)
        else:
            await ctx.channel.send(
                "Your server is not autorised to use this contact balasai to get access this is only to make sure that no one will Misuse bot"
            )


def setup(bot):
    bot.add_cog(recruit(bot))
