import fitz  # pymupdf
import pytesseract
import cv2
import numpy as np
from PIL import Image
import os

# connect to tesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def preprocess_image(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # noise removal
    gray = cv2.medianBlur(gray, 3)

    # threshold improves OCR accuracy
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

    return thresh


def ocr_image(image_path):
    processed = preprocess_image(image_path)
    text = pytesseract.image_to_string(processed)
    return text


def extract_from_pdf(pdf_path):
    text = ""
    doc = fitz.open(pdf_path)

    for page in doc:
        page_text = page.get_text()

        # if page has no text -> scanned PDF -> OCR
        if page_text.strip() == "":
            pix = page.get_pixmap(dpi=300)
            img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
            temp_img = "temp_page.png"
            img.save(temp_img)

            text += ocr_image(temp_img)
            os.remove(temp_img)
        else:
            text += page_text

    return text


def extract_text_from_report(file_path):
    ext = file_path.lower()

    if ext.endswith(".pdf"):
        return extract_from_pdf(file_path)

    if ext.endswith((".png", ".jpg", ".jpeg")):
        return ocr_image(file_path)

    return "Unsupported file format"