
import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="DeepSeek Chatbot", page_icon="🤖")

st.title("🤖 DeepSeek Chatbot")
st.caption("Powered by OpenRouter + Streamlit")

api_key = st.secrets["API_KEY"]

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
    default_headers={
        "HTTP-Referer": "https://atele-x.streamlit.app",
        "X-Title": "DeepSeek Chatbot"
    }
)

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Type your message..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    try:
        response = client.chat.completions.create(
            model="deepseek/deepseek-r1:free",
            messages=st.session_state.messages
        )
        reply = response.choices[0].message.content
        st.session_state.messages.append({"role": "assistant", "content": reply})
        with st.chat_message("assistant"):
            st.markdown(reply)
    except Exception as e:
        st.error(f"Error: {e}")
