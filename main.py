from telegram import Bot
from dotenv import load_dotenv
import os
import asyncio
import json

load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")


async def send_jobs():
    bot = Bot(token=TOKEN)

    # Load filtered jobs
    with open("database/filtered_jobs.json", "r", encoding="utf-8") as f:
        jobs = json.load(f)

    print("Jobs loaded:", len(jobs))

    # No jobs found
    if len(jobs) == 0:
        await bot.send_message(
            chat_id=CHAT_ID,
            text=" No relevant internships found."
        )
        return

    # Load previously sent jobs
    with open("database/sent_jobs.json", "r", encoding="utf-8") as f:
        sent_jobs = json.load(f)
        
    print("Sent jobs stored:", len(sent_jobs))    

    new_sent_jobs = sent_jobs.copy()
    
    new_jobs_count = 0

    # Send only new jobs
    for job in jobs:  # first 10 jobs

        job_id = f"{job['company']}_{job['role']}"

        if job_id in sent_jobs:
            print("Already sent:", job["role"])
            continue

        message = f"""
    Internship Found

    Company: {job['company']}
    Role: {job['role']}
    Location: {job.get('location', 'Not Available')}
    Apply: {job.get('link', 'Not Available')}
    Source: {job.get('source', 'LinkedIn')}
"""
        
        try:
            print("Sending:", job["role"])

            await bot.send_message(
              chat_id=CHAT_ID,
              text=message
            )

            new_jobs_count += 1
            new_sent_jobs.append(job_id)

            await asyncio.sleep(1)

        except Exception as e:
            print("Telegram Error:", e)
            continue

    # Save updated sent jobs list
    with open("database/sent_jobs.json", "w", encoding="utf-8") as f:
        json.dump(new_sent_jobs, f, indent=4)
        
    print("Sent jobs after update:", len(new_sent_jobs))    

    print(f"New jobs sent: {len(new_sent_jobs) - len(sent_jobs)}")


asyncio.run(send_jobs())