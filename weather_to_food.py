def suggest_recipe_based_on_weather(weather):
    try:

        temp = float(weather.get("temperature", 20))  # Default temperature: 20°C
        description = weather.get("description", "").lower()
        city = weather.get("city", "").lower()


        recipe = suggest_by_weather(description, temp)
        if recipe:
            return recipe


        recipe = suggest_by_city(city)
        if recipe:
            return recipe


        return suggest_by_temperature(temp)

    except (TypeError, ValueError) as e:
        print(f"Error processing weather data: {e}")
        return "quick meals"


def suggest_by_weather(description, temp):

    if "rain" in description or "drizzle" in description:
        return "hearty soup" if temp < 10 else "soup"
    elif "snow" in description:
        return "stew"
    elif "thunderstorm" in description:
        return "comfort food"
    elif "clear" in description or "sunny" in description:
        if temp > 25:
            return "salad"
        elif temp > 15:
            return "grilled dishes"
        else:
            return "light meals"
    elif "cloudy" in description or "overcast" in description:
        return "casserole" if temp < 10 else "pasta"
    return None


def suggest_by_city(city):

    cuisine_map = {
        "mexico": "mexican",
        "japan": "japanese",
        "italy": "italian",
        "india": "indian",
    }
    for key, cuisine in cuisine_map.items():
        if key in city:
            return cuisine
    return None


def suggest_by_temperature(temp):

    if temp < 0:
        return "hot chocolate"
    elif temp < 10:
        return "baked goods"
    elif temp < 20:
        return "comfort food"
    elif temp < 30:
        return "barbecue"
    else:
        return "smoothies"