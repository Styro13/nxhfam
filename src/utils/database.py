"""Database helper using sqlite3 for persistence."""

from __future__ import annotations

import sqlite3
from typing import Any


class Database:
    """Simple wrapper around sqlite3 for executing queries."""

    def __init__(self, path: str | None = None) -> None:
        self.path = path or 'aegis.db'
        self.conn = sqlite3.connect(self.path)
        self.conn.row_factory = sqlite3.Row

    def execute(self, query: str, params: tuple[Any, ...] | None = None) -> sqlite3.Cursor:
        """Execute a query and return the cursor."""
        cur = self.conn.cursor()
        cur.execute(query, params or ())
        self.conn.commit()
        return cur

    def close(self) -> None:
        """Close the database connection."""
        self.conn.close()
