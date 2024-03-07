


import pytesseract
from PIL import Image
from openpyxl import Workbook
import docx

# Function to extract text from an image using Tesseract OCR

# Load the image
img = Image.open(r"C:\Users\monal\Downloads\5.jpg").convert('L')  # Convert to grayscale (optional)

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Extract text using Tesseract (English by default)
text = pytesseract.image_to_string(img, lang='eng+mar+hin')

# Print the extracted text
print(text)


document = docx.Document()

# Split the extracted text into lines (adjust based on your needs)
text_lines = text.splitlines()

# Add each line as a paragraph to the document
for line in text_lines:
    paragraph = document.add_paragraph(line)


# Save the document with a filename
document.save("extracted_text6mar.docx")
