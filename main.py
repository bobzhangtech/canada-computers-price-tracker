from config import (
    MIN_INTERVAL,
    MAX_INTERVAL,
    MIN_DELAY,
    MAX_DELAY,
    DATABASE_NAME,
)
from scraper import scrape_cc
from database import create_table, save_price, get_last_price, get_recent_db_entries
import sqlite3
import time
import random

print("Enter the Canada Computers product URLs to track.")
print("Paste one URL per line. Press Enter on an empty line when done.\n")
urls_to_track = []
while True:
    url = input("URL (or press Enter to finish): ").strip()
    if not url:
        if urls_to_track:
            break
        print("Please enter at least one URL.")
    else:
        urls_to_track.append(url)
        print(f"  Added ({len(urls_to_track)} total)")

print(f"\nTracking {len(urls_to_track)} product(s). Starting now...\n")

connection = sqlite3.connect(DATABASE_NAME)
cursor = connection.cursor()
create_table(cursor)
connection.commit()
connection.close()

while True:
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    INTERVAL = random.randint(MIN_INTERVAL, MAX_INTERVAL)

    print(f"\n--- Starting SCAN at {time.ctime()} ---")

    for url in urls_to_track:
        print(f"\nScraping {url}...")
        name, price = scrape_cc(url)

        if name:
            last_price = get_last_price(cursor, name)
            if last_price is None:
                print(f"First time seeing {name}!")
            elif last_price < price:
                print(f"{name} has INCREASED from ${last_price} to ${price}!")
            elif last_price > price:
                print(f"{name} has DECREASED from ${last_price} to ${price}!")
            else:
                print(f"No change, still ${price}...")

            save_price(cursor, name, price)
            connection.commit()
            print("Saved to database!")

        else:
            print("Failed to find product data...")

        time.sleep(random.uniform(MIN_DELAY, MAX_DELAY))

    print("\n--- Recent Database Entries ---")
    rows = get_recent_db_entries(cursor)
    for row in rows:
        print(row)

    connection.close()
    hours = INTERVAL // 3600
    minutes = (INTERVAL % 3600) // 60
    print(f"\nScan complete. Sleeping for {hours} hours and {minutes} minutes...")
    time.sleep(INTERVAL)
