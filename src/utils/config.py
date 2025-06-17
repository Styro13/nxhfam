"""Configuration utilities for environment variables."""

import os
from typing import Optional


def get_env(name: str, default: Optional[str] = None) -> str:
    """Return the environment variable value or default.

    Parameters
    ----------
    name: str
        Name of the environment variable to retrieve.
    default: Optional[str]
        Fallback value if the variable is not set.

    Returns
    -------
    str
        The environment variable's value.
    """
    value = os.getenv(name, default)
    if value is None:
        raise RuntimeError(f"Missing environment variable: {name}")
    return value
