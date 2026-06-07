import subprocess
import sys

print("Step 1: Scraping jobs...")
subprocess.run([sys.executable, "scraper/apify_scraper.py"], check=True)

print("Step 2: Filtering jobs...")
subprocess.run([sys.executable, "ai/scorer.py"], check=True)

print("Step 3: Sending Telegram alerts...")
subprocess.run([sys.executable, "main.py"], check=True)

print("Done!")