from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.infrastructure.clients import get_s3_client


@asynccontextmanager
async def lifespan(app: FastAPI):
    s3_client = get_s3_client()
    await s3_client.check_or_create_bucket()
    yield
