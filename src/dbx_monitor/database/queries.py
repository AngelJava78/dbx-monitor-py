from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[3]
SQL_DIR = BASE_DIR / "sql"


def load_sql(filename: str) -> str:
    sql_path = SQL_DIR / filename

    if not sql_path.exists():
        raise FileNotFoundError(f"SQL file does not exist: {sql_path}")

    return sql_path.read_text(encoding="utf-8")
