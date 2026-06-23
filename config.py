import os

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

MONGO_URI = os.getenv("MONGO_URI")

ADMINS = [int(x) for x in os.getenv("ADMINS", "").split()]

DB_NAME = "RenameBot"

MAX_FILE_SIZE = 2 * 1024 * 1024 * 1024  # 2GB

METADATA_TITLE = "Powered By My Channel"
METADATA_AUTHOR = "My Channel"
METADATA_COMMENT = "Renamed By Bot"
