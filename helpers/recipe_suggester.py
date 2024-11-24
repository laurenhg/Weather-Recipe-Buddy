from helpers.cuisine_mapping import get_cuisine_map
from helpers.category_helper import align_with_spoonacular
import random

def suggest_recipe_based_on_weather(weather):

    try:
        temp = float(weather.get("temperature", 20))
        description = weather.get("description", "").lower()
        city = weather.get("city", "").lower()

        recipe_category = suggest_by_weather(description, temp)
        if recipe_category:
            return align_with_spoonacular(recipe_category)

        recipe_category = suggest_by_city(city)
        if recipe_category:
            return align_with_spoonacular(recipe_category)

        fallback_category = random.choice(["main course", "soup", "grill", "salad"])
        return align_with_spoonacular(fallback_category)
    except (TypeError, ValueError) as e:
        print(f"Error processing weather data: {e}")
        return "main course"

def suggest_by_weather(description, temp):

    weather_temp_map = {
        "rain": {"cold": ["stew", "soup"], "mild": ["soup", "casserole"], "warm": ["curry", "ramen"]},
        "drizzle": {"cold": ["broth-based soup"], "mild": ["soup"], "warm": ["pho"]},
        "snow": {"cold": ["stew", "soup"], "mild": ["Italian"], "warm": ["curry"]},
        "thunderstorm": {"cold": ["comfort food"], "mild": ["casserole"], "warm": ["mac and cheese"]},
        "clear": {"cold": ["main course"], "mild": ["grilled dishes"], "warm": ["grill", "salad"]},
        "sunny": {"cold": ["main course"], "mild": ["grilled dishes"], "warm": ["grill", "seafood"]},
        "cloudy": {"cold": ["soup", "stew"], "mild": ["pasta"], "warm": ["casserole", "baked"]},
        "overcast": {"cold": ["stew", "soup"], "mild": ["pasta", "Italian"], "warm": ["casserole", "gnocchi"]},
    }

    temp_category = categorize_temperature(temp)

    for weather_condition, temp_map in weather_temp_map.items():
        if weather_condition in description:
            suggestions = temp_map.get(temp_category, ["main course"])
            return random.choice(suggestions)

    return random.choice(["main course", "soup", "BBQ", "pasta"])

def categorize_temperature(temp):

    if temp < 0:
        return "cold"
    elif temp < 15:
        return "mild"
    else:
        return "warm"

def suggest_by_city(city):

    cuisine_map = get_cuisine_map()
    for key, cuisine in cuisine_map.items():
        if key in city:
            return cuisine
    return None