from PyPDF2 import PdfReader

def read_pdf(filepath: str) -> str:
    try:
        reader = PdfReader(filepath)
        text = ""
        for page in reader.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted
        return text
    except Exception as e:
        return f"[PDF_ERROR] {e}"