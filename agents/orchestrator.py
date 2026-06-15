from agents.weather_agent import weather_agent
from agents.news_agent import news_agent
from agents.impact_agent import impact_agent
from agents.rag_agent import answer_question
from utils.llm import generate_response


def generate_report(
        city,
        weather_data,
        news_data,
        impact_data,
        rag_response
):

    news_summary = "\n".join(
        [f"- {article['title']}" for article in news_data]
    )

    prompt = f"""
You are SustainAI, an AI Sustainability Expert.

Generate a professional sustainability report.

City:
{city}

Weather Data:
{weather_data}

Environmental News:
{news_summary}

Impact Analysis:
{impact_data}

Knowledge Base Insights:
{rag_response}

Generate:

# Sustainability Report

1. Sustainability Score
2. Risk Level
3. Current Environmental Conditions
4. Key News Insights
5. Sustainability Recommendations
6. Relevant SDGs
7. Final Conclusion

Use professional formatting.
"""

    return generate_response(prompt)


def orchestrator(city, question):

    weather_data = weather_agent(city)

    news_data = news_agent(city)

    impact_data = impact_agent(weather_data)

    rag_response = answer_question(question)

    report = generate_report(
        city,
        weather_data,
        news_data,
        impact_data,
        rag_response
    )

    return report