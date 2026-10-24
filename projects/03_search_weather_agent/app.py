from agents import get_agent
import streamlit as st

st.subheader("Google Search Agent")
st.caption("Search Anything on google and get real time weather details")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    st.chat_message(msg.get("role")).markdown(msg.get("content"))

if "agent" not in st.session_state:
    st.session_state.agent = get_agent()

query = st.chat_input("Ask anything...")
if query:
    st.session_state.messages.append({"role": "user", "content": query})
    st.chat_message("user").markdown(query)

    res = st.session_state.agent.invoke(
        {
            "messages": [
                {"role": "user", "content": query},
            ]
        },
        {"configurable": {"thread_id": "chat1"}},
    )
    ans = res["messages"][-1].content

    st.session_state.messages.append({"role": "ai", "content": ans})
    st.chat_message("ai").markdown(ans)
