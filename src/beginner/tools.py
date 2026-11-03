from typing import Any

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.messages import HumanMessage
from langchain.tools import tool
from tavily import TavilyClient

load_dotenv()

tavily_client = TavilyClient()


@tool
def web_search(query: str) -> dict[str, Any]:
    """tool for searching the web for information"""
    print(f"we are doing some research on {query}")
    return tavily_client.search(query)


agent = create_agent(model="gpt-6-luna", tools=[web_search])

response = agent.invoke(
    {"messages": [HumanMessage(content="give me the latest golang version")]}
)


print("this is the AI last response:")
print(response["messages"][-1].content[-1]["text"])

print("======== ALL MESSAGES ========")
print(response["messages"])
