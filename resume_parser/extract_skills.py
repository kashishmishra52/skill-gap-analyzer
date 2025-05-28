import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""

    for page in doc:
        text += page.get_text()

    return text
import spacy

nlp = spacy.load("en_core_web_sm")

# A small sample of common tech skills to match
COMMON_SKILLS = ["python", "java", "sql", "html", "css", "javascript", "excel",
                 "machine learning", "deep learning", "pandas", "numpy", "react", "node.js", "flask", "tensorflow"]

def extract_skills(text):
    doc = nlp(text.lower())
    skills_found = []

    for token in doc:
        if token.text in COMMON_SKILLS and token.text not in skills_found:
            skills_found.append(token.text)

    return skills_found
