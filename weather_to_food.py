def suggest_recipe_based_on_weather(weather):
    # Validate the weather dictionary
    if not isinstance(weather, dict):
        print("Error: Weather data must be a dictionary.")
        return "quick meals"

    # Check for required keys
    if "temperature" not in weather or "description" not in weather:
        print("Error: Missing required weather data.")
        return "quick meals"

    try:
        temp = float(weather["temperature"])  # Ensure temperature is numeric
        description = weather["description"].lower()

        # Determine recipe category based on weather
        if "rain" in description or "drizzle" in description:
            return "soup"
        elif "snow" in description:
            return "hot chocolate and stew"
        elif "thunderstorm" in description:
            return "comfort food"
        elif temp < 10:
            return "warm comfort food"
        elif 10 <= temp <= 25:
            return "light meals"
        elif temp > 25:
            return "salads and smoothies"
        else:
            return "quick meals"
    except (TypeError, ValueError) as e:
        print(f"Error processing weather data: {e}")
        return "quick meals"