# Personal AI Assistant

## Overview
A personal AI assistant built with Google's Agent Development Kit (ADK) and LiteLLM. It uses an OpenRouter-hosted language model and two custom Python tools to help with arithmetic and basic text analysis.

## Features
- **Calculator tool:** Supports addition, subtraction, multiplication, division, and exponentiation through two operands and an operation name.
- **Text analyzer tool:** Counts characters, words, and sentences in supplied text.
- **Tool-aware instructions:** The agent is instructed to use the relevant tool rather than guess tool results and to report tool failures honestly.

## Project Structure
```text
personal_assistant/
├── agent.py
├── __init__.py              # Include if present in your project
├── requirements.txt         # Dependency list
├── .env.example             # Placeholder environment variables only
└── README.md
```

## Requirements
- Python
- Google ADK
- LiteLLM
- python-dotenv

Install dependencies if needed:
```bash
pip install google-adk litellm python-dotenv
```

## Configuration
Create a local `.env` file in the project directory with your own OpenRouter API key:

```env
OPENROUTER_API_KEY=your_openrouter_api_key_here
GOOGLE_GENAI_USE_VERTEXAI=FALSE
```

The project code must load environment variables (for example, with `load_dotenv()`). Keep the real `.env` file private; do not commit or submit it.

## Run
From the parent directory containing the `personal_assistant` folder, activate your Python environment and run:

```bash
adk web
```

Open the ADK Web interface and select `personal_assistant`.

## Example Requests
- `Calculate 25 multiplied by 4.`
- `Count the characters, words, and sentences in: Python is useful. AI is growing!`

## Notes
- The model is configured through LiteLLM with OpenRouter's free-model router: `openrouter/openrouter/free`. Availability and rate limits depend on OpenRouter.
- This version includes two custom tools and does not include Google Search.
- The calculator currently accepts `(a, b, operation)` rather than an arbitrary expression string. Update it if the workshop rubric requires an expression-string interface.
- Include any additional source files your actual project uses. Do not include `.env`, API keys, `.venv/`, `__pycache__/`, or generated files.
