print("START.PY LOADED")
from pyrogram import Client, filters
from pyrogram.types import Message

from database import users


async def add_user(user_id):
    user = await users.find_one({"_id": user_id})

    if not user:
        await users.insert_one(
            {
                "_id": user_id
            }
        )


@Client.on_message(filters.private & filters.command("start"))
async def start_command(client, message: Message):
    await add_user(message.from_user.id)

    total_users = await users.count_documents({})

    text = f"""
👋 Hello {message.from_user.mention}

🤖 Welcome to Rename Bot

✅ Rename Videos
✅ Rename Documents
✅ Batch Rename
✅ Custom Thumbnail
✅ Custom Caption
✅ Auto Metadata

📊 Total Users: {total_users}
"""

    await message.reply_text(text)
