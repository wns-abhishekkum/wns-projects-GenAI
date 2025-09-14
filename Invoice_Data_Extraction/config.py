
import os
from dotenv import load_dotenv

load_dotenv()  # reads .env file

AZURE_ENDPOINT = os.getenv("endpoint")
AZURE_KEY = os.getenv("subscription_key")


# Azure OCR config
# AZURE_ENDPOINT = os.getenv("AZURE_OCR_ENDPOINT", "https://your-endpoint.cognitiveservices.azure.com/")
# AZURE_KEY = os.getenv("AZURE_OCR_KEY", "your-key-here")

# Tesseract config
# TESSERACT_PATH = r"C:\Program Files\Tesseract-OCR\tesseract.exe" 
TESSERACT_PATH = r"C:\Users\u428150\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"  # adjust for your OS
# pytesseract.pytesseract.tesseract_cmd = r"C:\Users\u428150\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"
