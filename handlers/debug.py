from pyrogram import Client, filters

print("DEBUG.PY LOADED")

@Client.on_message(filters.all)
async def debug(client, message):
    print("MESSAGE RECEIVED:", message.text)
