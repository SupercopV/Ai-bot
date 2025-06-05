import streamlit as st
import requests

st.set_page_config(page_title="DeepSeek Chatbot", page_icon="💬")

st.title("💬 DeepSeek Chatbot")
st.markdown("Powered by [OpenRouter](https://openrouter.ai) + Streamlit")

# Load secret
api_key = st.secrets.get("API_KEY")

# Choose model
model = st.selectbox("Choose Model", ["deepseek-chat"])

# Initialize chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
if prompt := st.chat_input("Type your message..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Prepare request
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://atele-x.streamlit.app",
        "X-Title": "DeepSeek Chatbot"
    }
    data = {
        "model": model,
        "messages": st.session_state.messages
    }

    # Make request
    try:
        response = requests.post(url, headers=headers, json=data)
        result = response.json()
        reply = result["choices"][0]["message"]["content"]
    except Exception as e:
        reply = f"Error {response.status_code}: {result}"

    # Display reply
    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.markdown(reply)
