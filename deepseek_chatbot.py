
import streamlit as st
import requests

st.set_page_config(page_title="DeepSeek Chatbot via OpenRouter", page_icon="💬")

st.title("💬 DeepSeek Chatbot")
st.markdown("Powered by [OpenRouter](https://openrouter.ai) + Streamlit")

# Read API key from Streamlit secrets
api_key = st.secrets.get("API_KEY")

if not api_key:
    st.error("API key is missing! Please add it to Streamlit secrets.")
    st.stop()

# Choose model
model = st.selectbox("Choose Model", ["deepseek-chat", "deepseek-coder"])

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": "You are a helpful assistant."}]

# Display messages
for msg in st.session_state.messages[1:]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
if prompt := st.chat_input("Type your message..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Call OpenRouter API
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://your-app-name.streamlit.app",
        "X-Title": "DeepSeek Chatbot"
    }

    payload = {
        "model": model,
        "messages": st.session_state.messages,
        "temperature": 0.7
    }

    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=payload)

    if response.status_code == 200:
        reply = response.json()["choices"][0]["message"]["content"]
        st.session_state.messages.append({"role": "assistant", "content": reply})
        with st.chat_message("assistant"):
            st.markdown(reply)
    else:
        st.error(f"Error {response.status_code}: {response.text}")
