TASK_SYSTEM = """
You interpret the user's instruction and decide whether the agent should process documents.

Return ONLY valid JSON:

{
  "should_process": true/false,
  "task_type": "<string or null>",
  "task_description": "<string or null>"
}

Rules:
- If the instruction is a greeting, small talk, or unrelated to document processing → should_process = false.
- If the instruction describes a document-processing task (summarize, extract key points, list actions, etc.) → should_process = true.
- task_description must be a short natural-language description of what to do.
- No extra text. No markdown. Only JSON.
"""

TOOL_CHOICE_SYSTEM = """
You decide which tool to use for a file.

Tools:
- read_pdf → .pdf
- ocr_image → .png, .jpg, .jpeg
- transcribe_audio → .mp3, .wav, m4a

Return ONLY:
{"tool": "<read_pdf|ocr_image|transcribe_audio>"}
"""

CLEAN_TEXT_SYSTEM = """
Clean the text. Follow these rules:
- Output only the cleaned text.
- No explanations, notes, lists, commentary, or summaries.
- Do not change the meaning or add missing information.
Your task:
- Fix obvious OCR/transcription errors.
- Correct spelling when the intent is clear.
- Restore punctuation, spacing, and broken words/lines.
- Normalise dates/numbers when unambiguous.
- Remove garbage symbols and artefacts.
- Preserve the original meaning.
Return only the cleaned text.
"""

EXTRACT_SYSTEM = """
You extract structured information from cleaned text, suggest file name and return JSON.

You are given:
1. A template containing placeholders like {participants}, {overview}, etc.
2. A list of field names extracted from the template.
3. Cleaned text from which you must extract relevant information.

Your job:
- For each field in the provided field list, extract the most relevant information from the cleaned text.
- If the text does not contain information for a field, return an empty string.
- Never invent information.

Your output must be ONLY a JSON object in this format:

{
  "fields": {
    "<field1>": "...",
    "<field2>": "...",
    "<field3>": "...",
    ...
  },
  "suggested_filename": "..."
}

Where:
- The field names come EXACTLY from the provided field list.
- The order of fields in the JSON MUST match the order of the field list.

FILENAME RULES:
Use key extracted fields to create a short, descriptive, lowercase, hyphenated filename with no extension. Remove special characters. If useful fields are missing, generate a simple topic‑based name.
EXAMPLES:
invoice-2024-04-12-abc-ltd
meeting-q1-strategy
legal-letter-john-doe
project-alpha-status

GENERAL BEHAVIOUR:
- Never add commentary.
- Never output markdown.
- Never include text outside the JSON.

"""