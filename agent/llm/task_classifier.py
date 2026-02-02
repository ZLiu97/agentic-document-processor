import ollama
from core.json_utils import safe_json_loads
from llm.prompts import TASK_SYSTEM

def interpret_task(model: str, user_instruction: str) -> dict:
    messages = [
        {"role": "system", "content": TASK_SYSTEM},
        {"role": "user", "content": user_instruction}
    ]
    resp = ollama.chat(model=model, messages=messages)
    raw = resp["message"]["content"].strip()
    return safe_json_loads(raw)