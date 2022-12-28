import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


os.environ["OPENAI_API_KEY"] = os.environ.get("OPENAI_API_KEY")
os.environ["SERPAPI_API_KEY"] = os.environ.get("SERPAPI_API_KEY")


app = FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)