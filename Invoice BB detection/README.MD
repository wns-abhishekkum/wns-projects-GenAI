# Invoice Bounding Box Drawing (PDF & DOCX)

This project is a **Streamlit application** that extracts text from **PDF and DOCX** files and highlights important elements such as **dates, numbers, and percentages** with bounding boxes.  

It supports:
-  Single and Multi-page PDF processing  
-  Single and Multi-page DOCX simulation (splits text into pages)  
-  Automatic bounding box drawing with Tesseract OCR  
-  Annotated visualization in the Streamlit UI  

---


## Features

- Extracts text from PDF and Word documents
- Uses **Tesseract OCR** to detect words and positions
- Draws bounding boxes around:
  - Dates (various formats)
  - Numbers (integers, decimals)
  - Percentages (e.g., `45%`)
- Handles **multi-page documents**
- Displays extracted text + annotated images in the Streamlit web app

---


Requirements:
pip install -r reqiurements.txt

Run:
    streamlit run file with .py extension

---

## Installation

1. **Clone the repository**

```bash
git clone https://github.com/your-username/invoice-bounding-box.git
cd invoice-bounding-box

## Install dependencies


## Install Tesseract OCR

>> Download Tesseract OCR

>> Install it and note the installation path (e.g., C:\Program Files\Tesseract-OCR\tesseract.exe).

# Update your script if needed:

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


---
## Usage

Run the Streamlit app:

## streamlit run app.py
