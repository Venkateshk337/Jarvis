import io
import sys
import streamlit as st
import speech_recognition as sr
from openai import OpenAI
import os

import prompt
from config import OPENAI_API_KEY

# Initialize OpenAI client
client = OpenAI(api_key=OPENAI_API_KEY)

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": prompt.JARVIS_PROMPT}]
if "last_user" not in st.session_state:
    st.session_state.last_user = ""
if "last_assistant" not in st.session_state:
    st.session_state.last_assistant = ""


def listen_to_user():
    """Capture voice input and return recognized text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("🎤 Listening... Speak your request")
        audio = recognizer.listen(source)
    try:
        return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        return "Could not understand audio"
    except sr.RequestError:
        return "Speech recognition service unavailable"


def ask_jarvis(user_prompt):
    """Send prompt to OpenAI with conversation context and get Python code."""
    st.session_state.messages.append({"role": "user", "content": user_prompt})

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=st.session_state.messages
    )

    assistant_message = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": assistant_message})

    st.session_state.last_user = user_prompt
    st.session_state.last_assistant = assistant_message

    # Extract code block
    code = assistant_message.strip("```python").strip("```").strip()
    return code


def run_generated_code(code: str):
    """Run generated Python code and capture its output."""
    old_stdout = sys.stdout
    sys.stdout = io.StringIO()
    local_vars = {}
    try:
        exec(code, {}, local_vars)
        output = sys.stdout.getvalue()
    except Exception as e:
        output = f"⚠️ Error while running code: {e}"
    finally:
        sys.stdout = old_stdout
    return output


# ----------------- Streamlit Frontend -----------------
st.title("🤖 Jarvis – Python Coding Assistant")

# Display last conversation
if st.session_state.last_user:
    st.markdown(f"**Previous Prompt:** {st.session_state.last_user}")
if st.session_state.last_assistant:
    st.markdown(f"**Previous Response:**\n```\n{st.session_state.last_assistant}\n```")

# Text input
user_text = st.text_input("💬 Type your request here:")

# Voice input
voice_input = None
if st.button("🔊 Speak"):
    voice_input = listen_to_user()
    st.write(f"👤 You said: {voice_input}")

# Choose whichever input is not empty
final_input = voice_input if voice_input else user_text

if final_input:
    with st.spinner("Jarvis is thinking..."):
        code = ask_jarvis(final_input)
        result = run_generated_code(code)

    # st.subheader("🤖 Generated Code")
    # st.code(code, language="python")

    st.subheader("📌 Output")
    st.text(result if result else "No output (maybe the code only defined a function)")
