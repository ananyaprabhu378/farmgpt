import os
import requests
from dotenv import load_dotenv

load_dotenv()

def get_agri_articles():
    api_key = os.getenv("NEWSDATA_API_KEY")

    if not api_key:
        print("❌ API key not found")
        return []

    url = "https://newsdata.io/api/1/news"

    params = {
        "apikey": api_key,
        "q": "agriculture farming crops india",
        "country": "in",
        "language": "en",
        "category": "business,science,technology"
    }

    try:
        response = requests.get(url, params=params)
        data = response.json()

        # Debug (remove later if needed)
        print("API Response:", data)

        if data.get("results"):
            articles = []

            for a in data["results"][:8]:
                article = {
                    "title": a.get("title", "No Title"),
                    "link": a.get("link", ""),
                    "source": a.get("source_id", "Unknown"),
                    "date": a.get("pubDate", ""),
                    "image": a.get("image_url", None)
                }
                articles.append(article)

            return articles

        return []

    except Exception as e:
        print("❌ Error fetching news:", e)
        return []