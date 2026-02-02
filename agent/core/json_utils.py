import json
import re

CONTROL_CHARS = ''.join(map(chr, range(0, 32)))
CONTROL_CHAR_RE = re.compile('[%s]' % re.escape(CONTROL_CHARS))

def safe_json_loads(raw: str):
    raw = raw.strip()

    # Remove markdown fences
    raw = raw.replace("```json", "").replace("```", "").strip()

    # Remove ASCII control characters
    raw = CONTROL_CHAR_RE.sub('', raw)

    # Extract ONLY the first JSON object
    match = re.search(r"\{(?:[^{}]|(?:\{[^{}]*\}))*\}", raw)
    if not match:
        raise ValueError("No JSON object found in LLM output:\n" + raw)

    json_str = match.group(0)

    # Try strict parse
    try:
        return json.loads(json_str)
    except json.JSONDecodeError:
        pass

    # Attempt repairs
    json_str = json_str.replace("'", '"')
    json_str = re.sub(r",\s*}", "}", json_str)
    json_str = re.sub(r",\s*]", "]", json_str)

    # Remove control chars again
    json_str = CONTROL_CHAR_RE.sub('', json_str)

    return json.loads(json_str)