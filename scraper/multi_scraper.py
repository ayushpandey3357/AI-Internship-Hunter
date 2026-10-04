import json
import os
from scraper.jobspy_scraper import scrape_jobspy_platforms
from scraper.internshala_scraper import scrape_internshala
from scraper.unstop_scraper import scrape_unstop
from scraper.aicte_scraper import scrape_aicte
from scraper.wellfound_scraper import scrape_wellfound

def run_all_scrapers():
    print("==========================================")
    print("[*] Starting Multi-Platform Internship Scraper")
    print("==========================================")

    all_jobs = []

    # 1. JobSpy Platforms (LinkedIn, Indeed, Glassdoor) - Agent Recommended
    print("\n--- 1. Scraping LinkedIn, Indeed, Glassdoor (JobSpy) ---")
    all_jobs.extend(scrape_jobspy_platforms())

    # 2. Unstop (Dare2Compete) - Agent Recommended
    print("\n--- 2. Scraping Unstop (Indian Tech & AI Internships) ---")
    all_jobs.extend(scrape_unstop())

    # 3. Internshala - User Recommended
    print("\n--- 3. Scraping Internshala ---")
    all_jobs.extend(scrape_internshala())

    # 4. AICTE Internship Portal - User Recommended
    print("\n--- 4. Scraping AICTE Portal ---")
    all_jobs.extend(scrape_aicte())

    # 5. Wellfound (AngelList) - User Recommended
    print("\n--- 5. Scraping Wellfound (Startup Roles) ---")
    all_jobs.extend(scrape_wellfound())

    # Deduplicate gathered jobs by (company, role)
    unique_jobs = []
    seen = set()

    for job in all_jobs:
        company = str(job.get("company", "")).strip().lower()
        role = str(job.get("role", "")).strip().lower()
        key = (company, role)

        if key not in seen:
            seen.add(key)
            unique_jobs.append(job)

    # Ensure database directory exists
    os.makedirs("database", exist_ok=True)

    with open("database/jobs.json", "w", encoding="utf-8") as f:
        json.dump(unique_jobs, f, indent=4)

    print("\n==========================================")
    print(f"[OK] Finished! Saved {len(unique_jobs)} unique jobs to database/jobs.json")
    print("==========================================")

if __name__ == "__main__":
    run_all_scrapers()
