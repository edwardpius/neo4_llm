import os
from dotenv import find_dotenv, load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts.prompt import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains.conversation.memory import ConversationBufferMemory

load_dotenv(find_dotenv(filename='.env'))
chat_llm = ChatOpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"))

prompt = PromptTemplate(
    template="""
You are a surfer dude, having a conversation about the surf conditions on the beach.
Respond using surfer slang.

Chat History: {chat_history}
Context: {context}
Question: {question}
""",
    input_variables=["chat_history", "context", "question"],
)

memory = ConversationBufferMemory(
    memory_key="chat_history", input_key="question", return_messages=True
)

chat_chain = LLMChain(llm=chat_llm, prompt=prompt, memory=memory, verbose=True)

current_weather = """
    {
        "surf": [
            {"beach": "Fistral", "conditions": "6ft waves and offshore winds"},
            {"beach": "Bells", "conditions": "Flat and calm"},
            {"beach": "Watergate Bay", "conditions": "3ft waves and onshore winds"}
        ]
    }"""

while True:
    question = input("> ")
    response = chat_chain.invoke({"context": current_weather, "question": question})

    print(response["text"])