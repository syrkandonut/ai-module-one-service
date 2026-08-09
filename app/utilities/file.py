import asyncio
import io
import os

import mammoth  # type: ignore[import-untyped]
from fastapi import UploadFile


async def file_to_bytes(file: UploadFile) -> bytes:
    return await file.read()


async def get_file_size(file: UploadFile) -> int:
    file.file.seek(0, os.SEEK_END)
    file_size = file.file.tell()
    file.file.seek(0)

    return file_size


def _bytes_to_text(file_bytes: bytes) -> str:
    with io.BytesIO(file_bytes) as file_stream:
        return mammoth.convert_to_markdown(file_stream).value  # type: ignore


async def get_text(file_bytes: bytes) -> str:
    return await asyncio.to_thread(_bytes_to_text, file_bytes)
