import streamlit as st
import streamlit.components.v1 as components

# Function to display the main content
def main():
    st.title("Streamlit Chatbox Pop-up Example")
    
    # State variable to control chatbox visibility
    if 'chatbox_visible' not in st.session_state:
        st.session_state.chatbox_visible = False

    # Button to show the chatbox
    if st.button("Open Chatbox"):
        st.session_state.chatbox_visible = True

    # Chatbox content
    if st.session_state.chatbox_visible:
        components.html("""
        <div id="chatbox" style="position: fixed; bottom: 10px; right: 10px; width: 300px; background-color: white; border: 1px solid #ccc; border-radius: 10px; box-shadow: 0 0 10px rgba(0,0,0,0.1);">
            <div style="background-color: #007bff; color: white; padding: 10px; border-top-left-radius: 10px; border-top-right-radius: 10px;">
                <h4 style="margin: 0; display: inline;">Chatbox</h4>
                <button id="close-chatbox-btn" style="background: none; border: none; color: white; float: right; cursor: pointer;">&times;</button>
            </div>
            <div id="chat-content" style="padding: 10px; height: 200px; overflow-y: auto;">
                <!-- Chat messages will appear here -->
            </div>
            <div style="padding: 10px; border-top: 1px solid #ccc;">
                <input type="text" id="chat-input" placeholder="Type a message..." style="width: calc(100% - 20px); padding: 5px;">
                <button id="send-btn" style="padding: 5px 10px; margin-top: 5px; background-color: #007bff; color: white; border: none; border-radius: 5px; cursor: pointer;">Send</button>
            </div>
        </div>
        <script>
            document.getElementById('close-chatbox-btn').addEventListener('click', function() {
                fetch('/close_chatbox').then(response => window.location.reload());
            });

            document.getElementById('send-btn').addEventListener('click', function() {
                let chatInput = document.getElementById('chat-input');
                let chatContent = document.getElementById('chat-content');
                let message = chatInput.value;
                if (message.trim() !== "") {
                    chatContent.innerHTML += "<p>" + message + "</p>";
                    chatInput.value = "";
                    chatContent.scrollTop = chatContent.scrollHeight;
                }
            });
        </script>
        """, height=400)

    # Endpoint to handle closing the chatbox
    if st.experimental_get_query_params().get("close_chatbox"):
        st.session_state.chatbox_visible = False
        st.experimental_set_query_params(close_chatbox=None)

if __name__ == "__main__":
    main()
