import os

API_ID = int(os.getenv("20342933"))
API_HASH = os.getenv("9233e5deebe6abfc9ba297a9678851be")
BOT_TOKEN = os.getenv("8434987797:AAEPMRsydRT81ZqylwjbwFsNwYkQPQ2Z1tA")

MONGO_URI = os.getenv("mongodb+srv://sanjusen212121:dRTWTRgVX19SJwTk@cluster0.2nwk3.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0
")

ADMINS = [int(x) for x in os.getenv("6803963354", "").split()]

DB_NAME = "RenameBot"

MAX_FILE_SIZE = 2 * 1024 * 1024 * 1024  # 2GB

METADATA_TITLE = "Master Exx"
METADATA_AUTHOR = "Master Exx"
METADATA_COMMENT = "Powered By Master Exx"
METADATA_COPYRIGHT = "Master Exx"
