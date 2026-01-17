import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "default_api_key")
    GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini/gemini-2.0-flash")
    DB_PATH = r"C:\Users\medap\OneDrive\Desktop\Raghuveer\BITSoM\wanderwall-swarm\inventory-swarm\inventory.duckdb"

settings = Config()