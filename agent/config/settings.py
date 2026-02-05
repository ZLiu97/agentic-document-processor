MODELS = {
    "task": "phi3:3.8b",
    "tool": "phi3:3.8b",
    "clean": "phi3:3.8b",
    "extract": "llama3.1"
}

OPTIONS = {
    "task": {"temperature": 0.1,"top_p": 0.3, "repeat_penalty": 1.2},
    "tool": {"temperature": 0.1,"top_p": 0.3, "repeat_penalty": 1.2},
    "clean": {"temperature": 0.3,"top_p": 0.3, "repeat_penalty": 1.2},
    "extract": {"temperature": 0.3,"top_p": 0.3, "repeat_penalty": 1.2, "num_ctx": 8192}
}

MAX_WORKERS = 4
MAX_TEXT_CHARS = 3000
