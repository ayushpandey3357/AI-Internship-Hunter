# AI Internship Hunter 

AI Internship Hunter is an automated internship discovery system that searches for internships from LinkedIn, filters relevant opportunities, and sends real-time notifications through Telegram.

## Features

* LinkedIn internship scraping using Apify
* AI/Data-related internship filtering
* Duplicate removal
* Telegram notifications
* Location tracking
* Direct application links
* Secure API key management using `.env`

## Tech Stack

* Python
* Apify
* Telegram Bot API
* JSON
* Git & GitHub

## Project Workflow

LinkedIn Jobs → Apify Scraper → jobs.json → AI Filter → filtered_jobs.json → Telegram Notifications

## Folder Structure

AI-Internship-Hunter/

├── ai/

├── scraper/

├── telegram_bot/

├── database/

├── main.py

├── requirements.txt

└── README.md

## How to Run

### 1. Clone Repository

```bash
git clone <repository-url>
cd AI-Internship-Hunter
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Create .env

```env
APIFY_TOKEN=your_apify_token
TELEGRAM_TOKEN=your_telegram_token
CHAT_ID=your_chat_id
```

### 5. Run

```bash
python scraper/apify_scraper.py
python ai/scorer.py
python main.py
```

## Future Improvements

* Internshala Integration
* Naukri Integration
* Wellfound Integration
* Database Storage
* Automatic Scheduling

## Author

Ayush Kumar Pandey
B.Tech CSE | Aspiring Data Engineer
