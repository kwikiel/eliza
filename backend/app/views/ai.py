from gptmock import ChatBot
from app.schemas.ai import Prompt, AIAnswer
# Import RedirectResponse from fastapi.responses
from fastapi.responses import RedirectResponse
from fastapi import APIRouter

router = APIRouter(prefix="/api")


@router.get("/")
def root():
    return RedirectResponse(url="/docs")


@router.post("/chat", response_model=AIAnswer)
def chat(message: Prompt):
    chatbot_model = ChatBot()
    response = chatbot_model.generate(message.prompt)
    print(AIAnswer(response=response))
    return AIAnswer(response=response)


@router.post("/thought_process", response_model=AIAnswer)
def thought_process(message: Prompt):
    chatbot_model = ChatBot()
    response = chatbot_model.generate_thought_process(message.prompt)
    print(AIAnswer(response=response))
    return AIAnswer(response=response)