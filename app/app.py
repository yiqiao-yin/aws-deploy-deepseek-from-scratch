import streamlit as st
from helper import query_deepseek  # Import the backend function

# Set Streamlit page config
st.set_page_config(page_title="DeepSeek-R1 Chatbot", layout="wide")

# Streamlit app UI
st.title("🤖 DeepSeek-R1 Chatbot")

# Sidebar for user settings
st.sidebar.header("⚙️ Model Settings")

# Sliders for model parameters with emojis
max_gen_len = st.sidebar.slider("📝 Max Generation Length", min_value=100, max_value=2048, value=1024, step=50)
temperature = st.sidebar.slider("🔥 Temperature (Creativity)", min_value=0.0, max_value=1.0, value=0.1, step=0.05)
top_p = st.sidebar.slider("🎯 Top-P Sampling (Diversity)", min_value=0.0, max_value=1.0, value=0.9, step=0.05)

# Button to clear chat history
if st.sidebar.button("🗑️ Clear Chat History"):
    st.session_state.messages = []  # Reset conversation history
    st.rerun()  # Refresh the app

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if prompt := st.chat_input("💬 Ask me anything!"):
    # Display user message in chat history
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Show a spinner while waiting for the response
    with st.spinner("🤖 Generating response... Please wait."):
        response = query_deepseek(prompt, max_gen_len, temperature, top_p)

    # Display assistant response
    with st.chat_message("assistant"):
        st.markdown(response)

    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
