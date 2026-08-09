from fastapi import FastAPI

from app.api.s3 import router as s3_router
from app.api.ai import router as ai_router
from app.config import settings

from .exc_handlers import init_global_exception_handler, init_s3_exception_handlers
from .lifespan import lifespan


def create_app():
    app = FastAPI(
        title='AI module',
        docs_url='/api/docs',
        description='AI module one',
        debug=settings.server.debug,
        lifespan=lifespan,
    )

    init_s3_exception_handlers(app)
    init_global_exception_handler(app)

    app.include_router(s3_router)
    app.include_router(ai_router)

    return app
