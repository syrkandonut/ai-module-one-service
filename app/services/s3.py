from fastapi import UploadFile

from app import utilities
from app.api.consts import MAX_FILE_SIZE_S3, AllowExtensionsS3
from app.exceptions.s3 import (
    S3ServiceEmptyFileName,
    S3ServiceFileExtentionNotAllowed,
    S3ServiceFileTooLarge,
)
from app.infrastructure.clients.s3 import S3Client


class S3Service:
    def __init__(self, s3_client: S3Client) -> None:
        self.s3_client = s3_client

    async def upload_file(self, file: UploadFile):
        file_content = await utilities.file_to_bytes(file)
        file_size = await utilities.get_file_size(file)

        if not file.filename:
            raise S3ServiceEmptyFileName(detail='Empty file name')

        extention = file.filename.split('.')[-1].upper() if '.' in file.filename else ''
        if extention not in AllowExtensionsS3:
            raise S3ServiceFileExtentionNotAllowed(
                detail=f'File extention not in {
                    [extention.value for extention in AllowExtensionsS3]
                }',
            )

        if file_size and file_size > MAX_FILE_SIZE_S3:
            raise S3ServiceFileTooLarge(
                detail=f'File is too large {file_size} > {MAX_FILE_SIZE_S3} bytes',
            )

        await self.s3_client.upload_file(
            filename=file.filename,
            file_content=file_content,
        )

    async def get_file_content(self, filename: str) -> str:
        return await self.s3_client.get_file_content(filename)  # type: ignore
