import streamlit as st 
import ollama
"""
This script creates a Streamlit web application that allows users to chat with an AI model named DeepSeek-r1. 
The application maintains a chat history and streams responses from the AI model in real-time.
Modules:
    - streamlit: Used to create the web application interface.
    - ollama: Used to interact with the DeepSeek-r1 AI model.
Functions:
    - st.title: Sets the title of the Streamlit web application.
    - st.session_state: Maintains the chat history across user interactions.
    - st.chat_input: Displays an input box for the user to enter their message.
    - st.chat_message: Displays messages in the chat interface.
    - ollama.chat: Sends the chat history to the DeepSeek-r1 model and streams the response.
Workflow:
    1. Set the page title.
    2. Initialize chat history in the session state if it doesn't exist.
    3. Display the chat input box.
    4. Display the chat history.
    5. Handle new user inputs:
        - Display the user's message.
        - Add the user's message to the chat history.
        - Get a streaming response from the DeepSeek-r1 model.
        - Display the AI model's response.
        - Add the AI model's response to the chat history.
Note:
    - The AI model's response is processed to replace specific tags with more readable text.
"""

# setting page title 
st.title("Chat with DeepSeek-r1 🐳 ")


# Initialize chat history in session state if it doesn't exist
if 'messages' not in st.session_state:
    st.session_state.messages = [
        {'role': 'system', 'content': 'You are AI helpful assistant.'}
    ]

# Display chat input box for user to enter their message
user_input = st.chat_input("Your Message: ")

# Display chat history and handle new user inputs
for message in st.session_state.messages:
    if message['role'] != 'system':
        with st.chat_message(message['role']):
            st.write(message['content'])

# If there is a new user input, process it
if user_input:
    # Display the user's message in the chat interface
    with st.chat_message('user'):
        st.write(user_input)
        
    # Add the user's message to the chat history
    st.session_state.messages.append({'role': 'user', 'content': user_input})
    
    # Get a streaming response from the AI model
    with st.chat_message('assistant'):
        message_placeholder = st.empty()
        full_response = ""
        
        # Send the chat history to the AI model and stream the response
        completion = ollama.chat(
            model='deepseek-r1:1.5b',
            messages=st.session_state.messages,
            stream=True
        )

        # Process the streaming response from the AI model
        for chunk in completion:
            if 'message' in chunk and 'content' in chunk['message']:
                content = chunk['message']['content']
                content = content.replace('<think>', 'thinking.............................................\n').replace("</think>", "\n\n\n\n Answer:")
                full_response += content
                message_placeholder.write(full_response + "|... ")
                
        # Display the full response from the AI model
        message_placeholder.write(full_response)
    
    # Add the AI model's response to the chat history
    st.session_state.messages.append({'role': 'assistant', 'content': full_response})