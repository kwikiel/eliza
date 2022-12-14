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
origins = ["http://localhost:3000", "0.0.0.0:3000"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class AIAnswer(BaseModel):
    response: str


# Redirect to the documentation
@app.get("/")
def root():
    return RedirectResponse(url="/docs")



@app.post("/api/chat", response_model=AIAnswer)
def chat(message: str):
    chatbot_model = ChatBot()
    response = chatbot_model.generate(message)
    print(AIAnswer(response=response))
    return AIAnswer(response=response)



