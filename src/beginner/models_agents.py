from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.chat_models import init_chat_model

# from langchain.messages import AIMessage, HumanMessage

load_dotenv()

model = init_chat_model(model="gpt-6-luna", temperature=1.0)

agent = create_agent(model=model)

response = model.invoke("tell me a story")
# response = agent.invoke(
#     {
#         "messages": [
#             HumanMessage(content="what is the capital of indonesia?"),
#             AIMessage(content="Jakarta."),
#             HumanMessage(content="tell me more about it"),
#         ]
#     }
# )

print(response.content)
# print(response["messages"][-1].content)
print("=========================")
print("RESPONSE:", response)
