from app.exceptions.ai import LLMNoResponse
from app.infrastructure.clients import LlamaClient
from app.schemas.structured_outputs import ContactsInfoSchema, ResumeSchema


class AIService:
    def __init__(self, ai_client: LlamaClient):
        self.ai_client = ai_client

    async def extract_contacts(self, text: str) -> ContactsInfoSchema:
        result = await self.ai_client.chat(
            system_promt=(
                'Your task is to extract information about hotel contacts. '
                'You MUST strictly follow the provided JSON schema.'
                'You MUST strictly use info from the text else N/A'
            ),
            user_promt=f'Extract info from this text: {text}',
            output_schema=ContactsInfoSchema,
            temperature=0.0,
        )

        if not result:
            raise LLMNoResponse

        return result

    async def resume_text(self, text: str) -> ResumeSchema:
        result = await self.ai_client.chat(
            system_promt=(
                'Your task is to summarize text.'
                'Fill out all fields, do not use empty strings'
                'You MUST strictly follow the provided JSON schema.'
            ),
            user_promt=f'Summarize this text: {text}',
            output_schema=ResumeSchema,
            temperature=0.7,
        )

        if not result:
            raise LLMNoResponse

        return result
