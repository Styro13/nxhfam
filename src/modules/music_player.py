"""Music playback commands."""

from discord.ext import commands

from ..utils.database import Database


class MusicPlayer(commands.Cog):
    """Cog that streams audio from YouTube links."""

    def __init__(self, bot: commands.Bot, db: Database) -> None:
        self.bot = bot
        self.db = db
        self.queue = []

    # Placeholder for music commands


async def setup(bot: commands.Bot) -> None:
    """Load the cog."""
    db = Database()
    await bot.add_cog(MusicPlayer(bot, db))
