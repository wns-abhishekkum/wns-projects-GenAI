from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic import BaseModel
from transformers import pipeline
import spacy
import pdfplumber

# ----------------- Load Models ----------------- #
nlp = spacy.load("en_core_web_sm")
# classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
classifier = pipeline("zero-shot-classification", model="valhalla/distilbart-mnli-12-3")


# Define categories
CATEGORIES = {
    "expense_type": ["travel", "office supplies", "software", "food", "utilities"],
    "department": ["HR", "Finance", "IT", "Sales", "Operations"],
    "project": ["Project Alpha", "Project Beta", "Project Gamma"]
}

# ----------------- Helpers ----------------- #
def preprocess_text(text: str) -> str:
    """Clean and preprocess invoice text."""
    doc = nlp(text)
    tokens = [token.lemma_ for token in doc if not token.is_stop and token.is_alpha]
    return " ".join(tokens)


def categorize_invoice(invoice_text: str) -> dict:
    """Categorize invoice into predefined categories."""
    cleaned_text = preprocess_text(invoice_text)
    results = {}
    for category, labels in CATEGORIES.items():
        prediction = classifier(cleaned_text, labels)
        best_label = prediction["labels"][0]
        best_score = prediction["scores"][0]
        results[category] = {"label": best_label, "confidence": round(best_score, 2)}
    return results


def extract_entities(invoice_text: str) -> dict:
    """Extract entities like DATE, MONEY, ORG, CARDINAL, QUANTITY."""
    doc = nlp(invoice_text)
    entities = {}
    for ent in doc.ents:
        if ent.label_ in ["DATE", "MONEY", "ORG", "CARDINAL", "QUANTITY"]:
            entities.setdefault(ent.label_, []).append(ent.text)
    return entities


def extract_text_from_pdf(file_path: str) -> str:
    """Extract text from a PDF using pdfplumber."""
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
            text += "\n"
    return text.strip()


# ----------------- FastAPI Setup ----------------- #
app = FastAPI(title="Invoice Categorization & Tagging API")

class InvoiceText(BaseModel):
    text: str


@app.post("/process_text")
async def process_invoice_text(invoice: InvoiceText):
    """Process invoice from raw text."""
    categories = categorize_invoice(invoice.text)
    entities = extract_entities(invoice.text)
    return {"categories": categories, "entities": entities}


@app.post("/process_file")
async def process_invoice_file(file: UploadFile = File(...)):
    """Process invoice from uploaded text or PDF file."""
    if file.filename.endswith(".txt"):
        contents = await file.read()
        text = contents.decode("utf-8")

    elif file.filename.endswith(".pdf"):
        # Save temp file for pdfplumber
        temp_path = f"temp_{file.filename}"
        with open(temp_path, "wb") as f:
            f.write(await file.read())
        text = extract_text_from_pdf(temp_path)

    else:
        raise HTTPException(status_code=400, detail="Only .txt and .pdf files are supported.")

    if not text.strip():
        raise HTTPException(status_code=400, detail="No readable text found in the file.")

    categories = categorize_invoice(text)
    entities = extract_entities(text)
    return {"categories": categories, "entities": entities}
