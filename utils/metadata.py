import asyncio
from config import (
    METADATA_TITLE,
    METADATA_AUTHOR,
    METADATA_COMMENT,
    METADATA_COPYRIGHT
)


async def add_metadata(input_file, output_file):

    cmd = [
        "ffmpeg",
        "-i",
        input_file,

        "-metadata",
        f"title={METADATA_TITLE}",

        "-metadata",
        f"author={METADATA_AUTHOR}",

        "-metadata",
        f"comment={METADATA_COMMENT}",

        "-metadata",
        f"copyright={METADATA_COPYRIGHT}",

        "-codec",
        "copy",

        output_file,
        "-y"
    ]

    process = await asyncio.create_subprocess_exec(
        *cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )

    await process.communicate()

    return output_file
