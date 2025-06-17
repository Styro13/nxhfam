"""Server economy commands and shop management."""

from discord.ext import commands

from ..utils.database import Database


class Economy(commands.Cog):
    """Cog providing currency commands and virtual shop interactions."""

    def __init__(self, bot: commands.Bot, db: Database) -> None:
        self.bot = bot
        self.db = db

    # Placeholder for command implementations


async def setup(bot: commands.Bot) -> None:
    """Load the cog."""
    db = Database()
    await bot.add_cog(Economy(bot, db))
