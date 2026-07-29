from pydantic import Field
from pydantic_settings import BaseSettings


class LlamaSettings(BaseSettings):
    host: str = Field(default="http://localhost:11434", alias="LLM_HOST")
    model: str = Field(default="llama3.2:3b", alias="LLM_MODEL")
