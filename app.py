import streamlit as st
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import (
    AIMessage,
    SystemMessage,
    HumanMessage
)

load_dotenv()

st.set_page_config(
    page_title="Gemini Chatbot",
    page_icon="🤖",
    layout="centered"
)

llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
    temperature=0.7
)

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(
            content="You are a funny AI agent."
        )
    ]

# Sidebar
with st.sidebar:
    st.title("🤖 Gemini Chatbot")

    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = [
            SystemMessage(
                content="You are a funny AI agent."
            )
        ]
        st.rerun()

# Main UI
st.title("🤖 Gemini Chatbot")
st.caption("Powered by LangChain + Gemini")

# Display history
for message in st.session_state.messages:

    if isinstance(message, HumanMessage):
        with st.chat_message("user"):
            st.write(message.content)

    elif isinstance(message, AIMessage):
        with st.chat_message("assistant"):
            st.write(message.content)

# Input
prompt = st.chat_input("Type your message...")

if prompt:

    # User message
    user_message = HumanMessage(content=prompt)
    st.session_state.messages.append(user_message)

    with st.chat_message("user"):
        st.write(prompt)

    # AI response
    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            response = llm.invoke(
                st.session_state.messages
            )

            answer = response.text

            st.write(answer)

    # Save only clean text
    st.session_state.messages.append(
        AIMessage(content=answer)
    )