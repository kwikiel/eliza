from backend.config import app
from backend.gptmock import ChatBot
from backend.schema import Prompt, AIAnswer

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