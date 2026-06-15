import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENWEATHER_API_KEY")


def get_weather(city):

    url = (
        f"http://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={api_key}&units=metric"
    )

    response = requests.get(url)

    if response.status_code != 200:
        return {
            "error": "Could not fetch weather data"
        }

    data = response.json()
    lat = data["coord"]["lat"]
    lon = data["coord"]["lon"]

    aqi = get_air_quality(lat, lon)

    return {
    "city": city,
    "temperature": data["main"]["temp"],
    "humidity": data["main"]["humidity"],
    "pressure": data["main"]["pressure"],
    "weather": data["weather"][0]["main"],
    "description": data["weather"][0]["description"],
    "aqi": aqi
}
def get_air_quality(lat, lon):

    url = (
        f"http://api.openweathermap.org/data/2.5/air_pollution"
        f"?lat={lat}&lon={lon}&appid={api_key}"
    )

    response = requests.get(url)

    data = response.json()

    return data["list"][0]["main"]["aqi"]