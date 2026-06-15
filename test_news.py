from agents.news_agent import news_agent

articles = news_agent("Delhi")

for i, article in enumerate(articles, start=1):

    print(f"\nArticle {i}")
    print(article["title"])