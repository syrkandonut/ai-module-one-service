from pydantic_settings import BaseSettings, SettingsConfigDict

from .llama import LlamaSettings
from .server import ServerSettings


class Settings(BaseSettings):
    server: ServerSettings = ServerSettings()
    llm: LlamaSettings = LlamaSettings()

    model_config = SettingsConfigDict(
        env_file='../.env',
        env_file_encoding='utf-8',
        extra='ignore',
    )


settings = Settings()
