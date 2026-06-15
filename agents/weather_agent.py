from utils.weather_api import get_weather


def weather_agent(city):
    return get_weather(city)