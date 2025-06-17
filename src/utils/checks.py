"""Common permission checks used across cogs."""

from discord.ext import commands


def is_admin() -> commands.check:
    """Check if the invoking user has administrator permissions.

    Returns
    -------
    commands.check
        A decorator that can be applied to commands to restrict them to
        administrators only.
    """

    async def predicate(ctx: commands.Context) -> bool:
        return ctx.author.guild_permissions.administrator

    return commands.check(predicate)
