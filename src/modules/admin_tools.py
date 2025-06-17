"""Administrator utilities for managing the server."""

from discord.ext import commands

from ..utils.database import Database


class AdminTools(commands.Cog):
    """Cog containing administrator commands."""

    def __init__(self, bot: commands.Bot, db: Database) -> None:
        self.bot = bot
        self.db = db

    # Placeholder for admin commands


async def setup(bot: commands.Bot) -> None:
    """Load the cog."""
    db = Database()
    await bot.add_cog(AdminTools(bot, db))
