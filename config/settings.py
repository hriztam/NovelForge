import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY", "default_api_key")
    CHROMA_PATH = "./storage/chroma_db"
    SCREENSHOT_DIR = "./storage/screenshots"
    MAX_ITERATIONS = 3
    LLM_MODEL = "gemini-pro"

settings = Settings()