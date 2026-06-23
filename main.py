import asyncio
from pyrogram import Client, idle
from config import API_ID, API_HASH, BOT_TOKEN
from webserver import start_webserver

app = Client(
    "RenameBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="handlers")
)

async def main():
    await start_webserver()
    await app.start()
    print("Bot Started")
    await idle()
    await app.stop()

app.run(main())
