import discord
from discord.ext import commands

@commands.hybrid_command(description="ping pong!")
async def ping(ctx):
    await ctx.send("pong!", ephemeral=True)

async def setup(bot):
    bot.add_command(ping)