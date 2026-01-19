import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

class Config:
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "default_api_key")
    GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini/gemini-2.0-flash")
    # Get project root and construct DB path
    BASE_DIR = Path(__file__).resolve().parent
    DB_PATH = str(BASE_DIR / "inventory.duckdb")

settings = Config()