import pytesseract
from PIL import Image

# Connect python to tesseract location
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Load image
img = Image.open("sample.png")

# Extract text
text = pytesseract.image_to_string(img)

print("\n----- Extracted Text -----\n")
print(text)