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

## Prerequisites

- Python 3.9+
- Ollama API - local server
- Required Python packages:
  ```
  ollama
  gradio
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