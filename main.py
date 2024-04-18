import os
import pathlib
import settings
import discord
from discord.ext import commands

base_dir = pathlib.Path(__file__).parent
cmds_dir = base_dir / "cmds"

def run():
    Intents = discord.Intents.all()

    bot = commands.Bot(command_prefix="!",intents=Intents)

    @bot.event
    async def on_ready():
        print(bot.user, bot.user.id)
        for file in cmds_dir.glob("*.py"):
            file.name != "__init__.py"
            await bot.load_extension(f"cmds.{file.name[:-3]}")
        await bot.tree.sync()


    bot.run(settings.TOKEN)

if __name__ == "__main__":
    run()