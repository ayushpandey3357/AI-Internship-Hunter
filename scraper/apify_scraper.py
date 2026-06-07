from apify_client import ApifyClient
from dotenv import load_dotenv
import os
import json

load_dotenv()

client = ApifyClient(os.getenv("APIFY_TOKEN"))

run = client.actor(
    "curious_coder/linkedin-jobs-scraper"
).call(
    run_input={
        "urls": [
            "http://linkedin.com/jobs/search/?currentJobId=4423237942&geoId=102713980&keywords=AIML%20intern&origin=JOB_SEARCH_PAGE_LOCATION_AUTOCOMPLETE",
            "https://www.linkedin.com/jobs/search/?currentJobId=4422695639&geoId=102713980&keywords=Data%20engineer%20intern&origin=JOB_SEARCH_PAGE_SEARCH_BUTTON&refresh=true",
            "https://www.linkedin.com/jobs/search/?currentJobId=4422693652&geoId=102713980&keywords=Java%20developer%20intern&origin=JOB_SEARCH_PAGE_SEARCH_BUTTON&refresh=true",
            "https://www.linkedin.com/jobs/search/?currentJobId=4422675689&geoId=102713980&keywords=machine%20learning%20intern&origin=JOB_SEARCH_PAGE_SEARCH_BUTTON&refresh=true",
            "https://www.linkedin.com/jobs/search/?currentJobId=4424061458&geoId=102713980&keywords=data%20analyst%20intern&origin=JOB_SEARCH_PAGE_KEYWORD_AUTOCOMPLETE&refresh=true",
            "https://www.linkedin.com/jobs/search-results/?currentJobId=4425189775&keywords=software%20developer%20intern&origin=SEMANTIC_SEARCH_LANDING_PAGE",
            "https://www.linkedin.com/jobs/search-results/?currentJobId=4421584585&keywords=backend%20developer%20intern&origin=SEMANTIC_SEARCH_LANDING_PAGE"
            
        ]
    }
)

dataset_id = run.default_dataset_id
print("Dataset ID:", dataset_id)

jobs = []
seen = set()

for item in client.dataset(dataset_id).iterate_items():       

    print("FOUND:", item.get("title"))

    company = item.get("companyName")
    role = item.get("title")

    key = (company, role)

    if key not in seen:
        seen.add(key)

        jobs.append({
          "company": company,
          "role": role,
          "source": "LinkedIn",
          "location": item.get("location"),
          "link": item.get("link")
        })

print("Jobs collected:", len(jobs))

with open("database/jobs.json", "w", encoding="utf-8") as f:
    json.dump(jobs, f, indent=4)

print(f"Saved {len(jobs)} jobs to database/jobs.json")