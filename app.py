import streamlit as st
from chatbot import get_response


# Page configuration
st.set_page_config(
    page_title="Rule-Based AI Chatbot",
    page_icon="🤖",
    layout="centered"
)


# CSS
st.markdown("""
<style>

    /* Make chat input part of normal page flow */
    div[data-testid="stChatInput"] {
        position: relative !important;
        bottom: auto !important;
        left: auto !important;
        right: auto !important;
        width: 100% !important;
        margin-top: 20px;
        margin-bottom: 20px;
    }

    /* Remove fixed positioning from chat input container */
    div[data-testid="stBottom"] {
        position: relative !important;
        bottom: auto !important;
    }

</style>
""", unsafe_allow_html=True)


# Title
st.title("🤖 Rule-Based AI Chatbot")

st.write(
    "Ask me questions about AI, Machine Learning, Python, "
    "Data Science, or this project."
)


# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []


# Display chat history
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.write(message["content"])


# Chat input
user_input = st.chat_input("Ask a question...")


# Process user input
if user_input:

    # User message
    with st.chat_message("user"):
        st.write(user_input)

    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })


    # Bot response
    response = get_response(user_input)

    with st.chat_message("assistant"):
        st.write(response)

    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })


# Clear chat button
if st.button("🗑️ Clear Chat"):

    st.session_state.messages = []

    st.rerun()