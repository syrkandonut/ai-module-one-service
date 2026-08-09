from enum import StrEnum

MAX_FILE_SIZE_S3: int = 20 * 1024 * 1024


class AllowExtensionsS3(StrEnum):
    DOCX = 'DOCX'
    DOC = 'DOC'
