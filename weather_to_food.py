def suggest_recipe_based_on_weather(weather):
    temp = weather["temperature"]
    description = weather["description"].lower()

    if "rain" in description or "drizzle" in description:
        return "soup"
    elif temp < 10:
        return "comfort food"
    elif temp > 25:
        return "salads"
    else:
        return "quick meals"