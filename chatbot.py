from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
    temperature=0.7
)
from langchain_core.messages import AIMessage,SystemMessage,HumanMessage


messages=[
SystemMessage(content='You are a funny AI agent')
]

while True:

    print("___________welcome type 0 to exit application")
    prompt=input("You: ")
    messages.append(HumanMessage(content=prompt))
    if prompt=="0":
        break
    response = llm.invoke(messages)
    messages.append(AIMessage(content=response.content))
    print("Bot :",response.content)
   
  