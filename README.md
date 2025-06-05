# 🧠 DeepSeek Chatbot via OpenRouter

A lightweight Streamlit chatbot app powered by [OpenRouter](https://openrouter.ai), supporting models like `deepseek-chat` and `deepseek-coder`.

---

## 🚀 Features

- Clean UI with chat bubbles
- Supports multiple DeepSeek models
- Simple API key input via sidebar
- Easily deployable on Streamlit Cloud

---

## 🛠️ Setup

1. **Clone the repo:**

```bash
git clone https://github.com/your-username/deepseek-chatbot-openrouter.git
cd deepseek-chatbot-openrouter
```

2. **Install dependencies:**

```bash
pip install -r requirements.txt
```

3. **Run the app:**

```bash
streamlit run deepseek_chatbot.py
```

4. **Enter your OpenRouter API key (`sk-or-...`) in the sidebar.**

---

## 🌐 Deploy on Streamlit Cloud

1. Push this project to your GitHub.
2. Go to [Streamlit Cloud](https://streamlit.io/cloud).
3. Create a new app linked to your repo.
4. Add a `secrets.toml` file for your API key:

```toml
# .streamlit/secrets.toml
DEEPSEEK_API_KEY = "sk-or-..."
```

5. Modify the code to read the key from `st.secrets["DEEPSEEK_API_KEY"]` if needed.

---

## 📦 Models Supported

- `deepseek-chat`
- `deepseek-coder`

More models: [https://openrouter.ai/docs#models](https://openrouter.ai/docs#models)

---

## 📧 Contact

Made with ❤️ using [Streamlit](https://streamlit.io) and [OpenRouter](https://openrouter.ai)
