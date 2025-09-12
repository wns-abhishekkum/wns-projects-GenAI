# if the pdf is having more than one page and docx file support

import streamlit as st
import pdfplumber
import cv2
import numpy as np
from PIL import Image, ImageDraw
from docx import Document
import pytesseract
import re

pytesseract.pytesseract.tesseract_cmd = r"C:\Users\u428150\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"


def extract_pdf_info(pdf_path):
    """
    Extract text and images from all pages of a PDF.

    Args:
        pdf_path (str or file-like): Path to the PDF file or file-like object.

    Returns:
        list of tuples:
            Each tuple contains:
            - text (str): Extracted text from the page.
            - words (list): List of extracted words with positions.
            - pil_image (PIL.Image.Image): Page rendered as a PIL image.
    """
    pages_info = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            words = page.extract_words()
            pil_image = page.to_image(resolution=300).original
            pages_info.append((text, words, pil_image))
    return pages_info


def extract_docx_info(docx_path):
    """
    Extract text and generate page-like images for DOCX content.

    Args:
        docx_path (str or file-like): Path to the DOCX file or file-like object.

    Returns:
        list of tuples:
            Each tuple contains:
            - text (str): Extracted text from the "page".
            - img (numpy.ndarray): OpenCV image with text drawn.
    """
    doc = Document(docx_path)
    paragraphs = [para.text for para in doc.paragraphs]

    pages_info = []
    lines_per_page = 50  # fixing number of lines for easy page split
    for i in range(0, len(paragraphs), lines_per_page):
        page_paras = paragraphs[i:i + lines_per_page]
        text = "\n".join(page_paras)

        # Create blank white image
        img = np.ones((1000, 800, 3), np.uint8) * 255

        # Use PIL to draw text
        pil_img = Image.fromarray(img)
        draw = ImageDraw.Draw(pil_img)
        y = 10
        for para in page_paras:
            draw.text((10, y), para, fill=(0, 0, 0))
            y += 15

        img = np.array(pil_img)
        pages_info.append((text, img))

    return pages_info


def draw_bounding_boxes(img, text):
    """
    Draw bounding boxes around detected dates, numbers, and percentages.

    Args:
        img (numpy.ndarray): Input image (OpenCV format).
        text (str): Extracted text (not directly used).

    Returns:
        numpy.ndarray: Annotated image with bounding boxes.
    """
    try:
        boxes = pytesseract.image_to_data(img, output_type=pytesseract.Output.DICT)

        # Regex patterns
        date_pattern = (
            r'\b\d{1,2}\s(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sept|Oct|Nov|Dec)\s\d{4}\b|'
            r'\b\d{1,2}\s(?:January|February|March|April|May|June|July|August|September|October|November|December)\s\d{4}\b|'
            r'\b\d{4}[-/]\d{2}[-/]\d{2}\b|'
            r'\b\d{2}[-/]\d{2}[-/]\d{4}\b|'
            r'\b\w{3} \d{2}, \d{4}\b|'
            r'\b\d{2} \w{3} \d{4}\b'
        )
        number_pattern = r'-?\d+(\.\d+)?'
        percentage_pattern = r'\d+%'

        for i in range(len(boxes['level'])):
            x, y, bw, bh = boxes['left'][i], boxes['top'][i], boxes['width'][i], boxes['height'][i]
            text_value = boxes['text'][i].lower()

            if re.search(date_pattern, text_value) or re.match(number_pattern, text_value) or re.match(percentage_pattern, text_value):
                color = (255, 165, 0)  # Orange for matches
            else:
                color = (0, 255, 255)  # Yellow otherwise

            img = cv2.rectangle(img, (x, y), (x + bw, y + bh), color, 2)
        return img
    except Exception as e:
        st.error(f"Error drawing bounding boxes: {e}")
        return img


def main():
    """
    Streamlit app entry point for multi-page PDF/DOCX bounding box detection.
    """
    st.title("Invoice Bounding Box Drawing (Multi-Page Support)")

    uploaded_file = st.file_uploader("Choose a file", type=["pdf", "docx"])
    if uploaded_file is not None:
        if uploaded_file.name.endswith('.pdf'):
            pages_info = extract_pdf_info(uploaded_file)
            for idx, (text, words, pil_image) in enumerate(pages_info, start=1):
                st.subheader(f"Page {idx}")
                st.text_area("Extracted Text", text, height=200)

                image = np.array(pil_image)
                annotated_image = draw_bounding_boxes(image, text)
                annotated_image = cv2.cvtColor(annotated_image, cv2.COLOR_BGR2RGB)
                st.image(Image.fromarray(annotated_image), caption=f'Annotated Page {idx}', use_column_width=True)

        elif uploaded_file.name.endswith('.docx'):
            pages_info = extract_docx_info(uploaded_file)
            for idx, (text, image) in enumerate(pages_info, start=1):
                st.subheader(f"Page {idx}")
                st.text_area("Extracted Text", text, height=200)

                annotated_image = draw_bounding_boxes(image, text)
                annotated_image = cv2.cvtColor(annotated_image, cv2.COLOR_BGR2RGB)
                st.image(Image.fromarray(annotated_image), caption=f'Annotated Page {idx}', use_column_width=True)


if __name__ == "__main__":
    main()
