"""Database helper using sqlite3 for persistence."""

from __future__ import annotations

import sqlite3
from typing import Any


class Database:
    """Simple wrapper around sqlite3 for executing queries."""

    def __init__(self, path: str | None = None) -> None:
        """Open a connection to the database."""
        self.path = path or 'aegis.db'
        self.conn = sqlite3.connect(self.path)
        self.conn.row_factory = sqlite3.Row

    def execute(self, query: str, params: tuple[Any, ...] | None = None) -> sqlite3.Cursor:
        """Execute a SQL statement with optional parameters.

        Parameters
        ----------
        query: str
            The SQL query to run.
        params: tuple[Any, ...] | None
            Parameters for the SQL query, if any.

        Returns
        -------
        sqlite3.Cursor
            Cursor positioned after executing the statement.
        """
        cur = self.conn.cursor()
        cur.execute(query, params or ())
        self.conn.commit()
        return cur

    def close(self) -> None:
        """Gracefully close the underlying SQLite connection."""
        self.conn.close()
