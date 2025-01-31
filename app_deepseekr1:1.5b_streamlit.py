import streamlit as st 
import ollama

# setting page title 
st.title("Chat with DeepSeek-r1 🐳 ")


# Initialize chat history in session state if it doesn't exist
if 'messages' not in st.session_state:
    st.session_state.messages = [
        {'role': 'system' , 'content': 'You are AI helpful assistant.'}
    ]
    
# Display chat input 
user_input = st.chat_input("Your Message: ")

# Display chat history and handle new inputs 
for message in st.session_state.messages:
    if message['role'] != 'system':
        with st.chat_message(message['role']):
            st.write(message['content'])

if user_input:
    # Display user message
    with st.chat_message('user'):
        st.write(user_input)
        
    # Add user message to history 
    st.session_state.messages.append({'role': 'user', 'content' : user_input})
    
    # Get streaming response 
    with st.chat_message('assistant'):
        message_placeholder = st.empty()
        full_response = ""
        
        completion = ollama.chat(
           model='deepseek-r1:1.5b',
           messages= st.session_state.messages,
           stream=True
        )

        # process the streaming response 
        for chunk in completion:
            if 'message' in chunk and 'content' in chunk['message']:
                content= chunk['message']['content']
                content = content.replace('<think>', 'thinking.............................................\n').replace("</think>", "\n\n\n\n Answer:")
                full_response += content
                message_placeholder.write(full_response + "|... ")
                
        message_placeholder.write(full_response)
    # Add assistant response to history 
    st.session_state.messages.append({'role':'assistant', 'content': full_response})