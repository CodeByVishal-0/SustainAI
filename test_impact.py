from agents.weather_agent import weather_agent
from agents.impact_agent import impact_agent

weather = weather_agent("Delhi")

impact = impact_agent(weather)

print(impact)