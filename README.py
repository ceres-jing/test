


import streamlit as st

def main():
    st.title("Chatbot Interface")

    # Initialize session state for chatbot visibility
    if 'chatbot_visible' not in st.session_state:
        st.session_state['chatbot_visible'] = False

    # CSS for the button and chat window
    st.markdown("""
        <style>
        .open-chat-button {
            position: fixed;
            bottom: 20px;
            right: 20px;
            z-index: 1000;
            padding: 10px 20px;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        .chat-window {
            position: fixed;
            bottom: 0;
            right: 0;
            width: 300px;
            height: 400px;
            border: 1px solid #ccc;
            background-color: white;
            padding: 10px;
            z-index: 1000;
            display: flex;
            flex-direction: column;
        }
        .chat-window-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .chat-window-content {
            flex: 1;
            overflow-y: auto;
            border: 1px solid #ccc;
            padding: 5px;
            background-color: #f9f9f9;
            margin-top: 10px;
            margin-bottom: 10px;
        }
        </style>
    """, unsafe_allow_html=True)

    # Button to open the chatbot
    if not st.session_state['chatbot_visible']:
        if st.button("Open Chatbot", key="open_chat"):
            st.session_state['chatbot_visible'] = True

    if st.session_state['chatbot_visible']:
        # Chat window
        st.markdown("""
            <div class="chat-window">
                <div class="chat-window-header">
                    <h4>Chatbot</h4>
                    <button id="close-chat-btn" style="background: none; border: none; font-size: 16px; cursor: pointer;">&times;</button>
                </div>
                <div class="chat-window-content" id="chat-window">
                    <!-- Chat content will go here -->
                </div>
                <textarea id="user-input" style="width: 100%;"></textarea>
                <button id="send-btn" style="width: 100%; margin-top: 5px;">Send</button>
            </div>
        """, unsafe_allow_html=True)

        # JavaScript to handle chat window interactions
        st.markdown("""
            <script>
            document.getElementById('close-chat-btn').addEventListener('click', function() {
                fetch('/close_chat').then(response => window.location.reload());
            });
            document.getElementById('send-btn').addEventListener('click', function() {
                const userInput = document.getElementById('user-input').value;
                if (userInput.trim() !== '') {
                    const chatWindow = document.getElementById('chat-window');
                    const userMessage = document.createElement('div');
                    userMessage.textContent = `You: ${userInput}`;
                    chatWindow.appendChild(userMessage);
                    chatWindow.scrollTop = chatWindow.scrollHeight;
                    document.getElementById('user-input').value = '';
                }
            });
            </script>
        """, unsafe_allow_html=True)

        # Add a button to toggle the chatbot visibility
        st.button("Close Chatbot", key="close_chat", on_click=close_chatbot)

# Function to close the chatbot
def close_chatbot():
    st.session_state['chatbot_visible'] = False

html("""
<script>
document.getElementById('close-chat-btn').addEventListener('click', function() {
    fetch('/_stcore/stream?element_type=close_chat').then(response => window.location.reload());
});
</script>
""", height=0)
if __name__ == "__main__":
    main()
