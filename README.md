# Canada Computers Price Tracker

This is a simple Python script that monitors product prices on the Canada Computers website and alerts you when a price changes.

## How it works

- Prompts you to enter product URLs at startup
- Scrapes each product page every 4-8 hours
- Detects and reports price increases and decreases
- Stores price history in a local SQLite database

## Setup

1. Clone the repo and navigate to the project folder
2. Create and activate a virtual environment:
   ```
   python -m venv .venv
   .venv\Scripts\activate
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

```
python main.py
```

When prompted, paste one Canada Computers product URL per line. Press Enter on an empty line to start tracking.

```
Enter the Canada Computers product URLs to track.
Paste one URL per line. Press Enter on an empty line when done.

URL (or press Enter to finish): https://www.canadacomputers.com/en/...
  Added (1 total)
URL (or press Enter to finish):

Tracking 1 product(s). Starting now...
```

The tracker runs continuously until you stop it with `Ctrl + C`. URLs are not saved between runs, and you will be prompted again on the next launch.

## Notes

- Only works with product pages on `canadacomputers.com`
- Price history is saved in `canada_computers.db` (excluded from version control)
