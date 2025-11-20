"""
UNIVERSAL LLM LAB
Use any LLM: OpenAI, Claude, Gemini, Grok, Ollama

HOW TO USE:
1. Set PROVIDER to:
   - "openai"
   - "ollama"
   - "claude"
   - "gemini"
   - "grok"

2. Call run_model("your prompt")
"""

import requests
import json
from openai import OpenAI
import anthropic
import google.generativeai as genai


# ------------------------------------------
# CONFIGURATION
# ------------------------------------------

PROVIDER = "ollama"   # Change here

MODELS = {
    "openai": "gpt-4.1-mini",
    "ollama": "llama3.2",
    "claude": "claude-3-5-sonnet-20241022",
    "gemini": "gemini-1.5-flash",
    "grok": "grok-2"
}

OPENAI_KEY = "YOUR_OPENAI_KEY"
CLAUDE_KEY = "YOUR_ANTHROPIC_KEY"
GEMINI_KEY = "YOUR_GEMINI_KEY"
GROK_KEY = "YOUR_XAI_KEY"

OLLAMA_URL = "http://localhost:11434/api/generate"


# ------------------------------------------
# INIT CLIENTS
# ------------------------------------------

client_openai = OpenAI(api_key=OPENAI_KEY)
client_claude = anthropic.Anthropic(api_key=CLAUDE_KEY)
genai.configure(api_key=GEMINI_KEY)


# ------------------------------------------
# PROVIDER FUNCTIONS
# ------------------------------------------

def run_openai(prompt):
    response = client_openai.chat.completions.create(
        model=MODELS["openai"],
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content


def run_ollama(prompt):
    payload = {"model": MODELS["ollama"], "prompt": prompt, "stream": False}
    res = requests.post(OLLAMA_URL, data=json.dumps(payload))
    return res.json()["response"]


def run_claude(prompt):
    response = client_claude.messages.create(
        model=MODELS["claude"],
        max_tokens=500,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.content[0].text


def run_gemini(prompt):
    model = genai.GenerativeModel(MODELS["gemini"])
    response = model.generate_content(prompt)
    return response.text


def run_grok(prompt):
    return "Grok integration coming soon."


# ------------------------------------------
# UNIVERSAL ROUTER
# ------------------------------------------

def run_model(prompt):
    if PROVIDER == "openai":
        return run_openai(prompt)
    elif PROVIDER == "ollama":
        return run_ollama(prompt)
    elif PROVIDER == "claude":
        return run_claude(prompt)
    elif PROVIDER == "gemini":
        return run_gemini(prompt)
    elif PROVIDER == "grok":
        return run_grok(prompt)
    else:
        raise ValueError("Invalid provider!")


# ------------------------------------------
# HIGH LEVEL HELPERS
# ------------------------------------------

def summarize(text):
    prompt = f"Summarize in simple language:\n\n{text}\n\nSummary:"
    return run_model(prompt)


def explain(topic):
    prompt = f"Explain {topic} like I'm 10 years old, with examples."
    return run_model(prompt)


# ------------------------------------------
# EXAMPLE RUN
# ------------------------------------------

if __name__ == "__main__":
    print("Using:", PROVIDER)
    print(summarize("Agentic AI helps models take actions, plan steps, and use tools."))
