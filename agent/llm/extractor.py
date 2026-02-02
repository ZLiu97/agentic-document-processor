import json
import ollama
from core.json_utils import safe_json_loads
from llm.prompts import EXTRACT_SYSTEM
from config.settings import MAX_TEXT_CHARS

def call_llm_extract(model: str, text: str, fields: list[str], template: str, task_description: str) -> dict:
    messages = [
        {"role": "system", "content": EXTRACT_SYSTEM},
        {"role": "user", "content": json.dumps({
            "fields": fields,
            "text": text[:MAX_TEXT_CHARS],
            "template": template,
            "task": task_description
        })}
    ]
    resp = ollama.chat(model=model, messages=messages)
    raw = resp["message"]["content"].strip()
    return safe_json_loads(raw)