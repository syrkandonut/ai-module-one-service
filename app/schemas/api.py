from pydantic import BaseModel

from .structured_outputs import ContactsInfoSchema, ResumeSchema


class UploadedResponse(BaseModel):
    status: str = 'Success'
    filename: str


class ContactsInfoResponse(ContactsInfoSchema): ...


class ResumeResponse(ResumeSchema): ...
