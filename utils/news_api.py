import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GNEWS_API_KEY")


def get_news(city):

    query = f"{city} environment OR pollution OR climate"

    url = (
        f"https://gnews.io/api/v4/search"
        f"?q={query}"
        f"&lang=en"
        f"&max=5"
        f"&apikey={API_KEY}"
    )

    response = requests.get(url)

    data = response.json()

    articles = []

    for article in data.get("articles", []):

        articles.append({
            "title": article["title"],
            "description": article["description"]
        })

    return articles