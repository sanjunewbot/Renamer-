from pyrogram import Client, filters
from pyrogram.types import Message

from database import captions
from utils.state import set_state, has_state, clear_state


@Client.on_message(filters.command("setcaption") & filters.private)
async def set_caption(client, message):
    set_state(message.from_user.id, "WAITING_CAPTION")

    await message.reply_text(
        "✍️ Send your custom caption.\n\n"
        "Variables:\n"
        "{filename}\n"
        "{filesize}"
    )


@Client.on_message(filters.private & filters.text)
async def save_caption(client, message):

    if not has_state(message.from_user.id, "WAITING_CAPTION"):
        return

    await captions.update_one(
        {"_id": message.from_user.id},
        {"$set": {"caption": message.text}},
        upsert=True
    )

    clear_state(message.from_user.id)

    await message.reply_text(
        "✅ Caption saved successfully."
    )


@Client.on_message(filters.command("delcaption") & filters.private)
async def del_caption(client, message):

    await captions.delete_one(
        {"_id": message.from_user.id}
    )

    await message.reply_text(
        "🗑 Caption deleted."
    )
