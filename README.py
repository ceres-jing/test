import streamlit as st
import streamlit.components.v1 as components
import rag_backend as sample_backend

# Set page configuration
st.set_page_config(page_title="F1 Regulations Chatbot", layout="wide")

# Custom CSS for styling the chatbot popup
st.markdown("""
    <style>
    .chat-button {
        position: fixed;
        bottom: 20px;
        right: 20px;
        background-color: #4CAF50;
        color: white;
        border: none;
        padding: 15px 20px;
        font-size: 18px;
        cursor: pointer;
        border-radius: 50px;
        z-index: 9999;
    }

    .chat-popup {
        display: none;
        position: fixed;
        bottom: 20px;
        right: 20px;
        border: 3px solid #f1f1f1;
        z-index: 9998;
        width: 400px;
        max-width: 100%;
    }

    .chat-container {
        max-height: 70vh;
        overflow-y: auto;
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 0 10px rgba(0,0,0,0.1);
    }

    .open-chat { display: block; }
    </style>
    """, unsafe_allow_html=True)

# JavaScript to handle the button click and open/close the chatbot
st.markdown("""
    <script>
    function toggleChat() {
        var chatPopup = document.getElementById("chatPopup");
        if (chatPopup.style.display === "none" || chatPopup.style.display === "") {
            chatPopup.style.display = "block";
        } else {
            chatPopup.style.display = "none";
        }
    }
    </script>
    """, unsafe_allow_html=True)

# Button to open the chatbot
st.markdown('<button class="chat-button" onclick="toggleChat()">Chat with us 💬</button>', unsafe_allow_html=True)

# Chat popup container
st.markdown('<div id="chatPopup" class="chat-popup"><div class="chat-container">', unsafe_allow_html=True)

# Title for the chatbot inside the popup
st.markdown('<p style="font-family:sans-serif; color:Green; font-size: 24px;">F1 Regulations Chatbot 🎯</p>', unsafe_allow_html=True)

if 'vector_index' not in st.session_state: 
    with st.spinner("📀 Not quite as fast as Max Verstappen... Please wait while we load your chatbot!"):
        st.session_state.vector_index = sample_backend.f1_regs_index()

input_text = st.text_area("Input Text", label_visibility="collapsed")
go_button = st.button("📌Search", type="primary")

if go_button: 
    with st.spinner("📢 Preparing the tyres!"):  # Spinner message
        response_content = sample_backend.reg_rag_response(index=st.session_state.vector_index, question=input_text)
        st.write(response_content)

# Closing the chat popup container
st.markdown('</div></div>', unsafe_allow_html=True)

