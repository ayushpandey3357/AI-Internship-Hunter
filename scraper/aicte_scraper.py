import requests
from bs4 import BeautifulSoup

def scrape_aicte():
    all_jobs = []
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    urls = [
        "https://internship.aicte-india.org/internships?q=AI",
        "https://internship.aicte-india.org/internships?q=Software",
        "https://internship.aicte-india.org/internships?q=Data"
    ]

    for url in urls:
        try:
            res = requests.get(url, headers=headers, timeout=10)
            if res.status_code == 200:
                soup = BeautifulSoup(res.text, "html.parser")
                # Extract links pointing to individual internship pages
                for a in soup.find_all("a", href=True):
                    href = a['href']
                    text = a.get_text(strip=True)
                    if "/internship/" in href or "details" in href.lower():
                        all_jobs.append({
                            "company": "AICTE Partner / Organization",
                            "role": text if text else "AICTE Technical Internship",
                            "source": "AICTE Portal",
                            "location": "India",
                            "link": href if href.startswith("http") else f"https://internship.aicte-india.org{href}"
                        })
        except Exception as e:
            print(f"[AICTE] Error scraping: {e}")

    print(f"[AICTE] Collected {len(all_jobs)} internships.")
    return all_jobs

if __name__ == "__main__":
    jobs = scrape_aicte()
    print("Sample AICTE job:", jobs[0] if jobs else "None")
