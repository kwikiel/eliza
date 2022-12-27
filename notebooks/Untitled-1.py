# %%
import os

os.environ["SERPAPI_API_KEY"] = "key_here"

from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.llms import OpenAI

# %%
llm = OpenAI(temperature=0, openai_api_key="key_here")

# %%
tools = load_tools(["serpapi", "llm-math"], llm=llm)

# %%
agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)

# %%
agent.run("Think how to achieve world dominance")


# %%


# %%



