from pydantic import Field
from pydantic_settings import BaseSettings


class S3Settings(BaseSettings):
    host: str = Field(alias='MINIO_HOST')
    port: str = Field(alias='MINIO_PORT')
    access_id: str = Field(alias='MINIO_USER')
    access_secret: str = Field(alias='MINIO_PASSWORD')
    bucket_name: str = 'docs-bucket'
