import discord
from bs4 import BeautifulSoup
from discord.ext import commands
import requests


class suggestions(commands.Cog):
    def __init__(self, bot):

        self.bot = bot
        CHANNEL_ID = "892336999879548938"

    @commands.command()
    async def suggest(ctx, command, *, description):
        ": Suggest a command. Provide the command name and description"
        embed = discord.Embed(
            title="Command Suggestion",
            description=f"Suggested by: {ctx.author.mention}\nCommand Name: *{command}*",
            color=discord.Color.green(),
        )
        embed.add_field(name="Description", value=description)
        channel = ctx.guild.get_channel(CHANNEL_ID)
        msg = await channel.send(embed=embed)
        await msg.add_reaction("👍")
        await msg.add_reaction("👎")


def setup(bot):
    bot.add_cog(suggestions(bot))
