from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.messages import AIMessage, HumanMessage

load_dotenv()

agent = create_agent(model="gpt-6-luna")

for token, metadata in agent.stream(
    {
        "messages": [
            HumanMessage(content="what is the capital of indonesia?"),
            AIMessage(content="Jakarta."),
            HumanMessage(content="tell me more about it"),
        ]
    },
    stream_mode="messages",
):
    if token.content:
        print(token.content, end="", flush=True)
