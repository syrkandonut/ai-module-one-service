from pydantic_settings import BaseSettings, SettingsConfigDict

from .llama import LlamaSettings
from .s3 import S3Settings
from .server import ServerSettings


class Settings(BaseSettings):
    server: ServerSettings = ServerSettings()
    llm: LlamaSettings = LlamaSettings()
    s3: S3Settings = S3Settings()

    model_config = SettingsConfigDict(
        env_file='../.env',
        env_file_encoding='utf-8',
        extra='ignore',
    )


settings = Settings()
