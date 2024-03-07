import streamlit as st
import pytesseract
from PIL import Image
import docx
import base64

# Function to extract text from an image using Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
def extract_text(image):
    img = image.convert('L')
    text = pytesseract.image_to_string(img, lang='eng+mar+hin')
    return text

# Main function to run the Streamlit app
def main():
    st.title("Image Text Extraction with Tesseract OCR")

    # File uploader to upload the image
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        # Display the uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        if st.button("Extract Text"):
            # Extract text from the uploaded image
            extracted_text = extract_text(image)
            st.write("Extracted Text:")
            st.write(extracted_text)

            # Save extracted text to a Word document
            document = docx.Document()
            text_lines = extracted_text.splitlines()
            for line in text_lines:
                paragraph = document.add_paragraph(line)
            document.save("extracted_text.docx")

            with open("extracted_text.docx", "rb") as file:
                btn = st.download_button(
                        label="Download file",
                        data=file,
                        file_name="file.docx",
                        mime="text/docx"
                                    )



# Run the Streamlit app
if __name__ == "__main__":
    main()
