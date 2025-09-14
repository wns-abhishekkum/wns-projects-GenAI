import os
import shutil
from fastapi import FastAPI, UploadFile, Form
from ocr_utils import extract_text_tesseract, extract_text_pdf
from parser import parse_invoice_text
from langchain_agent import extract_with_langchain

app = FastAPI(title="Invoice Data Extraction API")

@app.post("/extract")
async def extract_invoice(file: UploadFile, use_langchain: bool = Form(False)):
    """
    Upload an invoice (PDF/Image) and extract invoice fields.
    """
    temp_file = f"temp_{file.filename}"
    with open(temp_file, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    if temp_file.lower().endswith(".pdf"):
        text = extract_text_pdf(temp_file)
    else:
        text = extract_text_tesseract(temp_file)

    os.remove(temp_file)  # cleanup

    if use_langchain:
        result = extract_with_langchain(text)
    else:
        result = parse_invoice_text(text)

    return {"invoice_data": result}
