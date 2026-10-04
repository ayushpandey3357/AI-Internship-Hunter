import requests
from bs4 import BeautifulSoup

def scrape_internshala(categories=["computer-science", "machine-learning", "data-science", "artificial-intelligence-ai"]):
    all_jobs = []
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    for cat in categories:
        url = f"https://internshala.com/internships/{cat}-internship/"
        try:
            res = requests.get(url, headers=headers, timeout=10)
            if res.status_code == 200:
                soup = BeautifulSoup(res.text, "html.parser")
                cards = soup.find_all("div", class_="individual_internship")
                for card in cards:
                    role_elem = card.find("a", class_="job-title-href")
                    company_elem = card.find("p", class_="company-name")
                    location_elem = card.find("a", class_="location_link")

                    if role_elem and company_elem:
                        role = role_elem.get_text(strip=True)
                        company = company_elem.get_text(strip=True)
                        link = "https://internshala.com" + role_elem['href']
                        location = location_elem.get_text(strip=True) if location_elem else "Work From Home"

                        all_jobs.append({
                            "company": company,
                            "role": role,
                            "source": "Internshala",
                            "location": location,
                            "link": link
                        })
        except Exception as e:
            print(f"[Internshala] Error scraping category '{cat}': {e}")

    print(f"[Internshala] Collected {len(all_jobs)} internships.")
    return all_jobs

if __name__ == "__main__":
    jobs = scrape_internshala()
    print("Sample Internshala job:", jobs[0] if jobs else "None")
