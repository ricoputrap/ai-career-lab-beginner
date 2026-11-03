from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.messages import AIMessage, HumanMessage

load_dotenv()

agent = create_agent(model="gpt-6-luna")

response = agent.invoke(
    {
        "messages": [
            HumanMessage(content="what is the capital of indonesia?"),
            AIMessage(content="Jakarta."),
            HumanMessage(content="tell me more about it"),
        ]
    }
)

print(response["messages"][-1].content)
print("=========================")
print("RESPONSE:", response)
