# File: mute.py

import discord
from discord.ext import commands

from ..logging.log_actions import log_mute_action

class Mute(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='mute', help='Mute a user in the server')
    async def mute_user(self, ctx, member: discord.Member, *, reason=None):
        if ctx.message.author.guild_permissions.manage_messages:
            # Mute the user
            await member.add_roles(discord.utils.get(ctx.guild.roles, name='Muted'))
            await ctx.send(f'{member.mention} has been muted.')
            # Log the mute action
            await log_mute_action(ctx.guild, ctx.author, member, reason)
        else:
            await ctx.send('You do not have the required permissions to mute users.')

def setup(bot):
    bot.add_cog(Mute(bot))