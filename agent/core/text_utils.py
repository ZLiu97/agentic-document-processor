import re

def extract_placeholders(template: str):
    return re.findall(r"{(.*?)}", template)


def fill_template(template: str, data: dict) -> str:
    content = template
    for key in extract_placeholders(template):
        value = data.get(key, f"No {key} found")
        if isinstance(value, list):
            value = "\n".join(str(v) for v in value)
        content = content.replace(f"{{{key}}}", str(value))
    return content