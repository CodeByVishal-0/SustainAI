from agents.weather_agent import weather_agent
from agents.news_agent import news_agent
from agents.impact_agent import impact_agent

weather = weather_agent("Mumbai")
news = news_agent("Mumbai")

impact = impact_agent(
    weather,
    news
)

print(impact)