import requests

def scrape_unstop(keywords=["AI", "Machine Learning", "Data Science", "Software Developer"]):
    all_jobs = []
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    for kw in keywords:
        url = f"https://unstop.com/api/public/opportunity/search-new?opportunity=internships&searchTerm={kw}"
        try:
            res = requests.get(url, headers=headers, timeout=10)
            if res.status_code == 200:
                data = res.json().get('data', {}).get('data', [])
                for item in data:
                    title = item.get('title', '').strip()
                    org = item.get('organisation', {})
                    company = org.get('name', 'Startup/Company').strip() if isinstance(org, dict) else 'Startup/Company'
                    seo_url = item.get('seo_url', '')
                    location = item.get('job_detail', {}).get('locations', ['India']) if isinstance(item.get('job_detail'), dict) else ['India']
                    loc_str = location[0] if isinstance(location, list) and len(location) > 0 else "India"

                    if title and seo_url:
                        all_jobs.append({
                            "company": company,
                            "role": title,
                            "source": "Unstop",
                            "location": loc_str,
                            "link": seo_url if seo_url.startswith("http") else f"https://unstop.com{seo_url}"
                        })
        except Exception as e:
            print(f"[Unstop] Error searching '{kw}': {e}")

    print(f"[Unstop] Collected {len(all_jobs)} internships.")
    return all_jobs

if __name__ == "__main__":
    jobs = scrape_unstop()
    print("Sample Unstop job:", jobs[0] if jobs else "None")
