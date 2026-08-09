from fastapi import APIRouter, Depends, File, UploadFile, status

from app.schemas.api import UploadedResponse
from app.services import S3Service, get_s3_service

router = APIRouter()


@router.post(
    '/upload', status_code=status.HTTP_201_CREATED, response_model=UploadedResponse
)
async def upload_file(
    file: UploadFile = File(...),
    s3_service: S3Service = Depends(get_s3_service),
):
    await s3_service.upload_file(
        file=file,
    )

    return UploadedResponse(filename=file.filename)
