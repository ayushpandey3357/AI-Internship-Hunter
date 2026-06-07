import os

print("Step 1: Scraping jobs...")
os.system("python scraper/apify_scraper.py")

print("Step 2: Filtering jobs...")
os.system("python ai/scorer.py")

print("Step 3: Sending Telegram alerts...")
os.system("python main.py")

print("Done!")