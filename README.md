# AI Internship Hunter 🚀

AI Internship Hunter is an automated, multi-platform internship discovery system built with Python, JobSpy, GitHub Actions, and the Telegram Bot API.

## Features

* **Multi-Platform Scraping:** Automatically aggregates internships from **LinkedIn**, **Indeed**, **Glassdoor**, **Internshala**, **Unstop (Dare2Compete)**, **AICTE Portal**, and **Wellfound (AngelList)**.
* **Smart Role Filtering:** Filters target roles across AI/ML, Data Engineering, Data Science, SDE, Backend, and Full-Stack Engineering.
* **Instant Alerts:** Sends real-time Telegram notifications for newly posted opportunities.
* **Deduplication:** Prevents duplicate notifications using a tracking database (`database/sent_jobs.json`).
* **100% Free & Automated:** Powered by `python-jobspy` (no paid API tokens/Apify required) and runs on schedule via GitHub Actions.

## Tech Stack

* **Python 3.12**
* **`python-jobspy`** (LinkedIn, Indeed, Glassdoor, ZipRecruiter)
* **BeautifulSoup4 & `curl_cffi`** (Internshala, AICTE, Wellfound)
* **Telegram Bot API**
* **GitHub Actions** (CI/CD Automation)

## Workflow

1. Aggregate internships from all 7+ job platforms
2. Save raw listings in `database/jobs.json`
3. Filter target AI/ML & Engineering roles in `ai/scorer.py`
4. Deduplicate against previously notified jobs
5. Dispatch live Telegram notifications
6. Commit updated job history automatically

## Project Structure

```
AI-Internship-Hunter/
├── ai/
│   └── scorer.py
├── scraper/
│   ├── jobspy_scraper.py      # LinkedIn, Indeed, Glassdoor
│   ├── internshala_scraper.py  # Internshala
│   ├── unstop_scraper.py       # Unstop (Dare2Compete)
│   ├── aicte_scraper.py        # AICTE Portal
│   ├── wellfound_scraper.py    # Wellfound (AngelList)
│   └── multi_scraper.py        # Aggregator
├── database/
│   ├── jobs.json
│   ├── filtered_jobs.json
│   └── sent_jobs.json
├── .github/workflows/
│   └── internship-hunter.yml
├── main.py
├── run_pipeline.py
└── requirements.txt
```

## Setup & Running Locally

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/AI-Internship-Hunter.git
   cd AI-Internship-Hunter
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up `.env`:**
   ```env
   TELEGRAM_TOKEN=your_telegram_bot_token
   CHAT_ID=your_telegram_chat_id
   ```

4. **Run the pipeline:**
   ```bash
   python run_pipeline.py
   ```

## Author

**Ayush Kumar Pandey** | B.Tech CSE
