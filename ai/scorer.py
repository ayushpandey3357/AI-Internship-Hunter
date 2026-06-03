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
    "big data"
]

with open("database/jobs.json", "r", encoding="utf-8") as f:
    jobs = json.load(f)

filtered_jobs = []

for job in jobs:
    title = job["role"].lower()

    if any(keyword in title for keyword in AI_KEYWORDS):
        print("MATCH:", job["role"])
        filtered_jobs.append(job)

with open("database/filtered_jobs.json", "w", encoding="utf-8") as f:
    json.dump(filtered_jobs, f, indent=4)

print(f"Relevant Jobs Found: {len(filtered_jobs)}")