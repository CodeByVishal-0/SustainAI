from utils.news_api import get_news


def news_agent(city):

    try:
        return get_news(city)

    except Exception as e:

        print(f"News Agent Error: {e}")

        return []