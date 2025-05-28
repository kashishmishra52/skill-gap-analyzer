# test_resume_parser.py
from resume_parser.extract_skills import extract_text_from_pdf, extract_skills

pdf_path = "resume.pdf"  # your own resume
text = extract_text_from_pdf(pdf_path)
skills = extract_skills(text)

print("Extracted Skills:", skills)
