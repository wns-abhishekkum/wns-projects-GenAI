import re

def parse_invoice_text(text: str) -> dict:
    """Extract invoice fields using regex and rule-based parsing"""
    
    invoice_number = re.search(r"Invoice\s*Number[:\-]?\s*(\w+)", text, re.IGNORECASE)
    date = re.search(r"(?:Date|Invoice Date)[:\-]?\s*([\d\/\-\.]+)", text, re.IGNORECASE)
    total = re.search(r"(?:Total|Amount Due)[:\-]?\s*\$?([\d,]+\.\d{2})", text, re.IGNORECASE)
    vendor = re.search(r"(?:Vendor|From)[:\-]?\s*([A-Za-z0-9\s\.,&\-]+)", text, re.IGNORECASE)

    return {
        "invoice_number": invoice_number.group(1) if invoice_number else None,
        "date": date.group(1) if date else None,
        "total": total.group(1) if total else None,
        "vendor": vendor.group(1) if vendor else None
    }
