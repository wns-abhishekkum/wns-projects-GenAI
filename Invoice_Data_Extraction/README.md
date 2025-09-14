# 📄 Invoice Data Extraction API

A FastAPI-based tool to **extract structured information** (Invoice Number, Date, Vendor, Total Amount) from **invoice PDFs and images**.  
It supports both **rule-based parsing (regex)** and **LLM-powered extraction (LangChain + OpenAI)**.  
OCR can be done using **Tesseract** or **Azure OCR**.

---

## 🚀 Features
- 📑 Extracts text from **PDFs and Images**
- 🔍 Parses invoice fields using **Regex & Rule-based templates**
- 🤖 Supports **LangChain + OpenAI** for more accurate structured extraction
- 🔡 Works with **Tesseract OCR** (local) or **Azure OCR**
- ⚡ FastAPI service with Swagger UI for testing
- 🧪 Includes a `test.py` client script to send invoices to the API

---

## 📂 Project Structure
```
Invoice_Data_Extraction/
│── main.py                # FastAPI app
│── config.py              # Config (OCR keys, Tesseract path, etc.)
│── ocr_utils.py           # PDF/Image text extraction (Tesseract / pdfplumber / Azure OCR)
│── parser.py              # Regex-based invoice parsing
│── langchain_agent.py     # LangChain + OpenAI structured extraction
│── test.py                # Client script to test API
│── requirements.txt
│── sample_invoices/       # Example invoices (PDF/Images)
│── README.md
```

---

## 🔧 Installation

### 1. Clone Repository
```bash
git clone https://github.com/your-username/invoice-data-extraction.git
cd invoice-data-extraction
```

### 2. Create Virtual Environment
```bash
python -m venv IDEenv
source IDEenv/bin/activate   # Linux/Mac
IDEenv\Scripts\activate      # Windows
```

### 3. Install Requirements
```bash
pip install -r requirements.txt
```

---

## ⚙️ Configuration

### 🔹 `.env` file (recommended)
Create a `.env` file in project root:
```
AZURE_OCR_ENDPOINT=https://<your-cognitive-service>.cognitiveservices.azure.com/
AZURE_OCR_KEY=<your-azure-ocr-key>

AZURE_OPENAI_ENDPOINT=https://<your-openai-resource>.openai.azure.com/
AZURE_OPENAI_KEY=<your-azure-openai-key>
```

Also set Tesseract path in `config.py` if using local OCR:
```python
TESSERACT_PATH = r"C:\Users\u428150\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"  # adjust for your OS"
```

---

## ▶️ Running the API
Start FastAPI server:
```bash
uvicorn main:app --reload
```

Visit Swagger UI:
👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 📤 API Usage

### Endpoint: `/extract`
**Method:** `POST`  
**Parameters:**
- `file`: Invoice file (PDF/Image)
- `use_langchain`: `true/false` (default: `false`)

**Example (cURL):**
```bash
curl -X POST "http://127.0.0.1:8000/extract"   -F "file=@sample_invoices/invoice1.pdf"   -F "use_langchain=true"
```

**Response:**
```json
{
  "invoice_data": {
    "invoice_number": "INV-12345",
    "date": "2024-05-12",
    "vendor": "ABC Supplies Ltd.",
    "total": "1500.00"
  }
}
```

---

## 🧪 Testing with `test.py`
You can test without Postman using the provided client:
```bash
python test.py
```

This script uploads sample invoices and prints results.

---

## 📦 Requirements
```
fastapi
uvicorn
pytesseract
Pillow
pdfplumber
requests
langchain
langchain-openai
openai
python-dotenv
python-multipart
```

---

## ⚡ Notes
- If using **pdf2image**, you need [Poppler](https://github.com/oschwartz10612/poppler-windows/releases/) installed.  
- If using **Tesseract OCR**, install [Tesseract OCR](https://github.com/tesseract-ocr/tesseract).  
- For **Azure OCR**, set `AZURE_OCR_ENDPOINT` and `AZURE_OCR_KEY` in `.env`.  
- For **Azure OpenAI / OpenAI API**, configure your keys in `.env`.  

---

## 📌 Roadmap
- [ ] Add support for invoice line-item extraction  
- [ ] Improve regex rules with template matching  
- [ ] Add Dockerfile for easy deployment  
- [ ] Add database integration for saving extracted invoices  

---

## 📝 License
MIT License © 2025  
