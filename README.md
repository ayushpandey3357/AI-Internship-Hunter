# AI Internship Hunter

AI Internship Hunter is an automated internship discovery system built with Python, Apify, GitHub Actions, and Telegram Bot API.

## Features

* Scrapes internship opportunities from LinkedIn using Apify
* Filters AI/ML, Data Engineering, Data Science, SDE, Backend, Full Stack,     and Software Engineering roles
* Sends instant Telegram notifications for new opportunities
* Prevents duplicate notifications using a job tracking database
* Runs automatically through GitHub Actions
* Uses secure GitHub Secrets for API credentials

## Tech Stack

* Python
* Apify
* Telegram Bot API
* GitHub Actions
* JSON Database

## Workflow

1. Scrape LinkedIn internships
2. Store jobs in `jobs.json`
3. Filter relevant roles
4. Remove duplicates
5. Send Telegram notifications
6. Save sent jobs history

## Project Structure

AI-Internship-Hunter/
├── ai/
├── scraper/
├── telegram_bot/
├── database/
├── .github/workflows/
├── main.py
├── run_pipeline.py
└── requirements.txt

## Automation

The workflow runs automatically using GitHub Actions and delivers new internship opportunities directly to Telegram.


## Author

Ayush Kumar Pandey |
B.Tech CSE 

