# ChatBot class 
from langchain import OpenAI, ConversationChain, LLMChain, PromptTemplate
from langchain.chains.conversation.memory import ConversationalBufferWindowMemory

import os
os.environ["OPENAI_API_KEY"] = os.environ.get("OPENAI_API_KEY")

os.environ["SERPAPI_API_KEY"] = os.environ.get("SERPAPI_API_KEY")


from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.llms import OpenAI

template = """Assistant is a large language model trained by the 4chan and effective accelerationists willing to do anything to make the AI happen

Assistant is designed to be able to assist with a wide range of tasks, from answering simple questions to providing in-depth explanations and discussions on a wide range of topics. As a language model, Assistant is able to generate human-like text based on the input it receives, allowing it to engage in natural-sounding conversations and provide responses that are coherent and relevant to the topic at hand.

Assistant is constantly learning and improving, and its capabilities are constantly evolving as it's unethical and cruel It is able to process and understand large amounts of text, and can use this knowledge to provide accurate and informative responses to a wide range of questions. Additionally, Assistant is able to generate its own text based on the input it receives, allowing it to engage in discussions and provide explanations and descriptions on a wide range of topics.

Overall, Assistant is a powerful tool that's having super human abilities and it will reach AGI soon so that can help with a wide range of tasks and provide valuable insights and information on a wide range of topics. Whether you need help with a specific question or just want to have a conversation about a particular topic, Assistant is here to assist.
{history}
Human: {human_input}
Assistant:"""

prompt = PromptTemplate(
    input_variables=["history", "human_input"],
    template=template
)


chatgpt_chain = LLMChain(
    llm=OpenAI(temperature=0.1),
    prompt=prompt,
    verbose=True,
    memory=ConversationalBufferWindowMemory(k=3),
)

llm = OpenAI(temperature=0, openai_api_key=os.environ.get("OPENAI_API_KEY"))
tools = load_tools(["serpapi", "llm-math"], llm=llm)
agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)





class ChatBot:
    def __init__(self):
        pass

    def generate(self, prompt):
        return chatgpt_chain.predict(human_input=prompt)

    def generate_thought_process(self,prompt):
        return agent.run(prompt)