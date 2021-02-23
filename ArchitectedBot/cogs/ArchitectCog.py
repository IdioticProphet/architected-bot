from discord.ext import commands
from ..utils import was_killed_by_architects


class ArchitectCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.channel.name != "architected":
            return
        if not message.attachments:
            return

        for attachment in message.attachments:
            f = await attachment.read()
            if was_killed_by_architects:
                await message.reply("gitgud")
