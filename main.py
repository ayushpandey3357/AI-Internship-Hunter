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

    with open("database/filtered_jobs.json", "r", encoding="utf-8") as f:
        jobs = json.load(f)

    print("Jobs loaded:", len(jobs))

    if len(jobs) == 0:
        await bot.send_message(
            chat_id=CHAT_ID,
            text=" No relevant internships found."
        )
        return

    for job in jobs[:10]:  # send first 10 jobs for testing
        message = f"""
    Internship Found

    Company: {job['company']}
    Role: {job['role']}
    Location: {job.get('location', 'Not Available')}
    Apply: {job.get('link', 'Not Available')}
    Source: {job.get('source', 'LinkedIn')}
"""

        await bot.send_message(
            chat_id=CHAT_ID,
            text=message
        )

    print("Messages sent!")

asyncio.run(send_jobs())