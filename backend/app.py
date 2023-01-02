from gptmock import ChatBot
from pydantic import BaseModel
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")

