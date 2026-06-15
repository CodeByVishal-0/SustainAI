def calculate_score(weather_data, news_data):

    score = 100

    # Weather data
    aqi = weather_data["aqi"]
    temp = weather_data["temperature"]

    # AQI Impact
    if aqi == 5:
        score -= 40
    elif aqi == 4:
        score -= 30
    elif aqi == 3:
        score -= 20
    elif aqi == 2:
        score -= 10

    # Temperature Impact
    if temp > 45:
        score -= 25
    elif temp > 40:
        score -= 15
    elif temp > 35:
        score -= 10

    # News Impact
    news_titles = " ".join(
        article["title"].lower()
        for article in news_data
    )

    if "pollution" in news_titles:
        score -= 10

    if "air quality" in news_titles:
        score -= 10

    if "tree" in news_titles:
        score += 5

    if "renewable energy" in news_titles:
        score += 5

    return max(min(score, 100), 0)


def get_risk_level(score):

    if score >= 80:
        return "Low"

    elif score >= 60:
        return "Moderate"

    elif score >= 40:
        return "High"

    return "Critical"


def generate_recommendations(weather_data):

    recommendations = []

    if weather_data["aqi"] >= 3:
        recommendations.append(
            "Reduce outdoor activities during peak pollution hours."
        )

    if weather_data["temperature"] > 35:
        recommendations.append(
            "Conserve electricity and avoid peak heat exposure."
        )

    recommendations.append(
        "Use public transportation whenever possible."
    )

    recommendations.append(
        "Practice water conservation."
    )

    return recommendations


def impact_agent(weather_data, news_data):

    score = calculate_score(
        weather_data,
        news_data
    )

    return {
        "score": score,
        "risk_level": get_risk_level(score),
        "recommendations": generate_recommendations(
            weather_data
        )
    }