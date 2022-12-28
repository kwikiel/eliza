from fastapi import FastAPI
from gptmock import ChatBot
from pydantic import BaseModel
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
templates = Jinja2Templates(directory="templates")


# class Message(BaseModel):
#     message: str
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class AIAnswer(BaseModel):
    response: str


class Prompt(BaseModel):
    prompt: str

# Redirect to the documentation
@app.get("/")
def root():
    return RedirectResponse(url="/docs")


@app.post("/api/chat", response_model=AIAnswer)
def chat(message: Prompt):
    chatbot_model = ChatBot()
    response = chatbot_model.generate(message.prompt)
    print(AIAnswer(response=response))
    return AIAnswer(response=response)


@app.post("/api/thought_process", response_model=AIAnswer)
def thought_process(message: Prompt):
    chatbot_model = ChatBot()
    response = chatbot_model.generate_thought_process(message.prompt)
    print(AIAnswer(response=response))
    return AIAnswer(response=response)
