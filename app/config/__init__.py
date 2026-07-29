from pydantic_settings import BaseSettings, SettingsConfigDict

from .llama import LlamaSettings


class Settings(BaseSettings):
    llm: LlamaSettings = LlamaSettings()

    model_config = SettingsConfigDict(
        env_file="../.env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()
