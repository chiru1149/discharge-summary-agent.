
from tools.pdf_extractor import extract_text
from tools.conflict_detector import detect_conflicts
from tools.medication_reconciliation import reconcile_medications

def run_agent(pdf_path):
    text = extract_text(pdf_path)
    conflicts = detect_conflicts(text)
    meds = reconcile_medications(text)
    return {
        "summary":"Draft discharge summary generated",
        "conflicts": conflicts,
        "medications": meds
    }
