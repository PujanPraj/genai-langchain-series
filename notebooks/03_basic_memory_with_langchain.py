from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

model = ChatGroq(model="openai/gpt-oss-120b")
# prompts = [
#     {"role": "user", "content": "Hello, My name is Pujan Prajapati"},
#     {
#         "role": "ai",
#         "content": "Hello, Pujan! Nice to meet you. How can I assist you today?",
#     },
#     {"role": "user", "content": "What is my name"},
# ]

# response = model.invoke(prompts)
# print(response.content)


# Manage History
history = []
while True:
    query = input("User : ")
    history.append({"role": "user", "content": query})

    if query.lower() in ["quit", "exit", "bye"]:
        print("Bye!")
        break

    response = model.invoke(history)
    history.append({"role": "ai", "content": response.content})
    print("AI : ", response.content)
