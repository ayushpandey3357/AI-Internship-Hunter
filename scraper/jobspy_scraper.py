import json
from jobspy import scrape_jobs

def scrape_jobspy_platforms(keywords=["AI ML intern", "Data Engineering intern", "Software Engineering intern"]):
    all_jobs = []
    
    for keyword in keywords:
        print(f"[JobSpy] Searching: {keyword}...")
        try:
            jobs_df = scrape_jobs(
                site_name=["linkedin", "indeed", "glassdoor"],
                search_term=keyword,
                location="India",
                results_wanted=15,
                hours_old=72,
                country_indeed='India'
            )
            
            if jobs_df is not None and not jobs_df.empty:
                for index, row in jobs_df.iterrows():
                    company = str(row.get('company', 'Unknown')).strip()
                    role = str(row.get('title', 'Unknown')).strip()
                    link = str(row.get('job_url', '')).strip()
                    site = str(row.get('site', 'JobSpy')).capitalize()
                    location = str(row.get('location', 'India')).strip()
                    
                    if role and company and link:
                        all_jobs.append({
                            "company": company,
                            "role": role,
                            "source": site,
                            "location": location,
                            "link": link
                        })
        except Exception as e:
            print(f"[JobSpy] Error scraping '{keyword}': {e}")
            
    print(f"[JobSpy] Collected {len(all_jobs)} jobs.")
    return all_jobs

if __name__ == "__main__":
    jobs = scrape_jobspy_platforms()
    print("Sample job:", jobs[0] if jobs else "None")
