from pydantic import BaseModel

class AIAnswer(BaseModel):
    response: str


class Prompt(BaseModel):
    prompt: str