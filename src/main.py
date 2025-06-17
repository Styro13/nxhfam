"""Entry point for running the Aegis bot."""

import asyncio
from importlib import import_module

from discord.ext import commands

from .utils.config import get_env
from .utils.logger import setup_logger


MODULES = [
    "modules.voice_manager",
    "modules.economy",
    "modules.leveling",
    "modules.admin_tools",
    "modules.music_player",
]


def load_modules(bot: commands.Bot) -> None:
    """Dynamically load all modules listed in MODULES."""
    for module in MODULES:
        bot.load_extension(module)


def main() -> None:
    """Start the bot."""
    token = get_env("AEGIS_TOKEN")
    logger = setup_logger()

    bot = commands.Bot(command_prefix="!", intents=commands.Intents.all())

    load_modules(bot)

    logger.info("Starting Aegis bot")
    bot.run(token)


if __name__ == "__main__":
    main()
