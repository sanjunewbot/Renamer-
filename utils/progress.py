import time

progress_cache = {}

async def progress(current, total, message, start_time, action):

    now = time.time()

    if round(now - progress_cache.get(message.id, 0)) < 5:
        return

    progress_cache[message.id] = now

    percentage = current * 100 / total

    try:
        await message.edit_text(
            f"{action}\n\n"
            f"📦 {percentage:.1f}%\n"
            f"{current}/{total}"
        )
    except:
        pass
