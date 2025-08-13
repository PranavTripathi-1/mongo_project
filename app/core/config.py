# app/core/config.py
import os
from dotenv import load_dotenv

# Load .env if it exists
load_dotenv()

class Settings:
    MONGO_URI: str = os.getenv("MONGO_URI", "mongodb://localhost:27017")
    DB_NAME: str = os.getenv("DB_NAME", "testdb")

settings = Settings()
