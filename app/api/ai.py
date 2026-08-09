from fastapi import APIRouter, Depends, status

from app.schemas.api import ContactsInfoResponse, ResumeResponse
from app.services import AIService, S3Service, get_ai_service, get_s3_service

router = APIRouter()


@router.post(
    '/extract/contacts/{filename}',
    status_code=status.HTTP_200_OK,
    response_model=ContactsInfoResponse,
)
async def extract_contacts(
    filename: str,
    s3_service: S3Service = Depends(get_s3_service),
    ai_service: AIService = Depends(get_ai_service),
):
    file_content = await s3_service.get_file_content(
        filename=filename,
    )

    return await ai_service.extract_contacts(file_content)


@router.post(
    '/resume/{filename}', 
    status_code=status.HTTP_200_OK, 
    response_model=ResumeResponse,
)
async def resume_file(
    filename: str,
    s3_service: S3Service = Depends(get_s3_service),
    ai_service: AIService = Depends(get_ai_service),
):
    file_content = await s3_service.get_file_content(
        filename=filename,
    )

    return await ai_service.resume_text(file_content)
