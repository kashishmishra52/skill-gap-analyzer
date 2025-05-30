from resume_parser.extract_skills import extract_text_from_pdf, extract_skills
from job_parser.extract_job_skills import load_job_descriptions, extract_skills_from_job
from recommender.recommend_resources import load_resources, recommend_for_skills

# Load resume
resume_text = extract_text_from_pdf("resume.pdf")
resume_skills = extract_skills(resume_text)
print("✅ Resume Skills:", resume_skills)

# Load jobs
jobs = load_job_descriptions("data/jobs.json")
chosen_role = "Data Analyst"
job = next(job for job in jobs if job["title"].lower() == chosen_role.lower())

# Extract job skills
job_skills = extract_skills_from_job(job["description"])
print("✅ Job Required Skills:", job_skills)

# Skill Gap
missing_skills = [skill for skill in job_skills if skill not in resume_skills]
print("⚠️ Missing Skills:", missing_skills)

# Recommendations
resource_map = load_resources()
recommendations = recommend_for_skills(missing_skills, resource_map)

print("\n📚 Recommended Resources:")
for skill, links in recommendations.items():
    print(f"\n🔹 {skill.upper()}:")
    for link in links:
        print(f"   - {link}")
