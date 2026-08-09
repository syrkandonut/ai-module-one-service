class S3ClientError(Exception):
    def __init__(self, detail: str | None = None) -> None:
        self.detail = detail


class S3ServiceError(Exception):
    def __init__(self, detail: str | None = None) -> None:
        self.detail = detail


class S3ServiceEmptyFileName(S3ServiceError): ...


class S3ServiceFileExtentionNotAllowed(S3ServiceError): ...


class S3ServiceFileTooLarge(S3ServiceError): ...
