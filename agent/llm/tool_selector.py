import ollama
from core.json_utils import safe_json_loads
from llm.prompts import TOOL_CHOICE_SYSTEM

def call_llm_tool_choice(model: str, filename: str) -> str:
    messages = [
        {"role": "system", "content": TOOL_CHOICE_SYSTEM},
        {"role": "user", "content": filename}
    ]
    resp = ollama.chat(model=model, messages=messages)
    raw = resp["message"]["content"].strip()

    # Try JSON first
    try:
        return safe_json_loads(raw)["tool"]
    except Exception:
        pass

    # Fallback: bare string
    cleaned = raw.strip().replace('"', '').replace("'", "")
    if cleaned in ["read_pdf", "ocr_image", "transcribe_audio"]:
        return cleaned

    raise ValueError(f"Invalid tool selector output: {raw}")
