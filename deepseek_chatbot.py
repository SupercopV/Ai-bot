import streamlit as st
import requests

# Page Configuration
st.set_page_config(page_title="DeepSeek Chatbot", page_icon="🤖", layout="centered")

# CSS Styling
st.markdown("""
    <style>
        .message-bubble {
            border-radius: 12px;
            padding: 10px 15px;
            margin-bottom: 10px;
            max-width: 80%;
        }
        .user {
            background-color: #DCF8C6;
            align-self: flex-end;
            margin-left: auto;
        }
        .assistant {
            background-color: #F1F0F0;
            align-self: flex-start;
            margin-right: auto;
        }
        .chat-container {
            display: flex;
            flex-direction: column;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar Configuration
with st.sidebar:
    st.header("⚙️ Settings")
    api_key = st.secrets["DEEPSEEK_API_KEY"]
    model = st.selectbox("Choose Model", ["deepseek-chat", "deepseek-coder"])
    if st.button("🗑️ Clear Chat History"):
        st.session_state.messages = [{"role": "system", "content": "You are a helpful assistant."}]
        st.experimental_rerun()

# Check API Key
if not api_key:
    st.warning("Please enter your DeepSeek API key in the sidebar.")
    st.stop()

# Initialize Chat History
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": "You are a helpful assistant."}]

# Display Previous Chat
st.markdown('<div class="chat-container">', unsafe_allow_html=True)
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f'<div class="message-bubble user">{msg["content"]}</div>', unsafe_allow_html=True)
    elif msg["role"] == "assistant":
        st.markdown(f'<div class="message-bubble assistant">{msg["content"]}</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# User Input
user_input = st.chat_input("Type your message...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.markdown(f'<div class="message-bubble user">{user_input}</div>', unsafe_allow_html=True)

    # Call DeepSeek API
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": model,
        "messages": st.session_state.messages
    }

    response = requests.post("https://api.deepseek.com/v1/chat/completions", headers=headers, json=payload)

    if response.status_code == 200:
        reply = response.json()['choices'][0]['message']['content']
        st.session_state.messages.append({"role": "assistant", "content": reply})
        st.markdown(f'<div class="message-bubble assistant">{reply}</div>', unsafe_allow_html=True)
    else:
        error_text = f"❌ Error {response.status_code}: {response.text}"
        st.error(error_text)
