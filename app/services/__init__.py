from fastapi import Depends

from app.infrastructure.clients import (
    LlamaClient,
    S3Client,
    get_llama_client,
    get_s3_client,
)

from .ai import AIService
from .s3 import S3Service


def get_s3_service(s3_client: S3Client = Depends(get_s3_client)) -> S3Service:
    return S3Service(s3_client=s3_client)


def get_ai_service(ai_client: LlamaClient = Depends(get_llama_client)) -> AIService:
    return AIService(ai_client=ai_client)
