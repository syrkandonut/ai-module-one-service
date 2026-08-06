from typing import Type

from ollama import AsyncClient

from app.config import settings
from app.schemas.structured_outputs import StructuredOutputSchema


class LlamaClient:
    def __init__(self):
        self._model = settings.llm.model
        self._host = settings.llm.host
        self._client = None

    @property
    def client(self):
        if self._client is None:
            self._client = AsyncClient(host=self._host)
        return self._client

    async def chat(
        self,
        output_schema: Type[StructuredOutputSchema],
        system_promt: str | None = None,
        user_promt: str | None = None,
        temperature: float = 0.5,
    ) -> StructuredOutputSchema | None:
        response = await self.client.chat(
            model=self._model,
            messages=[
                {
                    'role': 'system',
                    'content': system_promt,
                },
                {
                    'role': 'user',
                    'content': user_promt,
                },
            ],
            format=output_schema.model_json_schema(),
            options={
                'temperature': temperature,
            },
        )

        raw_content = response.message.content

        return output_schema.model_validate_json(raw_content) if raw_content else None
