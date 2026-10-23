import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent

load_dotenv(BASE_DIR.parent / ".env")
TOKEN = os.getenv("Miliy_Telegram_Bot")

USERS = {
    os.getenv("botik_id_1") : "Саша",
    os.getenv("botik_id_2") : "Даша"
}
USERS = {username.lower().lstrip('@'): name for username, name in USERS.items()}
DATA_DIR = BASE_DIR / "tmp"
DATA_FILE = DATA_DIR / "invitations.json"