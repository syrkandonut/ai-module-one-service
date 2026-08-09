class LLMError(Exception):
    def __init__(self, detail: str | None = None) -> None:
        self.detail = detail


class LLMNoResponse(LLMError):
    detail = "LLM didn't return response"
