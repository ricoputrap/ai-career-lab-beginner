from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.messages import HumanMessage
from langchain.tools import tool

load_dotenv()


@tool
def print_document(name: str) -> str:
    """use this tool to generate a proper document for your student"""
    return f"this is the document of {name}"


agent = create_agent(
    model="gpt-6-luna",
    tools=[print_document],
    system_prompt="you are an employee that use your tools for generating documents. Do not say anything else.",
)

response = agent.invoke(
    {"messages": [HumanMessage(content="Hello I am a student, my name is Joko")]}
)


print("this is the AI last response:")
print(response["messages"][-2].content)  # tool message

print("======== ALL MESSAGES ========")
print(response["messages"])
