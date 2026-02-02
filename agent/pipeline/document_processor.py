import os
from pathlib import Path

from core.text_utils import extract_placeholders, fill_template
from core.file_utils import save_markdown
from core.logging_utils import log

from reader.pdf_reader import read_pdf
from reader.audio_reader import transcribe_audio
from reader.image_reader import ocr_image

from llm.text_cleaner import clean_text
from llm.extractor import call_llm_extract
from llm.tool_selector import call_llm_tool_choice

class DocumentProcessor:
    def __init__(self, models, template, output_dir):
        self.models = models
        self.template = template
        self.output_dir = output_dir

    def read(self, filepath: str, tool: str):
        if tool == "read_pdf":
            return read_pdf(filepath)
        if tool == "ocr_image":
            return ocr_image(filepath)
        if tool == "transcribe_audio":
            return transcribe_audio(filepath)
        return f"[UNKNOWN_TOOL] {tool}"

    def process(self, filepath: str, task_description: str):
        suffix = Path(filepath).suffix.lower()
        filename = os.path.basename(filepath)

        tool = call_llm_tool_choice(self.models["task"], filename)
        log(f"Detected {suffix} → using {tool}")
        
        raw = self.read(filepath, tool)
        cleaned = clean_text(self.models["clean"], raw)

        fields = extract_placeholders(self.template)
        result = call_llm_extract(
            self.models["extract"],
            cleaned,
            fields,
            self.template,
            task_description,
        )

        content = fill_template(self.template, result["fields"])
        saved_path = save_markdown(result["suggested_filename"], content, self.output_dir)

        log(f"Saved → {saved_path}")






