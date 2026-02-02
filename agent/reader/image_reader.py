from PIL import Image
import pytesseract

def ocr_image(filepath: str) -> str:
    try:
        img = Image.open(filepath)
        text = pytesseract.image_to_string(img)
        return text
    except Exception as e:
        return f"[IMAGE_ERROR] {e}"
