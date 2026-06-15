from utils.news_api import get_news


def news_agent(city):

    news = get_news(city)

    return news