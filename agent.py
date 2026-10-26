
import os

from google.adk.agents import Agent
import re
from google.adk.models.lite_llm import LiteLlm
from dotenv import load_dotenv

load_dotenv()

def calculator(a: float, b: float, operation: str) -> float:
    """Calculate using add, subtract, multiply, divide, or power."""

    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b
    elif operation == "power":
        return a ** b
    else:
        raise ValueError(
            "Unsupported operation. Use add, subtract, "
            "multiply, divide, or power."
        )

def text_analyzer(text: str) -> dict:
    """Count characters, words, and sentences in the given text."""

    characters = len(text)
    words = len(text.split())

    # Split on sentence-ending punctuation.
    sentences = [
        part for part in re.split(r"[.!?]+", text)
        if part.strip()
    ]

    return {
        "characters": characters,
        "words": words,
        "sentences": len(sentences),
    }


root_agent = Agent(
    name="personal_assistant",
    model=LiteLlm(
        model="openrouter/openrouter/free",
        api_key=os.environ["OPENROUTER_API_KEY"],
    ),
    description="A personal assistant for calculations and text analysis.",
    instruction=(
        "You are a helpful personal AI assistant. "
        "Use the calculator tool for arithmetic calculations. "
        "Use the text_analyzer tool to count characters, words, "
        "and sentences. Use tools instead of guessing results. "
        "If a tool fails, explain the problem honestly."
    ),
    tools=[calculator, text_analyzer],
)