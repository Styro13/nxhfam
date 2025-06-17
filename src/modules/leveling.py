"""User leveling system."""

from discord.ext import commands

from ..utils.database import Database


class Leveling(commands.Cog):
    """Cog that tracks XP and levels."""

    def __init__(self, bot: commands.Bot, db: Database) -> None:
        """Keep references to bot and database for listeners and commands."""
        self.bot = bot
        self.db = db

    # Placeholder for event listeners and commands. XP logic should be handled
    # here and persisted using ``self.db`` for each user.


async def setup(bot: commands.Bot) -> None:
    """Load the cog."""
    db = Database()
    await bot.add_cog(Leveling(bot, db))
