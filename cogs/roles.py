import asyncio

import discord
from discord.ext import commands

CONTRIBUTER_ROLE = 752546647191453768


class Roles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    async def toggle_role(self, ctx, role_id):
        if any(r.id == role_id for r in ctx.author.roles):
            try:
                await ctx.author.remove_roles(discord.Object(id=role_id))
            except:
                await ctx.message.add_reaction('\N{NO ENTRY SIGN}')
            else:
                await ctx.message.add_reaction('\N{HEAVY MINUS SIGN}')
            finally:
                return

        try:
            await ctx.author.add_roles(discord.Object(id=role_id))
        except:
            await ctx.message.add_reaction('\N{NO ENTRY SIGN}')
        else:
            await ctx.message.add_reaction('\N{HEAVY PLUS SIGN}')
    
    @commands.command(hidden=True)
    async def contribute(self, ctx):
        """Allows you to opt-in to being a contributer for the bot"""
        await self.toggle_role(ctx, CONTRIBUTER_ROLE)

def setup(bot):
    bot.add_cog(Roles(bot))
