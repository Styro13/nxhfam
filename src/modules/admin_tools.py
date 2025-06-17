"""Administrator utilities for managing the server."""

from discord.ext import commands

from ..utils.database import Database
from ..utils import is_admin


class AdminTools(commands.Cog):
    """Cog containing administrator commands."""

    def __init__(self, bot: commands.Bot, db: Database) -> None:
        """Initialize the cog with the running bot and database connection."""
        self.bot = bot
        self.db = db

    # Placeholder for admin commands. Permission checks should utilize helper
    # functions from ``src.utils.checks`` once implemented.

    @commands.command()
    @is_admin()
    async def ping(self, ctx: commands.Context) -> None:
        """Simple command to verify the bot is responsive."""
        await ctx.send("Pong!")


async def setup(bot: commands.Bot) -> None:
    """Load the cog."""
    db = Database()
    await bot.add_cog(AdminTools(bot, db))
