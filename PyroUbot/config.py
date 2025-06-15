import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "30"))

DEVS = list(map(int, os.getenv("DEVS", "5870285414").split()))

API_ID = int(os.getenv("API_ID", "26544005"))

API_HASH = os.getenv("API_HASH", "66f6221e5ce9109827b50eaf3d105025")

BOT_TOKEN = os.getenv("BOT_TOKEN", "8016103678:AAFIU9Yq-S2NOXqO94CJ3hoA4soXfwDyKRE")

OWNER_ID = int(os.getenv("OWNER_ID", "5870285414"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002615817338").split()))

RMBG_API = os.getenv("RMBG_API", "a6qxsmMJ3CsNo7HyxuKGsP1o")

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://naura:ahahahahaha@naura.al4xuyo.mongodb.net/?retryWrites=true&w=majority&appName=naura")

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-1002554488354"))
