# 🤖 Jarvis – Python Coding Assistant

Jarvis is a **voice + text powered Python coding assistant** built with **Streamlit**, **OpenAI API**, and **SpeechRecognition**.  
It allows users to type or speak their requests, generates Python code using OpenAI, and executes it in real-time within the app.

---

## 🚀 Features
- 🎤 **Voice Input** – Speak your query, Jarvis listens and understands it.  
- 💬 **Text Input** – Type your request if you prefer.  
- 🧠 **Conversation Memory** – Maintains context between prompts for smoother interaction.  
- ⚡ **Code Execution** – Runs generated Python code and displays the output instantly.  
- 🛠 **Error Handling** – Catches runtime errors gracefully and shows clear feedback.  

---

## 🛠 Tech Stack
- [Streamlit](https://streamlit.io/) – Interactive UI  
- [OpenAI API](https://platform.openai.com/) – Code generation  
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) – Voice-to-text conversion  
- [Python](https://www.python.org/) – Core language  

---

## 📂 Project Structure
├── jarvis.py # Main Streamlit app

├── prompt.py # Custom system prompt for Jarvis

├── config.py # Stores API key securely

├── requirements.txt # Dependencies

└── README.md # Documentation
