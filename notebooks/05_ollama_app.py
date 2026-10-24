from langchain_ollama import ChatOllama

model = ChatOllama(model="gemma3:4b")

result = model.invoke("hello")
print(result.content)
