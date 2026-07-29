from fastapi import FastAPI

from app.config import settings


def create_app():
    return FastAPI(
        title='AI module',
        docs_url='/api/docs',
        description='AI module one',
        debug=settings.server.debug,
    )
