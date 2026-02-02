import ollama
from llm.prompts import CLEAN_TEXT_SYSTEM

def clean_text(model: str, raw_text: str) -> str:
    messages = [
        {"role": "system", "content": CLEAN_TEXT_SYSTEM},
        {"role": "user", "content": raw_text}
    ]
    resp = ollama.chat(model=model, messages=messages)
    return resp["message"]["content"].strip()