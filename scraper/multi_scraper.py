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

    # 1. JobSpy Platforms (LinkedIn, Indeed, Glassdoor)
    print("\n--- 1. Scraping LinkedIn, Indeed, Glassdoor (JobSpy) ---")
    try:
        all_jobs.extend(scrape_jobspy_platforms())
    except Exception as e:
        print(f"[WARNING] JobSpy Scraper encounter error: {e}")

    # 2. Unstop (Dare2Compete)
    print("\n--- 2. Scraping Unstop (Indian Tech & AI Internships) ---")
    try:
        all_jobs.extend(scrape_unstop())
    except Exception as e:
        print(f"[WARNING] Unstop Scraper encounter error: {e}")

    # 3. Internshala
    print("\n--- 3. Scraping Internshala ---")
    try:
        all_jobs.extend(scrape_internshala())
    except Exception as e:
        print(f"[WARNING] Internshala Scraper encounter error: {e}")

    # 4. AICTE Internship Portal
    print("\n--- 4. Scraping AICTE Portal ---")
    try:
        all_jobs.extend(scrape_aicte())
    except Exception as e:
        print(f"[WARNING] AICTE Scraper encounter error: {e}")

    # 5. Wellfound (AngelList)
    print("\n--- 5. Scraping Wellfound (Startup Roles) ---")
    try:
        all_jobs.extend(scrape_wellfound())
    except Exception as e:
        print(f"[WARNING] Wellfound Scraper encounter error: {e}")


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
