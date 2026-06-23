from pyrogram import Client, filters
from pyrogram.types import Message

from database import captions

WAITING_CAPTION = set()


@Client.on_message(filters.private & filters.command("setcaption"))
async def set_caption_cmd(client: Client, message: Message):
    WAITING_CAPTION.add(message.from_user.id)

    await message.reply_text(
        "✍️ Send your custom caption.\n\n"
        "Available variables:\n"
        "{filename}\n"
        "{filesize}"
    )


@Client.on_message(filters.private & filters.text & ~filters.command(["setcaption", "delcaption", "start"]))
async def save_caption(client: Client, message: Message):
    user_id = message.from_user.id

    if user_id not in WAITING_CAPTION:
        return

    WAITING_CAPTION.remove(user_id)

    await captions.update_one(
        {"_id": user_id},
        {"$set": {"caption": message.text}},
        upsert=True
    )

    await message.reply_text(
        "✅ Caption saved successfully."
    )


@Client.on_message(filters.private & filters.command("delcaption"))
async def delete_caption(client: Client, message: Message):
    await captions.delete_one(
        {"_id": message.from_user.id}
    )

    await message.reply_text(
        "🗑 Caption deleted successfully."
    )
