import json

AI_KEYWORDS = [
    "ai",
    "aiml",
    "machine learning",
    "data science",
    "data engineer",
    "data engineering",
    "data analyst",
    "business intelligence",
    "deep learning",
    "genai",
    "artificial intelligence",
    "analytics",
    "ml engineer",
    "ai/ml",
    "big data",

    # SDE / Software roles
    "software engineer",
    "software developer",
    "software development engineer",
    "sde",
    "backend",
    "full stack",
    "full-stack",
    "java",
    "python developer",
    "engineering"
]

INTERNSHIP_WORDS = [
    "intern",
    "internship",
    "trainee",
    "fresher",
    "entry level"
]

EXCLUDED_WORDS = [
    "teacher",
    "business development",
    "hr",
    "recruiter",
    "sales",
    "marketing"
]

with open("database/jobs.json", "r", encoding="utf-8") as f:
    jobs = json.load(f)

filtered_jobs = []

for job in jobs:
    title = job["role"].lower()
        
    is_target_role = any(keyword in title for keyword in AI_KEYWORDS)
    is_internship = any(word in title for word in INTERNSHIP_WORDS)
    is_excluded = any(word in title for word in EXCLUDED_WORDS)

    if is_target_role and is_internship and not is_excluded:
        print("MATCH:", job["role"])
        filtered_jobs.append(job)    

with open("database/filtered_jobs.json", "w", encoding="utf-8") as f:
    json.dump(filtered_jobs, f, indent=4)

print(f"Relevant Jobs Found: {len(filtered_jobs)}")