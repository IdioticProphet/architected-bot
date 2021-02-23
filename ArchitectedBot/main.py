import discord
import logging
import os
from discord.ext import commands

from .cogs.ArchitectCog import ArchitectCog

TOKEN = open(os.getcwd()+os.path.sep+"token").read()


def main():
    logging.basicConfig(level=logging.INFO)
    bot = commands.Bot("!!!!!!!!")
    bot.add_cog(ArchitectCog(bot))
    bot.run(TOKEN)


if __name__ == "__main__":
    main()
