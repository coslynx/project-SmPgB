# ban.py

import discord
from discord.ext import commands

class Ban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='ban', help='Ban a user from the server')
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        try:
            await member.ban(reason=reason)
            await ctx.send(f'{member.mention} has been banned from the server.')
        except discord.Forbidden:
            await ctx.send('I do not have permission to ban this user.')
        except discord.HTTPException:
            await ctx.send('An error occurred while processing the ban.')

def setup(bot):
    bot.add_cog(Ban(bot))