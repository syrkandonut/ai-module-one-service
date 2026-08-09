from fastapi import FastAPI, HTTPException, Request, status

from app.exceptions import ai as ai_exc
from app.exceptions import s3 as s3_exc
from app.infrastructure.clients.consts import S3ErrorDetail


def init_s3_exception_handlers(app: FastAPI) -> None:

    @app.exception_handler(s3_exc.S3ServiceError)
    async def s3_service_exception_handler(
        request: Request, exc: s3_exc.S3ServiceError
    ) -> None:
        if isinstance(
            exc,
            (
                s3_exc.S3ServiceEmptyFileName,
                s3_exc.S3ServiceFileExtentionNotAllowed,
            ),
        ):
            status_code = status.HTTP_400_BAD_REQUEST
        elif isinstance(exc, s3_exc.S3ServiceFileTooLarge):
            status_code = status.HTTP_413_CONTENT_TOO_LARGE
        else:
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR

        raise HTTPException(status_code=status_code, detail=exc.detail)

    @app.exception_handler(s3_exc.S3ClientError)
    async def s3_client_exception_handler(
        request: Request, exc: s3_exc.S3ClientError
    ) -> None:
        if exc.detail == S3ErrorDetail.NoSuchKey:
            status_code = status.HTTP_404_NOT_FOUND
        elif exc.detail == S3ErrorDetail.EntityTooLarge:
            status_code = status.HTTP_413_CONTENT_TOO_LARGE
        else:
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR

        raise HTTPException(
            status_code=status_code,
            detail={
                'client': 's3',
                'code': f'{exc.detail}',
            },
        )

    @app.exception_handler(ai_exc.LLMError)
    async def ai_service_exception_handler(
        request: Request,
        exc: ai_exc.LLMError,
    ) -> None:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=exc.detail
        )


def init_global_exception_handler(app: FastAPI) -> None:

    @app.exception_handler(Exception)
    async def global_exception_handler(request: Request, exc: Exception):
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f'Internal server error: {str(exc)}',
        )
