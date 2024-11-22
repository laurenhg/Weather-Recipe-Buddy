def suggest_recipe_based_on_weather(weather):
    try:
        temp = float(weather.get("temperature", 20))
        description = weather.get("description", "").lower()
        city = weather.get("city", "").lower()

        recipe_category = suggest_by_weather(description, temp)
        if recipe_category:
            return recipe_category

        recipe_category = suggest_by_city(city)
        if recipe_category:
            return recipe_category

        return suggest_by_temperature(temp)

    except (TypeError, ValueError) as e:
        print(f"Error processing weather data: {e}")
        return "main course"

def suggest_by_weather(description, temp):
    if "rain" in description or "drizzle" in description:
        return "soup"
    elif "snow" in description:
        return "stew"
    elif "thunderstorm" in description:
        return "main course"
    elif "clear" in description or "sunny" in description:
        if temp > 25:
            return "salad"
        elif temp > 15:
            return "barbecue"
        else:
            return "main course"
    elif "cloudy" in description or "overcast" in description:
        return "pasta"
    return None

def suggest_by_city(city):
    cuisine_map = {
        "mexico": "Mexican",
        "japan": "Japanese",
        "italy": "Italian",
        "india": "Indian",
        # Add more mappings as needed
    }
    for key, cuisine in cuisine_map.items():
        if key in city:
            return cuisine
    return None

def suggest_by_temperature(temp):
    if temp < 0:
        return "soup"
    elif temp < 10:
        return "dessert"
    elif temp < 20:
        return "main course"
    elif temp < 30:
        return "barbecue"
    else:
        return "drink"