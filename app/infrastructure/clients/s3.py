from contextlib import asynccontextmanager
from typing import AsyncGenerator

from aiobotocore.session import AioBaseClient, get_session
from botocore.errorfactory import ClientError

from app import utilities
from app.config import settings

from .handlers import s3_handler


class S3Client:
    def __init__(self):
        self.access_id = settings.s3.access_id
        self.access_secret = settings.s3.access_secret
        self.bucket_name = settings.s3.bucket_name

        self.host = settings.s3.host
        self.port = settings.s3.port
        self.base_url = f'http://{self.host}:{self.port}'

        self.session = get_session()

    @asynccontextmanager
    async def _client(self) -> AsyncGenerator[AioBaseClient, None]:
        async with self.session.create_client(
            's3',
            endpoint_url=self.base_url,
            aws_access_key_id=self.access_id,
            aws_secret_access_key=self.access_secret,
            use_ssl=False,
        ) as client:
            yield client

    @s3_handler
    async def upload_file(self, filename: str, file_content: bytes) -> None:
        async with self._client() as client:
            await client.put_object(
                Bucket=self.bucket_name,
                Key=filename,
                Body=file_content,
            )

    @s3_handler
    async def get_file_content(self, filename: str) -> str:
        async with self._client() as client:
            response = await client.get_object(Bucket=self.bucket_name, Key=filename)
            async with response['Body'] as stream:
                file_bytes = await stream.read()

        return await utilities.get_text(file_bytes)

    @s3_handler
    async def check_or_create_bucket(self) -> None:
        async with self._client() as client:
            try:
                await client.head_bucket(Bucket=self.bucket_name)
            except ClientError:
                await client.create_bucket(Bucket=self.bucket_name)
