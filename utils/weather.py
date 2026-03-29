import os
import requests
from dotenv import load_dotenv

load_dotenv()

def get_weather(city):
    api_key = os.getenv("OPENWEATHER_API_KEY")
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    res = requests.get(url).json()
    if res.get("main"):
        temp = res["main"]["temp"]
        humidity = res["main"]["humidity"]
        desc = res["weather"][0]["description"]
        return {
            "temp": temp,
            "humidity": humidity,
            "desc": desc.title(),
            "display": f"🌡️ {temp}°C | 💧 {humidity}% | {desc.title()}"
        }
    return None