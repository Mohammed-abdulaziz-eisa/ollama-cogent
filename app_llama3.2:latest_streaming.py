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
        
# output 
'''
The reason why the sky appears blue is due to a phenomenon called Rayleigh scattering, named after the British physicist Lord Rayleigh, who first described it in the late 19th century.

Here's what happens:

1. **Sunlight enters Earth's atmosphere**: When sunlight enters our atmosphere, it encounters tiny molecules of gases such as nitrogen (N2) and oxygen (O2).
2. **Scattering occurs**: These gas molecules scatter the light in all directions, but they scatter shorter (blue) wavelengths more than longer (red) wavelengths.
3. **Blue light is scattered in all directions**: As a result, the blue light is dispersed throughout the atmosphere, reaching our eyes from all parts of the sky.
4. **Our eyes perceive the color blue**: When we look up at the sky, our eyes receive a predominantly blue light, which our brains interpret as the color blue.

Why doesn't the sky appear violet? Violet light has a shorter wavelength than blue light and is scattered even more by the gas molecules in the atmosphere. However, our eyes are more sensitive to blue light, so we perceive it as the dominant color of the sky.

Other factors can influence the apparent color of the sky, such as:

* **Dust and water vapor**: Tiny particles in the atmosphere can scatter shorter wavelengths, making the sky appear more hazy or reddish.
* **Sun's position**: When the sun is lower in the sky, the light has to travel through more of the atmosphere, scattering off more molecules and changing its color.
* **Atmospheric conditions**: Polluted air, smoke, and other environmental factors can alter the apparent color of the sky.

Now you know the reason behind that stunning blue hue we enjoy every day!% 

'''