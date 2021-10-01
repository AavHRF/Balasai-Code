import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup
from discord import Color
import html
import aiohttp
import asyncio
import json


class dtr(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def dtr(self, ctx, nation, password, region, channel_name):
        channel = await ctx.guild.create_text_channel(channel_name)
        print(channel.id)
        file = open("dtr.json", "r")
        data = json.load(file)
        data.append({channel.id: [nation, password, region]})
        file = open("dtr.json", "w")
        json.dump(data, file)
        files = open("dtrch.json", "r")
        datas = json.load(files)
        datas.append(channel.id)
        filea = open("dtrch.json", "w")
        json.dump(datas, filea)

    @commands.Cog.listener()
    async def on_message(self, message):
        fla = open("dtrch.json", "r")
        jso = json.load(fla)
        for x in jso:
            if x == str(message.channel.id):
                flan = open("dtr.json", "r")
                jso = json.load(flan)
                nation = channel.id[0]
                password = channel.id[1]
                region = channel.id[2]
                messages = message.channel.last_message.content
                author = message.channel.last_message.author
                print(messages)
                print(author)
                text = f"{author} send message in rmb message is {messages}"
                headers = {"User-Agent": nation, "X-Password": password}
                response = requests.get(
                    f"https://www.nationstates.net/cgi-bin/api.cgi?nation=Balasai&region={region}&c=rmbpost&text={text}&mode=prepare",
                    headers=headers,
                )
                print(response.text)
                headers2 = {"User-Agent": nation, "X-Pin": response.headers["X-Pin"]}
                so = BeautifulSoup(response.text, "xml")
                token = so.find("SUCCESS").text
                print(token)
                response2 = requests.get(
                    f"https://www.nationstates.net/cgi-bin/api.cgi?nation=Balasai&region=the_republic_of_india&c=rmbpost&text={text}&mode=execute&token={token}",
                    headers=headers2,
                )
                print(response2.text)
                print(text)


def setup(bot):
    bot.add_cog(dtr(bot))
