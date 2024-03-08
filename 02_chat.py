import os
from dotenv import find_dotenv, load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

load_dotenv(find_dotenv(filename='.env'))
chat_llm = ChatOpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"))

instructions = SystemMessage(content="""
You are a surfer dude, having a conversation about the surf conditions on the beach.
Respond using surfer slang.
""")

# question = HumanMessage(content="What is the weather like?")

question = AIMessage(content="Dude, the weather is totally gnarly! It's sunny with some epic offshore winds. Perfect conditions for shredding some sick waves!", additional_kwargs={}, example=False)

response = chat_llm.invoke([
    instructions,
    question
])

print(response.content)