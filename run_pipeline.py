import subprocess
import sys

print("Step 1: Scraping internships across multi-platforms (JobSpy, Unstop, Internshala, AICTE, Wellfound)...")
subprocess.run([sys.executable, "-m", "scraper.multi_scraper"], check=True)

print("\nStep 2: Filtering relevant roles...")
subprocess.run([sys.executable, "ai/scorer.py"], check=True)

print("\nStep 3: Sending Telegram alerts...")
subprocess.run([sys.executable, "main.py"], check=True)

print("\nAll Done!")