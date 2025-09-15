# 🧾 Invoice Categorization & Tagging API

This project provides a FastAPI-based system to **categorize invoices** (e.g., expense type, department, project) and **extract key entities** (e.g., dates, invoice numbers, amounts, vendors).  

It uses:
- **spaCy** → for entity recognition and preprocessing  
- **Transformers (BART MNLI)** → for zero-shot categorization  
- **pdfplumber** → for extracting text from PDF invoices  
- **FastAPI** → to serve as an API  

---

## 🚀 Features
- Upload and process both **`.txt`** and **`.pdf`** invoices  
- Automatic **categorization** (expense type, department, project)  
- Automatic **entity extraction** (dates, amounts, invoice numbers, vendors, etc.)  
- REST API endpoints to process invoices  
- Ready to integrate into financial systems for better **tracking and reporting**  

---

## 🛠️ Installation

## create a virtual environment
python -m venv venv
venv\Scripts\activate   # On Windows
source venv/bin/activate # On Mac/Linux

## Install dependencies

pip install -r requirements.txt

## Download spacy model 
python -m spacy download en_core_web_sm


## Run the API

uvicorn app:app --reload


###  Clone this repository
```bash
git clone https://github.com/YOUR_USERNAME/invoice-categorization-tagging.git
cd invoice-categorization-tagging


![Image Alt](https://github.com/wns-abhishekkum/wns-projects-GenAI/blob/3add8f1413c12885cc8f9aef38474eb306fed8ca/Invoice%20Categorization%20and%20Tagging/Screenshot%20(43).png)


## sample output

{
  "categories": {
    "expense_type": {"label": "software", "confidence": 0.93},
    "department": {"label": "IT", "confidence": 0.97},
    "project": {"label": "Project Alpha", "confidence": 0.62}
  },
  "entities": {
    "CARDINAL": ["4532"],
    "MONEY": ["$450"],
    "DATE": ["12th September 2025"],
    "ORG": ["Microsoft Azure"]
  }
}
 ![Image Alt](https://github.com/wns-abhishekkum/wns-projects-GenAI/blob/3add8f1413c12885cc8f9aef38474eb306fed8ca/Invoice%20Categorization%20and%20Tagging/Screenshot%20(43).png)




