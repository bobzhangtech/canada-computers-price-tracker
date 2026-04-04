import requests
from bs4 import BeautifulSoup
import json
from config import headers


def scrape_cc(url):
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code != 200:
            print(f"Error: Page returned status code {response.status_code}")
            return None, None

    except requests.exceptions.RequestException as e:
        print(f"Network Error (Wifi down?): {e}")
        return None, None

    soup = BeautifulSoup(response.text, "html.parser")
    script_tags = soup.find_all("script", {"type": "application/ld+json"})

    for tag in script_tags:
        try:
            raw_json_text = tag.string
            data = json.loads(raw_json_text)
            if data.get("@type") == "Product":
                name = data["name"]
                price = float(data["offers"]["price"])
                return name, price

        except (TypeError, ValueError):
            continue

    return None, None
