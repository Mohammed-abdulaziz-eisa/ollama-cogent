import ollama 
"""
This script demonstrates how to use the Ollama API to create a streaming chat completion
with the 'llama3.2:latest' model. The script sends a series of messages to the model and 
prints the response in real-time as it is received.

Modules:
    ollama: A module to interact with the Ollama API.

Functions:
    ollama.chat: Sends a chat request to the specified model and returns a streaming response.

Usage:
    The script initializes a chat with the model by sending a system message and a user query.
    It then prints the response from the model in real-time as it streams in.

Example:
    The user asks "why sky is blue?" and the model responds with an explanation, which is 
    printed to the console as it is received.
"""

# create streaming completion 
completion = ollama.chat(
    model= 'llama3.2:latest',
    messages=[
        {'role': 'system', 'content': 'you are a helpful assistant.'},
        {'role': 'user', 'content': 'why sky is blue?'}
    ],
    stream=True # Enable streaming 
)

# print the response as it comes in 
for chunk in completion:
    if 'message' in chunk and 'content' in chunk['message']:
        content= chunk['message']['content']
        print(content, end='', flush=True)