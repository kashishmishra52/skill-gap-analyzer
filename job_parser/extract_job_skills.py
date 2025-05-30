import json
import spacy

nlp = spacy.load("en_core_web_sm")

COMMON_SKILLS = ["python", "sql", "excel", "power bi", "tableau", "pandas", "statistics",
                 "machine learning", "scikit-learn", "tensorflow", "numpy", "flask", "fastapi",
                 "html", "css", "javascript", "react", "rest", "git"]

def load_job_descriptions(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)

def extract_skills_from_job(job_desc):
    doc = nlp(job_desc.lower())
    found = []

    for skill in COMMON_SKILLS:
        if skill in job_desc.lower() and skill not in found:
            found.append(skill)
    return found
