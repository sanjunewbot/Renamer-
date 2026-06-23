from pyrogram import Client, filters
from pyrogram.types import Message

from database import thumbs


@Client.on_message(filters.private & filters.command("setthumb"))
async def set_thumb_cmd(client: Client, message: Message):
    await message.reply_text(
        "🖼 Send me a photo that you want to save as your thumbnail."
    )


@Client.on_message(filters.private & filters.photo)
async def save_thumb(client: Client, message: Message):
    user_id = message.from_user.id

    file_id = message.photo.file_id

    await thumbs.update_one(
        {"_id": user_id},
        {"$set": {"file_id": file_id}},
        upsert=True
    )

    await message.reply_text(
        "✅ Thumbnail saved successfully."
    )


@Client.on_message(filters.private & filters.command("delthumb"))
async def del_thumb(client: Client, message: Message):
    user_id = message.from_user.id

    await thumbs.delete_one({"_id": user_id})

    await message.reply_text(
        "🗑 Thumbnail deleted successfully."
    )
