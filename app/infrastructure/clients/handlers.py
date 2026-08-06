from functools import wraps

from botocore.exceptions import ClientError

from app.exceptions.s3 import S3ClientError


def s3_handler(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except ClientError as s3_error:
            detail = s3_error.response.get('Error', {}).get('Code') or 'UnknownError'
            raise S3ClientError(detail=detail)

    return wrapper
