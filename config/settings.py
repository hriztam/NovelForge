import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    GOOGLE_API_KEY = os.getenv("AIzaSyCriYgozr7OGxuVFJdXdZgMBIxmWwHmCg8")
    CHROMA_PATH = "./storage/chroma_db"
    SCREENSHOT_DIR = "./storage/screenshots"
    MAX_ITERATIONS = 3
    LLM_MODEL = "gemini-pro"

settings = Settings()