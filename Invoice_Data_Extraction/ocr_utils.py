import pytesseract
from PIL import Image
import fitz  # PyMuPDF
import pdfplumber
import pytesseract
from PIL import Image
import requests
from config import TESSERACT_PATH, AZURE_ENDPOINT, AZURE_KEY

pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH

def extract_text_tesseract(image_path: str) -> str:
    """Extract text from image using Tesseract OCR"""
    image = Image.open(image_path)
    return pytesseract.image_to_string(image)

# def extract_text_pdf(pdf_path: str) -> str:
#     """Extract text directly from PDF using PyMuPDF"""
#     doc = fitz.open(pdf_path)
#     text = ""
#     for page in doc:
#         text += page.get_text("text")
#     return text




def extract_text_pdf(pdf_path: str) -> str:
    """Extract text from PDF using pdfplumber (no Poppler required)"""
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text





def extract_text_azure(image_path: str) -> str:
    """Extract text from image using Azure OCR"""
    ocr_url = f"{AZURE_ENDPOINT}/vision/v3.2/ocr"
    headers = {"Ocp-Apim-Subscription-Key": AZURE_KEY, "Content-Type": "application/octet-stream"}
    with open(image_path, "rb") as f:
        response = requests.post(ocr_url, headers=headers, data=f)
    result = response.json()
    text = " ".join([word["text"] for region in result.get("regions", []) 
                     for line in region["lines"] 
                     for word in line["words"]])
    return text
