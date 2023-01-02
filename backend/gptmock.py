# ChatBot class 
import os
import json
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.llms import OpenAI


llm = OpenAI(temperature=0, openai_api_key=os.environ.get("OPENAI_API_KEY"))
tools = load_tools(["serpapi", "llm-math"], llm=llm)
agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True, return_intermediate_steps=True)

class ChatBot:
    def __init__(self):
        pass
    def generate2(self,prompt):
        return agent.run(prompt)

    def generate(self,prompt):
        response = agent({"input": prompt})
        return json.dumps(response["intermediate_steps"])
