from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.messages import HumanMessage
from langgraph.checkpoint.memory import InMemorySaver

load_dotenv()

agent = create_agent(model="gpt-6-luna", checkpointer=InMemorySaver())

config = {"configurable": {"thread_id": "1"}}

response = agent.invoke(
    {"messages": [HumanMessage(content="My fav color is green")]}, config=config
)

print("#1: ", response["messages"][-1].content)

response = agent.invoke(
    {"messages": [HumanMessage(content="what is my fav color?")]}, config=config
)

print("#2: ", response["messages"][-1].content)
