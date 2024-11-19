def map_weather_to_food(weather):
    if weather["temperature"] <10:
        return "soup"
    elif 10 <= weather["temperature"] <= 25:
        return "comfort food"
    else:
        return "salad"