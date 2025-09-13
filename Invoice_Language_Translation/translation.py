import os
import pandas as pd
import pytesseract
from pdf2image import convert_from_path
import spacy
from transformers import pipeline
import sentencepiece
import sacremoses

# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\u428150\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"


# Initialize spaCy for language detection
nlp = spacy.load("xx_ent_wiki_sm")

# Initialize the translation pipeline from transformers
translator = pipeline("translation", model="Helsinki-NLP/opus-mt-mul-en")

# Directory containing invoice files
 # Ensure this is the correct path to your invoice directory
invoice_dir = r"C:\Users\u428150\OneDrive - WNS\Desktop\wns-projects-GenAI\Invoice_Language_Translation\Inputfiles"

# Output directory for translated text files
output_dir = r"C:\Users\u428150\OneDrive - WNS\Desktop\wns-projects-GenAI\Invoice_Language_Translation\output"

os.makedirs(output_dir, exist_ok=True)


def detect_language(text):
    """
    Detect the language of a given text using a loaded spaCy language model.

    Args:
        text (str): The input text whose language needs to be detected.

    Returns:
        str: The detected language code (e.g., 'en' for English, 'fr' for French).
             If detection fails, returns 'unknown'.

    Notes:
        - Requires `nlp` to be a spaCy pipeline with a language detector component.
        - If the spaCy model does not support language detection, this function 
          may always return the default language or raise an exception.
    """
    try:
        doc = nlp(text)
        return doc.lang_
    except Exception as e:
        print(f"Error detecting language: {e}")
        return 'unknown'


def translate_text(text, dest_lang='en'):
    """
    Translate the given text into a specified target language using a translation pipeline.

    Args:
        text (str): The input text to be translated.
        dest_lang (str, optional): The target language code (default is 'en' for English).

    Returns:
        str: The translated text. If an error occurs, returns the original text.
    """
    try:
        max_length = 400
        lines = text.split('\n')
        chunks = []
        current_chunk = []

        current_length = 0
        for line in lines:
            line_length = len(line)
            if current_length + line_length > max_length:
                chunks.append('\n'.join(current_chunk))
                current_chunk = []
                current_length = 0
            current_chunk.append(line)
            current_length += line_length

        if current_chunk:
            chunks.append('\n'.join(current_chunk))

        translated_chunks = []
        for chunk in chunks:
            translated_chunk = translator(chunk, max_length=512, clean_up_tokenization_spaces=True)[0]['translation_text']
            translated_chunks.append(translated_chunk)
        return '\n'.join(translated_chunks)
    except Exception as e:
        print(f"Error translating text: {e}")
        return text


def extract_text_from_pdf(pdf_path):
    """
    Translate the given text from a source language into a specified target language.

    Args:
        text (str): The input text to be translated.
        src_lang (str, optional): The source language code. Defaults to 'auto' 
            (let the model auto-detect if supported).
        dest_lang (str, optional): The target language code (default is 'en' for English).

    Returns:
        str: The translated text. If an error occurs, returns the original text.
    """
    try:
        pages = convert_from_path(pdf_path)
        text = ''
        for page in pages:
            text += pytesseract.image_to_string(page)
        return text
    except Exception as e:
        print(f"Error extracting text from PDF: {e}")
        return ''

# Read invoices into a DataFrame
invoices = []
for file_name in os.listdir(invoice_dir):
    file_path = os.path.join(invoice_dir, file_name)
    if os.path.isfile(file_path):
        content = ''
        try:
            if file_name.endswith('.txt'):
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
            elif file_name.endswith('.pdf'):
                content = extract_text_from_pdf(file_path)
            elif file_name.endswith('.jpg') or file_name.endswith('.jpeg') or file_name.endswith('.png'):
                content = pytesseract.image_to_string(file_path)
        except Exception as e:
            print(f"Error reading file {file_name}: {e}")
        invoices.append({'file_name': file_name, 'content': content})

df_invoices = pd.DataFrame(invoices)

# Detect language and translate content
df_invoices['language'] = df_invoices['content'].apply(detect_language)
df_invoices['translated_content'] = df_invoices['content'].apply(translate_text)

# Save each translated invoice to a separate text file
for index, row in df_invoices.iterrows():
    output_file_name = f"{os.path.splitext(row['file_name'])[0]}_translated.txt"
    output_file_path = os.path.join(output_dir, output_file_name)
    try:
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            output_file.write(row['translated_content'])
        print(f"Translated invoice saved to: {output_file_path}")
    except Exception as e:
        print(f"Error writing translated file {output_file_name}: {e}")

print("Translation complete. Translated invoices saved to:", output_dir)