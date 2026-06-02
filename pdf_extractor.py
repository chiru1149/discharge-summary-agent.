
import fitz

def extract_text(pdf_path):
    try:
        doc = fitz.open(pdf_path)
        return "\n".join(page.get_text() for page in doc)
    except Exception as e:
        return f"PDF extraction failed: {e}"
