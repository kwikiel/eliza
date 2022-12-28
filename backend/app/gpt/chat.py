from langchain import OpenAI, ConversationChain, LLMChain, PromptTemplate
from langchain.chains.conversation.memory import ConversationalBufferWindowMemory
from backend.app.models.prompt_template import TEMPLATE

prompt = PromptTemplate(
    input_variables=["history", "human_input"],
    template=TEMPLATE
)

chatgpt_chain = LLMChain(
    llm=OpenAI(temperature=0.1),
    prompt=prompt,
    verbose=True,
    memory=ConversationalBufferWindowMemory(k=3),
)


def generate(prompt):
    return chatgpt_chain.predict(human_input=prompt)