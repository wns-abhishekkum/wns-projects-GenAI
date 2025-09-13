# Invoice Translation and Language Detection
## Project Background
This project extracts text from invoices (PDF, image, or text format), detects the source language, translates the content into English, and saves the translated results in separate text files.  

It leverages **OCR (Tesseract)**, **spaCy for language detection**, and **Hugging Face Transformers for translation**.

## 🚀 Features
- Extracts text from:
  - **PDF invoices** (via `pdf2image` + Tesseract OCR)
  - **Image invoices** (`.jpg`, `.jpeg`, `.png`)
  - **Plain text invoices** (`.txt`)
- Detects language using **spaCy multilingual model**
- Translates content to **English** using **Helsinki-NLP/opus-mt-mul-en**
- Saves results as `_translated.txt` files
- Handles large text blocks with chunking


## Invoice_Language_Translation/
    │
    ├── Inputfiles/ # Place invoice files here (PDF, TXT, JPG, PNG)
    ├── output/ # Translated invoices will be saved here
    ├── invoice_translation.py # Main script
    ├── requirements.txt # Dependencies list
    └── README.md # Project documentation


## Requirements
pandas
pytesseract
pdf2image
spacy
transformers
sentencepiece
sacremoses

You also need to have Tesseract OCR installed on your machine. You can download it from here.

## Setup Instructions

   ```bash
    ##cd Invoice_Language_Translation
Install the required Python libraries:
   ```bash
    pip install -r requirements.txt
Ensure that Tesseract OCR is installed and update the `pytesseract.pytesseract.tesseract_cmd` path in the code to point to your Tesseract executable.
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\u428150\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"



## Running the Code
1. Place your invoice files (PDFs, images, or text files) in the `Inputfiles` directory.
2. Run the script:
   ```bash
    python translation.py
3. The translated invoices will be saved in the output directory.

## Example Run and Output
When you run the script, it processes each invoice file, detects the language, translates the content to English, and saves the translated text in a new file. Here’s a sample output:

   ```bash
   
```
## Screenshot of Application Running
Screenshot(40).png
The above screenshot shows the script processing invoices and saving translated versions in the specified directory.

## Issues and Error Handling
The script includes basic error handling for issues such as file reading errors, language detection, and translation errors. If any errors occur during processing, the script will print an error message to the console and continue with the next file.
