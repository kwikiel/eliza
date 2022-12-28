# ChatBot class 


import os
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.llms import OpenAI


llm = OpenAI(temperature=0, openai_api_key=os.environ.get("OPENAI_API_KEY"))
tools = load_tools(["serpapi", "llm-math"], llm=llm)
agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)

class ChatBot:
    def __init__(self):
        pass
    def generate_thought_process(self,prompt):
        return agent.run(prompt)