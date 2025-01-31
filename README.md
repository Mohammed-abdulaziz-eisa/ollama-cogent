# Ollama-Cogent

A collection of practical implementations demonstrating different integration patterns with Ollama's API, focusing on Large Language Model (LLM) deployments and streaming interactions.

## Overview

This repository provides production-ready examples of integrating Ollama with different model architectures and user interfaces. The implementations showcase various deployment patterns, from simple streaming completions to interactive chat applications.

## Repository Structure

```
ollama-cogent/
├── app_deepseekr1:1.5b.py      # Basic completion with DeepSeek-R1 1.5B model
├── app_llama3.2:latest_gradio.py  # Interactive Gradio UI for Llama 3.2
└── app_llama3.2:latest_streaming.py  # Streaming implementation with Llama 3.2
└── app_deepseekr1:1.5b_streamlit.py # Interactive Streamlit UI with DeepSeek-R1 1.5B
└── app_llama3.2:latest_chainlit.py # Interactive Chainlit UI with Llama 3.2
```

## Features

- Streaming text completion implementations
- Interactive chat interface using Gradio
- Support for multiple LLM architectures (DeepSeek-R1, Llama 3.2)
- Real-time response handling
- Conversation history management
- Thought process visualization

## Implementation Details

### DeepSeek-R1 1.5B Implementation
`app_deepseekr1:1.5b.py` a basic completion setup with the DeepSeek-R1 1.5B model, featuring:
- Direct message content access
- Thought process visualization
- Structured response formatting

### Llama 3.2 Streaming Implementation
`app_llama3.2:latest_streaming.py` showcases a streamlined implementation focusing on:
- Efficient streaming response handling
- Real-time content display
- System message configuration
- Proper stream handling and buffer management


### Llama 3.2 Gradio Interface
`app_llama3.2:latest_gradio.py` provides a web-based chat interface with:
- Real-time streaming responses
- Conversation history management
- Clear/reset functionality
- Thought process formatting
- Queue management for multiple users


### DeepSeek-R1 1.5B Streamlit Interface
`app_deepseekr1:1.5b_streamlit.py` provides a web-based chat interface with:
- Setting up the Streamlit page title
- Initializing chat history in session state
- Displaying chat input and chat history
- Handling new user inputs and displaying user messages
- Streaming responses from the DeepSeek-R1 1.5B model using the Ollama API
- Processing and displaying the streaming response in real-time
- Adding assistant responses to the chat history

### Llama 3.2 Chainlit Interface
`app_llama3.2:latest_chainlit.py` provides a web-based chat interface with:

#### Features
- Setting up Chainlit for a chat interface
- Initializing chat history
- Handling user messages
- Streaming responses from the Llama 3.2 model
- Real-time response display
- Updating messages dynamically

## Prerequisites

- Python 3.9+
- Ollama API - local server
- Required Python packages:
  ```
  ollama
  gradio
  streamlit
  chainlit
  ```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Mohammed-abdulaziz-eisa/ollama-cogent.git
cd ollama-cogent
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Ensure Ollama is running locally or configure the API endpoint as needed.

## Usage

### Basic Completion with DeepSeek-R1
```bash
python3 app_deepseekr1:1.5b.py
```

### Interactive Chat Interface
```bash
python3 app_llama3.2:latest_gradio.py
```
Access the interface at `http://localhost:7860`

### Streaming Implementation
```bash
python3 app_llama3.2:latest_streaming.py
```

### Interactive Streamlit Interface
```bash
streamlit run app_deepseekr1:1.5b_streamlit.py
```

### Interactive Chainlit Interface
```bash
chainlit run app_llama3.2:latest_chainlit.py -w 
```
The `-w` flag enables auto-reloading in Chainlit, eliminating the need to restart the server after each change to your application. Your chatbot UI will be accessible at `http://localhost:8000`.

## Best Practices Implemented

- Structured error handling
- Clean code organization
- Comprehensive documentation
- Modular design patterns
- Efficient stream handling
- Proper resource management
- Clear separation of concerns

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Ollama team for providing the API
- Gradio team for the UI framework
- DeepSeek and Llama model creators
- Streamlit team for the web framework