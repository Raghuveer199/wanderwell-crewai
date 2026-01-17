import duckdb
from crewai.tools import BaseTool
from pydantic import PrivateAttr
from config import settings

class DuckDBReadOnlyTool(BaseTool):
    """
    DuckDB reader tool with strict read-only enforcement.
    Designed for chaotic agent swarms that generate dynamic SQL.
    """

    name: str = "duckdb_reader"
    description: str = (
        "Execute READ-ONLY SQL queries against DuckDB inventory. "
        "ONLY single-statement SELECT queries are allowed. "
        "Use this tool to explore vendors, experiences, stays, rooms, vehicles, and tickets."
    )

    # Pydantic Private Attribute for non-field
    _db_path: str = PrivateAttr()

    def __init__(self):
        super().__init__()
        self._db_path = settings.DB_PATH

    def _run(self, query: str) -> str:
        cleaned = query.strip().lower()

        if not cleaned.startswith("select"):
            return (
                "ERROR: Only SELECT statements are allowed. "
                "Do not attempt inserts, updates, deletes, or DDL."
            )

        # Prevent multi-statement execution
        if ";" in cleaned.rstrip(";"):
            return "ERROR: Multiple SQL statements are not allowed."

        try:
            con = duckdb.connect(
                database=self._db_path,
                read_only=True
            )

            df = con.execute(query).fetchdf()

            if df.empty:
                return "Query executed successfully, but no rows were returned."

            return df.to_markdown(index=False)

        except Exception as e:
            return f"QUERY ERROR: {str(e)}"

        finally:
            try:
                con.close()
            except Exception:
                pass
