import pandas as pd
import pdfplumber
import pytesseract
from PIL import Image
from docx.api import Document

def load_data(file_path):
    if file_path.endswith('.csv'):
        return pd.read_csv(file_path)
    
    elif file_path.endswith('.xlsx'):
        return pd.read_excel(file_path)
    
    elif file_path.endswith('.txt'):
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
        
    elif file_path.endswith('.pdf'):
        with pdfplumber.open(file_path) as pdf:
            return "\n".join([page.extract_text() or '' for page in pdf.pages])
        
    elif file_path.endswith('.docx'):
        doc = Document(file_path)
        return "\n".join([para.text for para in doc.paragraphs])
    
    elif file_path.lower().endswith(('.png', '.jpg', '.jpeg')):
        img = Image.open(file_path)
        return pytesseract.image_to_string(img)
    
    else:
        return "Unsupported file format."


if __name__ == "__main__":
    file_path = input("Enter the file path: ").strip()
    content = load_file(file_path)

    if isinstance(content, pd.DataFrame):
        print(" File loaded as DataFrame. Preview:")
        print(content.head())
    elif isinstance(content, str):
        print(" File loaded as Text. Preview:")
        print(content[:1000])  # print only first 1000 characters
    else:
        print("Failed to load file properly.")
