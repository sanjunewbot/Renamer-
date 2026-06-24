from pyrogram import Client, filters

print("START.PY LOADED")

@Client.on_message(filters.command("start"))
async def start_command(client, message):
    print("START COMMAND TRIGGERED")
    await message.reply_text("Bot Working ✅")
