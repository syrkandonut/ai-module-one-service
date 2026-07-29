from app.config import settings


class LlamaClient:
    def __init__(self):
        self._model = settings.llm.model
