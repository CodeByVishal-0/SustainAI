import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GNEWS_API_KEY")


def get_news(city):

    try:

        params = {
            "q": f"{city} environment",
            "lang": "en",
            "max": 5,
            "apikey": API_KEY
        }

        response = requests.get(
            "https://gnews.io/api/v4/search",
            params=params,
            timeout=20
        )

        response.raise_for_status()

        data = response.json()

        articles = []

        for article in data.get("articles", []):

            articles.append({
                "title": article["title"],
                "description": article["description"]
            })

        return articles

    except Exception as e:

        print(f"News API Error: {e}")

        return []