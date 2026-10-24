from dotenv import load_dotenv

load_dotenv()

from langchain_groq import ChatGroq
import streamlit as st

model = ChatGroq(model="openai/gpt-oss-20b")

if "messages" not in st.session_state:
    st.session_state.messages = []

# ui
st.subheader("🤖 Qna Bot")

for msg in st.session_state.messages:
    st.chat_message(msg.get("role")).markdown(msg.get("content"))

query = st.chat_input("Ask anything")
if query:
    st.session_state.messages.append({"role": "user", "content": query})
    st.chat_message("user").markdown(query)

    res = model.invoke(st.session_state.messages)
    st.session_state.messages.append({"role": "ai", "content": res.content})
    st.chat_message("assistant").markdown(res.content)

print(st.session_state.messages)

# while True:
#     query = input("User: ")
#     if query in ["exit", "bye"]:
#         break

#     histroy.append({"role": "user", "content": query})

#     res = model.invoke(histroy)
#     print("AI : ", res.content)
#     histroy.append({"role": "ai", "content": res.content})
