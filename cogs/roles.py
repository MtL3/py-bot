import asyncio

import discord
from discord.ext import commands

CONTRIBUTER_ROLE = 752546647191453768


class Roles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    async def toggle_role(self, ctx, role_id):
        # If user has contributer role, remove it
        if any(r.id == role_id for r in ctx.author.roles):
            try:
                await ctx.author.remove_roles(discord.Object(id=role_id))
            except:
                # Raised exception
                await ctx.message.add_reaction('\N{NO ENTRY SIGN}')
            else:
                # Passed
                await ctx.message.add_reaction('\N{HEAVY MINUS SIGN}')
            finally:
                return
        # If user has no contributer role, add it
        try:
            await ctx.author.add_roles(discord.Object(id=role_id))
        except:
            # Raised exception
            await ctx.message.add_reaction('\N{NO ENTRY SIGN}')
        else:
            # Passed
            await ctx.message.add_reaction('\N{HEAVY PLUS SIGN}')
    
    @commands.command(hidden=True)
    async def contribute(self, ctx):
        """Allows you to opt-in to being a contributer for the bot"""
        # Toggle the role and delete command after 5 seconds
        await self.toggle_role(ctx, CONTRIBUTER_ROLE)
        await ctx.message.delete(delay=5)

def setup(bot):
    bot.add_cog(Roles(bot))
