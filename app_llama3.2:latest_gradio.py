import ollama
import gradio as gr

def chat_with_ollama(message, history):
    """
    Function to interact with the Ollama model.
    
    Args:
        message (str): The user's message.
        history (list): The conversation history.
        
    Yields:
        str: The response from the model.
    """
    response = ""
    messages = [{'role': 'system', 'content': 'You are a helpful assistant.'}]
    
    for user_msg, assistant_msg in history:
        messages.append({'role': 'user', 'content': user_msg})
        if assistant_msg:
            messages.append({'role': 'assistant', 'content': assistant_msg})
    
    messages.append({'role': 'user', 'content': message})
    
    completion = ollama.chat(
        model='llama3.2:latest',
        messages=messages,
        stream=True
    )
    
    for chunk in completion:
        if 'message' in chunk and 'content' in chunk['message']:
            content = chunk['message']['content']
            content = content.replace('<think>', 'thinking....').replace("</think>", "\n\n Answer:")
            response += content
            yield response

def user(user_message, history):
    """
    Function to handle user input.
    
    Args:
        user_message (str): The user's message.
        history (list): The conversation history.
        
    Returns:
        tuple: Empty string and updated history.
    """
    return "", history + [[user_message, None]]

def bot(history):
    """
    Function to handle bot responses.
    
    Args:
        history (list): The conversation history.
        
    Yields:
        list: Updated conversation history.
    """
    history[-1][-1] = ""
    for chunk in chat_with_ollama(history[-1][0], history[:-1]):
        history[-1][-1] = chunk
        yield history

with gr.Blocks() as demo:
    chatbot = gr.Chatbot()
    msg = gr.Textbox(placeholder='Enter your message here ...')
    clear = gr.Button("Clear")
    
    msg.submit(user, [msg, chatbot], [msg, chatbot], queue=False).then(
        bot, chatbot, chatbot
    )
    clear.click(lambda: None, None, chatbot, queue=False)

if __name__ == '__main__':
    demo.launch()