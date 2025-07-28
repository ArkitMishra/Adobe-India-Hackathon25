# src/parser.py

import pdfplumber
import pytesseract
from PIL import Image
import io
import os
import fitz  # PyMuPDF
import cv2
import numpy as np

def extract_text_from_pdf(file_path):
    data = []
    try:
        with pdfplumber.open(file_path) as pdf:
            for i, page in enumerate(pdf.pages):
                print(f"Processing Page {i+1} (Digital PDF)")
                text = page.extract_text()
                if text:
                    blocks = page.extract_words(use_text_flow=True, keep_blank_chars=False)
                    data.append({
                        "page": i + 1,
                        "type": "digital",
                        "content": blocks
                    })
                else:
                    print(f"No text found on Page {i+1}, switching to OCR...")
                    image = page.to_image(resolution=300).original
                    image_array = np.array(image)
                    text_ocr = pytesseract.image_to_string(image_array)
                    data.append({
                        "page": i + 1,
                        "type": "scanned",
                        "content": [{"text": line.strip()} for line in text_ocr.split('\n') if line.strip()]
                    })
    except Exception as e:
        print(f"Error reading PDF: {e}")
    return data
