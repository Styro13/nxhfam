"""Configuration utilities for environment variables."""

import os
from typing import Optional


def get_env(name: str, default: Optional[str] = None) -> str:
    """Return the environment variable value or default."""
    value = os.getenv(name, default)
    if value is None:
        raise RuntimeError(f"Missing environment variable: {name}")
    return value
