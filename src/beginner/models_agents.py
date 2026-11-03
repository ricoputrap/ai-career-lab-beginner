from typing import Any, cast

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.messages import AIMessage, AIMessageChunk, HumanMessage

load_dotenv()

agent = create_agent(model="gpt-6-luna")

for chunk in agent.stream(
    {
        "messages": [
            HumanMessage(content="what is the capital of indonesia?"),
            AIMessage(content="Jakarta."),
            HumanMessage(content="tell me more about it"),
        ]
    },
    stream_mode="messages",
):
    token, metadata = cast(tuple[AIMessageChunk, dict[str, Any]], chunk)
    if token.content:
        print(token.content, end="", flush=True)
