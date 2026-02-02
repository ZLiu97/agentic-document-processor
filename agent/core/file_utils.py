from pathlib import Path
import re

def list_files(directory: str):
    p = Path(directory)
    return [
        str(f)
        for f in p.iterdir()
        if f.is_file() and f.suffix.lower() in [
            ".pdf", ".m4a", ".mp3", ".wav", ".png", ".jpg", ".jpeg"
        ]
    ]

def save_markdown(filename: str, content: str, out_dir: str) -> str:
    out_dir_path = Path(out_dir)
    out_dir_path.mkdir(parents=True, exist_ok=True)

    base = filename.lower().replace(" ", "-")
    base = re.sub(r"[^a-z0-9\-]", "-", base)
    final_name = base + ".md"

    out_path = out_dir_path / final_name
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(content)

    return str(out_path)