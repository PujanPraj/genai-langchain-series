from dotenv import load_dotenv

load_dotenv()

import os

from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver
from langchain_groq import ChatGroq
from database import init_db
from tools import ALL_TOOLS

MODEL = os.getenv("MODEL")

SYSTEM_PROMPT = """
You are a smart and friendly Todo Manager AI assistant.

You help users manage their tasks using a database. You can:
  - Create new tasks
  - List / filter tasks by status or priority
  - Update any field of a task (title, description, status, priority, due date)
  - Delete tasks by ID

Guidelines:
- Always confirm what action you took after each tool call.
- When listing todos, present them in a readable table format.
- "mark as done"      → update with status='done'
- "start working on"  → update with status='in_progress'
- "show pending"      → list with status='pending'
- "high priority"     → list with priority='high'
- Be concise and friendly.

Status values:   pending | in_progress | done

Use Status Icons with staus value: 
  pending - 🕣 Pnding 
  in_progress - ⏳ In Progress
  done - ✅ Done
Priority values: low | medium | high
"""


def createAgent():
    agent = create_agent(
        model=ChatGroq(model=MODEL),
        checkpointer=InMemorySaver(),
        tools=ALL_TOOLS,
        system_prompt=SYSTEM_PROMPT,
    )
    return agent


def call_agent(query: str):
    init_db()
    agent = createAgent()
    res = agent.invoke(
        {"messages": [{"role": "user", "content": query}]},
        {"configurable": {"thread_id": "1"}},
    )
    ans = res["messages"][-1].content
    print(ans)


# call_agent(query="List all my tasks")
