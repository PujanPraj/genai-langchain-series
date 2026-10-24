from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

model = ChatGroq(model="openai/gpt-oss-120b", streaming=True)
question = "Can you explain me GenAI?"

response = model.stream(question)
for chunk in response:
    print(chunk.content, end="")
