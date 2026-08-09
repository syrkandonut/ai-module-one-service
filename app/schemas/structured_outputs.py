from enum import StrEnum
from typing import TypeVar

from pydantic import BaseModel, Field

StructuredOutputSchema = TypeVar('StructuredOutputSchema', bound=BaseModel)


class ContactInfoSchema(BaseModel):
    hotel: str = Field(description='Hotel name')
    address: str = Field(description='Address')
    tel: str | None = Field(default=None, description='Telephone number')


class ContactsInfoSchema(BaseModel):
    contacts: list[ContactInfoSchema] = Field(
        default_factory=list,
        description='List of extracted hotel contacts',
    )


class Sentiment(StrEnum):
    POSITIVE = 'positive'
    NEGATIVE = 'negative'
    NEUTRAL = 'neutral'
    CALM = 'calm'
    EXCITING = 'exciting'


class ResumeSchema(BaseModel):
    title: str = Field(
        description=('Must come up with a title based on the text'),
    )
    summary: str = Field(description='Brief content of the text')
    tags: list[str] = Field(description='Add a few tags about the text')
    sentiment: Sentiment = Field(description='Sentiment, mood, flow of the text')
