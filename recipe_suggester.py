
from helpers.cuisine_mapping import get_cuisine_map
import random

def suggest_recipe_based_on_weather(weather):
    """
    Suggests a recipe category based on weather conditions and temperature.
    """
    try:
        temp = float(weather.get("temperature", 20))
        description = weather.get("description", "").lower()
        city = weather.get("city", "").lower()

        # First prioritize weather and temperature
        recipe_category = suggest_by_weather(description, temp)
        if recipe_category:
            return recipe_category

        # If weather-based suggestions fail, check city mapping
        recipe_category = suggest_by_city(city)
        if recipe_category:
            return recipe_category

        # Fallback to general temperature-based suggestions
        return random.choice(["main course", "soup", "BBQ", "salad"])
    except (TypeError, ValueError) as e:
        print(f"Error processing weather data: {e}")
        return "main course"

def suggest_by_weather(description, temp):
    """
    Suggests a recipe category by both weather description and temperature.
    """
    weather_temp_map = {
        "rain": {"cold": ["stew", "soup"], "mild": ["soup", "casserole"], "warm": ["curry", "ramen"]},
        "drizzle": {"cold": ["broth-based soup"], "mild": ["soup"], "warm": ["pho"]},
        "snow": {"cold": ["stew", "soup"], "mild": ["Italian"], "warm": ["curry"]},
        "thunderstorm": {"cold": ["comfort food"], "mild": ["casserole"], "warm": ["mac and cheese"]},
        "clear": {"cold": ["main course"], "mild": ["grilled dishes"], "warm": ["BBQ", "salad"]},
        "sunny": {"cold": ["main course"], "mild": ["grilled dishes"], "warm": ["BBQ", "seafood"]},
        "cloudy": {"cold": ["soup", "stew"], "mild": ["pasta"], "warm": ["casserole", "pizza"]},
        "overcast": {"cold": ["stew", "soup"], "mild": ["pasta", "Italian"], "warm": ["casserole", "gnocchi"]},
    }

    # Temperature ranges
    temp_category = categorize_temperature(temp)

    # Match description keywords to categories
    for weather_condition, temp_map in weather_temp_map.items():
        if weather_condition in description:
            suggestions = temp_map.get(temp_category, ["main course"])
            return random.choice(suggestions)

    # Fallback suggestion
    return random.choice(["main course", "soup", "BBQ", "pasta"])

def categorize_temperature(temp):
    """
    Categorizes the temperature into 'cold', 'mild', or 'warm'.
    """
    if temp < 0:
        return "cold"
    elif temp < 15:
        return "mild"
    else:
        return "warm"

def suggest_by_city(city):
    """
    Suggests a recipe category based on the city name.
    """
    cuisine_map = get_cuisine_map()
    for key, cuisine in cuisine_map.items():
        if key in city:
            return cuisine
    return None