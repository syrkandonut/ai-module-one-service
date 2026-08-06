from .llama import LlamaClient
from .s3 import S3Client

llama_singleton_client = LlamaClient()
s3_singleton_client = S3Client()


def get_llama_client() -> LlamaClient:
    return llama_singleton_client


def get_s3_client() -> S3Client:
    return s3_singleton_client
