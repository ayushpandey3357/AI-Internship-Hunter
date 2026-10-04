from curl_cffi import requests
from bs4 import BeautifulSoup

def scrape_wellfound():
    all_jobs = []
    urls = [
        "https://wellfound.com/role/l/software-engineer/india",
        "https://wellfound.com/role/l/data-scientist/india"
    ]

    for url in urls:
        try:
            res = requests.get(url, impersonate="chrome", timeout=15)
            if res.status_code == 200:
                soup = BeautifulSoup(res.text, "html.parser")
                # Parse job links from Wellfound structure
                job_links = soup.find_all("a", href=True)
                for a in job_links:
                    href = a['href']
                    if "/jobs/" in href and not href.endswith("/jobs"):
                        title = a.get_text(strip=True)
                        if title and len(title) > 3:
                            all_jobs.append({
                                "company": "Startup (Wellfound)",
                                "role": title,
                                "source": "Wellfound",
                                "location": "India / Remote",
                                "link": href if href.startswith("http") else f"https://wellfound.com{href}"
                            })
        except Exception as e:
            print(f"[Wellfound] Error scraping: {e}")

    print(f"[Wellfound] Collected {len(all_jobs)} startup jobs.")
    return all_jobs

if __name__ == "__main__":
    jobs = scrape_wellfound()
    print("Sample Wellfound job:", jobs[0] if jobs else "None")
