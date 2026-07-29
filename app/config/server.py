from pydantic import Field
from pydantic_settings import BaseSettings


class ServerSettings(BaseSettings):
    debug: bool = Field(default=False, alias='DEBUG')
