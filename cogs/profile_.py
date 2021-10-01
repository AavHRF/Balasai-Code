from discord.ext import commands
import json
import discord


class profile(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["profile"])
    async def userinfo(self, ctx, member: discord.Member = None):
        with open("generalaccess.json", "r") as f:
            data = json.load(f)
            print(data)
            print(ctx.guild.id)
        if str(ctx.guild.id) in list(data):

            if member is None:
                member = ctx.author
                roles = [role for role in ctx.author.roles]
            else:
                roles = [role for role in member.roles]

            embed = discord.Embed(
                title=f"{member}",
                colour=member.colour,
                timestamp=ctx.message.created_at,
            )
            embed.set_footer(
                text=f"Requested by: {ctx.author}", icon_url=ctx.author.avatar_url
            )
            embed.set_author(name="User Info: ")
            embed.add_field(name="Discord ID:", value=member.id, inline=False)
            embed.add_field(name="Name", value=member.display_name, inline=False)
            # embed.add_field(name="Discriminator?:",value=member.discriminator, inline=False)
            embed.add_field(
                name="Joined Discod:",
                value=member.created_at.strftime("%a, %d, %B, %Y, %I, %M, %p UTC"),
                inline=False,
            )
            embed.add_field(
                name="Joined Server:",
                value=member.joined_at.strftime("%a, %d, %B, %Y, %I, %M, %p UTC"),
                inline=False,
            )
            embed.add_field(
                name=f"Roles [{len(roles)}]",
                value=" **|** ".join([role.mention for role in roles]),
                inline=False,
            )
            embed.add_field(name="Top Role?:", value=member.top_role, inline=False)
            embed.add_field(name="User is a bot?:", value=member.bot, inline=False)
            embed.set_thumbnail(url=member.avatar_url)
            nations = ""
            try:
                for nation in json.loads(open("ver.json", "r+").read())[str(member.id)]:
                    nations += "[{0}]({1}), ".format(
                        nation,
                        "https://www.nationstates.net/nation={0}".format(
                            nation.replace(" ", "_")
                        ),
                    )
            except KeyError:
                pass
            if not nations:
                nations = "{0} doesn't own any nations".format(member.mention)
            embed.add_field(name="Verified Nations", value=nations, inline=False)
            await ctx.send(embed=embed)
        else:
            await ctx.channel.send(
                "Your server is not autorised to use this contact balasai to get access this is only to make sure that no one will Misuse bot"
            )


def setup(bot):
    bot.add_cog(profile(bot))
